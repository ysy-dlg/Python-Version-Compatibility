#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2013-2014  Diego Torres Milano
Created on 2015-01-21 by Culebra v9.2.1
                      __    __    __    __
                     /  \  /  \  /  \  /  \ 
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \ 
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
'''


import re
import sys
import os


try:
    sys.path.insert(0, os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient

TAG = 'CULEBRA'

_s = 5
_v = '--verbose' in sys.argv


kwargs1 = {'ignoreversioncheck': False, 'verbose': True, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
kwargs2 = {'startviewserver': True, 'forceviewserveruse': False, 'autodump': False, 'ignoreuiautomatorkilled': True}
vc = ViewClient(device, serialno, **kwargs2)

device.Log.d(TAG, "dumping content of window=-1",  _v)
vc.dump(window=-1)

def doSomething(view):
    if view.getClass() == 'android.widget.TextView':
        print view.getText()
while True:
    device.Log.d(TAG, "finding view with id=android:id/list",  _v)
    android___id_list = vc.findViewByIdOrRaise("android:id/list")
    # check if scrollable
    if not android___id_list.isScrollable():
        break
    vc.traverse(root=android___id_list, transform=doSomething)
    device.Log.d(TAG, "Scrolling",  _v)
    device.dragDip((185.0, 499.0), (191.0, 175.5), 200, 20, 0)
    vc.sleep(1)
    device.Log.d(TAG, "dumping content of window=-1",  _v)
    vc.dump(window=-1)