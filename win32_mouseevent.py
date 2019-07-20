# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 20:47:40 2019

@author: Eric Su
"""

from ctypes import windll

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_MOVE = 0x0001 
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

# http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx

def set_cursor_pos(x, y):
    windll.user32.SetCursorPos(x, y)

def left_click(x, y):
        windll.user32.SetCursorPos(x, y)
        windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0,0) # left down
        windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0,0) # left up
        
def right_click(x, y):
        windll.user32.SetCursorPos(x, y)
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0,0) # right down
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0,0) # right up
        
def left_double_click(x, y):
        windll.user32.SetCursorPos(x, y)
        windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0,0) # left down
        windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0,0) # left up
        windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0,0) # left down
        windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0,0) # left up
        
def right_double_click(x, y):
        windll.user32.SetCursorPos(x, y)
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0,0) # right down
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0,0) # right up
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0,0) # right down
        windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0,0) # right up



#https://github.com/neal365/python/blob/master/mouseClick.py 
#https://www.jb51.net/article/114658.htm
        
'''
Let the computer auto click!
Neal : njugui@gmail.com
'''

import win32gui
import win32api
import win32con
import time

pos_list = [(1306,662), 
            (550,500), 
            (550,550), 
            (500,550), 
            (500,500)]

def LeftClick(handle, pos):
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp) 
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
   
def RightClick(handle, pos):
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32api.SendMessage(handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, tmp) 
    win32api.SendMessage(handle, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, tmp)

def MouseMove(handle, pos):
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp) 
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
           
def get_curpos():
    return win32gui.GetCursorPos()

def get_win_handle(pos):
    return win32gui.WindowFromPoint(pos)
    
if __name__ == '__main__':
    time.sleep(10)
    pos1 = (1306, 662)
    pos2 = (1398, 658)
    handle = get_win_handle(pos1)
    LeftClick(handle, pos1)  
    handle = get_win_handle(pos2)
    LeftClick(handle, pos2)  
     
    '''
    for i in range(len(pos_list)):
        handle = get_win_handle(pos_list[i])
        LeftClick(handle, pos_list[i])
        time.sleep(2)'''       