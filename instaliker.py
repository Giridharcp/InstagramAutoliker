## Make sure you are previously logged in to INSTAGRAM previously itself so to enable the program to function smoothly
# Refer the documentation of pyautogui for complete understanding of the program.


import pyautogui
import time
import webbrowser
name=input("Enter the user name: ")
webbrowser.open('www.instagram.com')
time.sleep(5)
x,y=pyautogui.locateCenterOnScreen(r'/searchbar.PNG')#specify where the searchbar.png is located
pyautogui.click(x,y)
time.sleep(0.2)
pyautogui.type(name)
time.sleep(0.8)
pyautogui.press('down')
pyautogui.press('enter')
def liker():
              i=0
              try:
                            while(i<=400):
                                          time.sleep(1.2)
                                          x,y=pyautogui.locateCenterOnScreen(r'/heart.PNG')#specify where the heart.png is located
                                          pyautogui.click(x-7,y)
                                          time.sleep(0.2)
                                          pyautogui.press('right')
                                          i+=1

              except TypeError:
                     time.sleep(1)
                     liker()
liker()
