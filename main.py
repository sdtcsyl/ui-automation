# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:37:56 2019

@author: Eric Su
"""

import os
from ctypes import windll
import win32_mouseevent
import win32_keyboard
import time

username = '' # your username
password = '' # your password


os.system("chrome.exe mail.qq.com")  
time.sleep(10)
win32_mouseevent.left_double_click(1804,636)
time.sleep(1)
win32_keyboard.typer(username)
time.sleep(2)
win32_mouseevent.left_double_click(1804,736)
time.sleep(1)
win32_keyboard.clear()
time.sleep(1)
win32_keyboard.typer(password)
time.sleep(2)
win32_mouseevent.left_click(1804,936)



####################################################???????
WM_LBUTTONDBLCLK = 0x0203
MK_LBUTTON = 0x0001
if __name__=='__main__':
    hProgman = windll.User32.FindWindowW( "Chrome_WidgetWin_0", 0 ) # use spyxx or syp++ to find the first parameters
    if hProgman != 0:
        hFolder = windll.User32.FindWindowExW( hProgman, 0, "SHELLDLL_DefView", 0 )
        if hFolder != 0:
            hListView = windll.User32.FindWindowExW( hFolder, 0, "SysListView32", 0 )
            if hListView != 0:
                windll.User32.PostMessageW( hListView, WM_LBUTTONDBLCLK, MK_LBUTTON,
                                            110 + (65536*32) )
                

