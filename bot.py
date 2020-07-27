from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  253 Y:  400 RGB: ( 77,  80, 115)
#Tile 2 Position: X:  159 Y:  400 RGB: (  0,   0,   0)
#Tile 3 Position: X:  167 Y:  400 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  169 Y:  400 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(253, 400)[0] == 0:
        click(253, 400)
    if pyautogui.pixel(159, 400)[0] == 0:
        click(159, 400)
    if pyautogui.pixel(167, 400)[0] == 0:
        click(167, 400)
    if pyautogui.pixel(169, 400)[0] == 0:
        click(169, 400)
