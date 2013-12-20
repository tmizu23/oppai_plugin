# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Oppai
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Oppai class from file Oppai
    from oppai import Oppai
    return Oppai(iface)
