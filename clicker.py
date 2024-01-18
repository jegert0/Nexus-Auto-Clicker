import keyboard
import pyautogui
import win32api, win32con
import time

# while 1:
#     if pyautogui.locateOnScreen('button.PNG') != None:
#         print('I can see it')
#         time.sleep(0.5)
#     else:
#         print('I cant see it')
#         time.sleep(0.5)
        
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

buttonLocation = pyautogui.locateCenterOnScreen('button.PNG')

# def moveMouse(x, y):
#     win32api.SetCursorPos((x, y))

# moveMouse(buttonLocation[0], buttonLocation[1])

while keyboard.is_pressed('q') == False:
    
    buttonLocation = pyautogui.locateCenterOnScreen('button.PNG')
    if buttonLocation != None:
        click(buttonLocation[0], buttonLocation[1])
    time.sleep(6.0)
    
