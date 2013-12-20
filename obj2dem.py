# -*- coding: utf-8 -*-
import sys,os,math,subprocess
import gdal,ogr

##### setting ####
# model1(a-chan): 0.9 11.0 0 1
# model2(nocchi): 1.0 9.0 0 1
# model3(kashiyuka): 1.0 9.0 0 1
# tsubomi: 0.35 2.0 0 -1
# model1(a-chan): 0.45 10 1 1
# model2(nocchi): 0.5 9 1 1
# model3(kashiyuka): 0.5 9 1 1


def myprocess(cmd):
    #print cmd
    #proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,env={"PATH": "/Library/Frameworks/GDAL.framework/Programs:/usr/local/bin"})
    proc = subprocess.Popen(cmd, shell=True,env={"PATH": "/Library/Frameworks/GDAL.framework/Programs:/usr/local/bin"})
    proc.wait()
    #print proc.stdout.readlines()
    #print proc.stderr.readlines()

def translate(filename,res,r,detail,flag):
    #around Mt.fuji
    offsetx = 15435509
    offsety = 4204037
    offsetz = 3000
    scale = 50

    #no offset
    #offsetx = 0
    #offsety = 0
    #offsetz = 0
    #scale = 1

    #around Mt.fuji
    if flag==-1:
        offsetx = 15683205
        offsety = 3154411
        offsetz = 3000
        scale = 15

    path = filename
    root, ext = os.path.splitext(path)
    base = os.path.basename(root)
    radius1 = r*res*scale
    radius2 = 1.5*r*res*scale

    ##### end setting ####

    ##### read vertices from obj and interpolate
    csvfile = root+"_points.csv"
    f = open(path,'r')
    of = open(csvfile,'w')
    of.write("x,y,z\n")

    x=[]
    y=[]
    z=[]

    for line in f:
        str = line.split(' ')
        if str[0]=="v":
            x.append(flag*float(str[1])*scale+offsetx)
            y.append(flag*float(str[2])*scale+offsety)
            z.append(-1*flag*float(str[3])*scale+offsetz)
            of.write(("%f,%f,%f\n") % (flag*float(str[1])*scale+offsetx,flag*float(str[2])*scale+offsety,-1*flag*float(str[3])*scale+offsetz))
        if str[0]=="f" and flag == 1 and detail == 1:
            p1 = int(str[1].split('/')[0])
            p2 = int(str[2].split('/')[0])
            p3 = int(str[3].split('/')[0])
            of.write(("%f,%f,%f\n") % ((x[p1-1] + x[p2-1])/2,(y[p1-1] + y[p2-1])/2,(z[p1-1] + z[p2-1])/2))
            of.write(("%f,%f,%f\n") % ((x[p2-1] + x[p3-1])/2,(y[p2-1] + y[p3-1])/2,(z[p2-1] + z[p3-1])/2))
            of.write(("%f,%f,%f\n") % ((x[p3-1] + x[p1-1])/2,(y[p3-1] + y[p1-1])/2,(z[p3-1] + z[p1-1])/2))
            of.write(("%f,%f,%f\n") % ((x[p1-1] + x[p2-1] + x[p3-1])/3,(y[p1-1] + y[p2-1] + y[p3-1])/3,(z[p1-1] + z[p2-1] + z[p3-1])/3))

    of.close()
    
    #### write vrt file
    vrtfile = root + "_points.vrt"
    vrtstr = "<OGRVRTDataSource><OGRVRTLayer name='%s'><SrcDataSource>%s</SrcDataSource><GeometryType>wkbPoint</GeometryType><GeometryField encoding='PointFromColumns' x='x' y='y' /></OGRVRTLayer></OGRVRTDataSource>" % (base+"_points",csvfile)
    of = open(vrtfile,'w')
    of.write(vrtstr)
    of.close()
    
    
    vds = ogr.Open(vrtfile)
    layer = vds.GetLayer()
    extent = layer.GetExtent()
    

    width = math.ceil((extent[1]-extent[0] + 2*radius1)/(res*scale))
    height = math.ceil((extent[3]-extent[2] + 2*radius2)/(res*scale))
    
    maxtiffile = root + "_max.tif"
    cmd = "gdal_grid --config GDAL_NUM_THREADS ALL_CPUS --config GDAL_CACHEMAX 2048 -zfield z -a maximum:radius1=%s:radius2=%s:angle=0:nodata=0 -outsize %s %s -txe %s %s -tye %s %s -l %s %s %s" % (radius1,radius2,width,height,extent[0]-radius1,extent[1]+radius1,extent[3]+radius2,extent[2]-radius2,base+"_points",vrtfile,maxtiffile)
    myprocess(cmd)
    
    mintiffile = root + "_min.tif"
    cmd = "gdal_grid --config GDAL_NUM_THREADS ALL_CPUS --config GDAL_CACHEMAX 2048 -zfield z -a minimum:radius1=%s:radius2=%s:angle=0:nodata=0 -outsize %s %s -txe %s %s -tye %s %s -l %s %s %s" % (radius1,radius2,width,height,extent[0]-radius1,extent[1]+radius1,extent[3]+radius2,extent[2]-radius2,base+"_points",vrtfile,mintiffile)
    myprocess(cmd)

    ## extract front side points. diff from max and min
    # calc minimum elevation for nodata setting
    #gdal.AllRegister() error???
    
    rds = gdal.Open(maxtiffile)
    datamax = rds.GetRasterBand(1).ReadAsArray()
    (upper_left_x, x_size, x_rotation, upper_left_y, y_rotation, y_size) = rds.GetGeoTransform()
    rds = None
    rds = gdal.Open(mintiffile)
    datamin = rds.GetRasterBand(1).ReadAsArray()
    rds = None
    
    demfile = root+"_dem.csv"
    of = open(demfile,'w')
    of.write("x,y,z\n")

    minz = 9999
    for feat in layer:
        geom = feat.GetGeometryRef()
        x = geom.GetX()
        y = geom.GetY()
        z = float(feat.GetField("z"))
        cellx = int((x - upper_left_x)/x_size)
        celly = int((y - upper_left_y)/y_size)
        maxval = datamax[celly][cellx]
        minval = datamin[celly][cellx]
        if maxval-z <= z - minval:
         of.write("%f,%f,%f\n" % (x,y,z))
         if minz > z: minz = z
    vds = None
    of.close()
    
    vrtdemfile = root + "_dem.vrt"
    vrtdemstr = "<OGRVRTDataSource><OGRVRTLayer name='%s'><SrcDataSource>%s</SrcDataSource><GeometryType>wkbPoint</GeometryType><GeometryField encoding='PointFromColumns' x='x' y='y' /></OGRVRTLayer></OGRVRTDataSource>" % (base+"_dem",demfile)
    of = open(vrtdemfile,'w')
    of.write(vrtdemstr)
    of.close()

    ## front side dem
    demtiffile = root + "_dem.tif"

    
    cmd = "gdal_grid --config GDAL_NUM_THREADS ALL_CPUS --config GDAL_CACHEMAX 2048 -zfield z -a invdist:power=1.2:smoothing=1:radius1=%s:radius2=%s:angle=8:max_points=100:nodata=%s -outsize %s %s -txe %s %s -tye %s %s -l %s %s %s" % (radius1,radius2,minz,width,height,extent[0]-radius1,extent[1]+radius1,extent[3]+radius2,extent[2]-radius2,base+"_dem",vrtdemfile,demtiffile)
    myprocess(cmd)

    ## hillshade
    hillshadefile = root + "_hillshade.tif"
    cmd = "gdaldem hillshade %s %s" % (demtiffile,hillshadefile)
    myprocess(cmd)
       

    #print "finish"

    return minz

