# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:34:56 2020
@author: ACER_DDHRUV_ARORA
"""
import winsound
winsound.Beep(1000, 100) 
import os
import pygame
import threading

os.chdir("E:/music")
songtracks = os.listdir()
pygame.mixer.init(0)

def man():
    print("""
      1.press z to next
      2.press n to stop
      3.press pa to pause
      4.press pl to unpause
      5.press re to restart the song
      """)

#-----------------------------------------------------------------------------
def ck():
    global a
    a = "1"
    print("Threading Check")
    a = input("Enter Data:")                # getting the input 
    print("YOU HAVE GIVEN : "+ a)
    if a is not None:                       # if a is None then thread will not repeat
        threading.Timer(5.0,ck).start()     # making thread repeat 
    
  
#-----------------------------------------------------------------------------

def stp():
   global A 
   A = False
   global i
   i = "xycbn"
   pygame.mixer.music.stop()

#threading.Thread(target = ck).start()

global A    
A = True
global i
global a
def musica():
    
    q = input(""" which mode do you want
              1. M - manual mode 
                 for this press M
              2. A - automatic mode
                 for this press A
              note : foe exit in auto mode give "so" as input
             """)
    
    count = 0
    
    while A:
        for i in songtracks:
            pygame.mixer.music.load(i)
            print("------Now plying -----\n"+ i +"\n-------------------")
            pygame.mixer.music.play()
            if A is not True:
                pygame.mixer.music.stop()
                break
            while (A==1) and pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)
                if q == "M":
                    man()
                    x = input("command pls")
                    if x=='n': #ends 
                        pygame.mixer.music.stop()
                        winsound.Beep(1000, 100)
                        stp()
                    elif x == "pa": #pause
                        pygame.mixer.music.pause()
                    elif x == "pl": #play
                        pygame.mixer.music.unpause()
                    elif x == "re": #restart
                         pygame.mixer.music.play()
                    elif x == "z":  #next
                         pygame.mixer.music.stop()
                         continue
                if q == "A":
                    count = count + 1
                    
                    if count==1:
                        count = count + 1
                        print(count)
                        threading.Thread(target = ck).start()
           
                    if a == "so":
                        stp() 
            
if __name__=="__main__" :
    print("Its a beta version with lots of bugs :}")
    musica()
    
