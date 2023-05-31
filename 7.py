import pyautogui
import time
import keyboard as keyb
while True:
    keyb.wait("f10")
    #cursor_start_position = pyautogui.position()

    while not keyb.is_pressed("f9"):
        #pyautogui.moveTo(cursor_start_position)
        pyautogui.mouseDown()
        #pyautogui.moveRel(0, 100)
        #pyautogui.PAUSE = 1
