import pygame
import time

def countdown(t):
    while t:
        min, secs = divmod(t, 60)
        timer = '{:2d}:{:2d}'.format(min, secs)
        print(timer)
        time.sleep(1)
        t -= 1
    
    print("End")

t = 10

countdown(int(t))