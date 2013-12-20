# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OppaiDialog
                                 A QGIS plugin
 This is Oppai Plugin.
                             -------------------
        begin                : 2013-12-20
        copyright            : (C) 2013 by Takayuki Miutani
        email                : mizutani.takayuki+oppai@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_oppai import Ui_Oppai

from qgis.core import *
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import obj2dem



class OppaiDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Oppai()
        self.ui.setupUi(self)
        self.statusBox = self.ui.textBrowser
        self.statusBox.setText(u"objファイルを選んでね♡")

    def accept(self):

            radioname = self.ui.buttonGroup.checkedButton().objectName()
            detail = 1 if self.ui.detailBox.isChecked() else 0
            if radioname == "aachanButton":
                objname = u"あ～ちゃん"
                res = 0.45 if detail else 0.9
                r = 11
                flag = 1
                qml = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "aachan.qml"
            if radioname == "nocchiButton":
                objname = u"のっち"
                res = 0.5 if detail else 1
                r = 9
                flag = 1
                qml = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "nocchi.qml"
            if radioname == "kashiyukaButton":
                objname = u"かしゆか"
                res = 0.5 if detail else 1
                r = 9
                flag = 1
                qml = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "kashiyuka.qml"
            if radioname == "tsubomiButton":
                objname = u"つぼみ"
                res = 0.35
                r = 2
                detail = 0
                flag = -1
                qml = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "tsubomi.qml"

            objfile =  QtGui.QFileDialog().getOpenFileName(self, objname, '', 'OBJ files (*.obj)')
            self.statusBox.setText(u"ただいま支度中…")

            if objfile:
                msg = u"10分ぐらい時間かかるけど待っててよ♫" if detail or flag==-1 else u"時間かかるけど待っててよ♪"
                QtGui.QMessageBox.information(self, "Oppai Plugin", msg)
                minval = obj2dem.translate(objfile,res,r,detail,flag)
                fileInfo = QtCore.QFileInfo(objfile)

                baseName = fileInfo.baseName()
                rlayer = QgsRasterLayer("%s/%s_hillshade.tif" % (fileInfo.path(),baseName),objname+u"_起伏")
                t = QgsRasterTransparency()
                t.initializeTransparentPixelList(181)
                rlayer.renderer().setRasterTransparency(t)

                QgsMapLayerRegistry.instance().addMapLayer(rlayer)
                rlayer = QgsRasterLayer("%s/%s_dem.tif" % (fileInfo.path(),baseName),objname+u"_標高")
                QgsMapLayerRegistry.instance().addMapLayer(rlayer)

                ''' cutom color rump
                r = rlayer
                s = QgsRasterShader()
                c = QgsColorRampShader()
                c.setColorRampType(QgsColorRampShader.INTERPOLATED)
                i = []
                item = QgsColorRampShader.ColorRampItem(10, QColor('#ffff00'), 'foo')
                i.append(item)
                item = QgsColorRampShader.ColorRampItem(100, QColor('#ff00ff'), 'bar')
                i.append(item)
                item = QgsColorRampShader.ColorRampItem(1000, QColor('#00ff00'), 'kazam')
                i.append(item)
                c.setColorRampItemList(i)
                s.setRasterShaderFunction(c)
                ps = QgsSingleBandPseudoColorRenderer(r.dataProvider(), 1,  s)
                r.setRenderer(ps)
                r.renderer().setOpacity(0.5)
                r.setBlendMode(QPainter.CompositionMode_Multiply)
                '''
                rlayer.loadNamedStyle(qml)
                t = QgsRasterTransparency()
                t.initializeTransparentPixelList(minval)
                rlayer.renderer().setRasterTransparency(t)
                rlayer.triggerRepaint()
                self.statusBox.setText(u"おまたせ～♡")
            else:
                self.statusBox.setText(u"objファイルを選んでね♡")
