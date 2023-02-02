import pyautogui
import random
import keyboard

while True:
    if keyboard.is_pressed("e"):
        break
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    duration = random.uniform(0.1, 2)
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.sleep(0.2)