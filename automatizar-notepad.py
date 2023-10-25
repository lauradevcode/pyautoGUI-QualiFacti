import pyautogui
import time

pyautogui.hotkey("win", "r")
pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(2)
pyautogui.typewrite("Hello world! Meu segundo código utilizando Pyautogui.")
pyautogui.press("enter")
pyautogui.typewrite("Sejam bem vindos(a)!")
