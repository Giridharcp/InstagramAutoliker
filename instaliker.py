import pyautogui
import time
import webbrowser
i=input("Enter the user name: ")
webbrowser.open('www.instagram.com')
time.sleep(5)
def liker():
              i=0
              try:
                            while(i<=400):
                                          time.sleep(1.2)
                                          x,y=pyautogui.locateCenterOnScreen(r'C:\Users\Giridhar\Pictures\heart.PNG')
                                          pyautogui.click(x-7,y)
                                          time.sleep(0.2)
                                          pyautogui.press('right')
                                          i+=1

              except TypeError:
                     time.sleep(1)
                     liker()
liker()
