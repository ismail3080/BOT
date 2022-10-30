import pyautogui as pg
import time

print("program will run 5s")
time.sleep(5)

for i in range(100):
	pg.write("STFUP")
	time.sleep(0.5)
	pg.press("Enter")
