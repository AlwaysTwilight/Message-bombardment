import pyautogui as pg
import time

t=int(input("Enter the wait time: "))  #Time after which the message will get spammed on the on screen available section where cursor is placed 
sentence=input("Enter the message for spamming: \n") #Text for spamming
time.sleep(t)

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
        print ("Time remaining: ", countdown(t))



for i in range (10):   #10 is the no of times the texts will get spammed, if you want to spam more than 10 texts messages change it to the desired number
    pg.write(sentence)
    pg.press('enter')

