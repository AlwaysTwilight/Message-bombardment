import pyautogui as pg
import time

t=int(input("Enter the wait time: "))
sentence=input("Enter the message for spamming: \n")
time.sleep(t)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        print ("Time remaining: ", countdown(t))



for i in range (10):
    pg.write(sentence)
    pg.press('enter')

