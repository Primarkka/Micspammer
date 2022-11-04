"""
Micspam.py
Joni Lappalainen, PTIVIS21C TUAS
This is a simple soundboard script which has a case-insensitive 
function for playing new sounds on the fly.
"""

from logging import root
from tkinter import *
import pygame as pg 
import tkinter as tk
import os
from pygame import mixer

"""Initialization"""
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Changes path to relative path from the .py file.
pg.mixer.init() #Initialize PyGame
pg.mixer.pre_init(44100, 16, 2, 4096)  #freq etc. settings
root = tk.Tk() #Initiliaze Tkinter

root.title('Videogame Micspam') #Name of the window
screen = tk.Frame(master=root, bg="Green", padx=5) #Background
screen.pack() #Geometry manager for the widgets


"""Input Textbox"""

inputstring_var = tk.StringVar() 
entry = tk.Entry(master=screen, borderwidth=3, width=10, 
textvariable = inputstring_var,  relief=SUNKEN)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

"""Button functions"""

def your_song():
    mixer.music.load((str(entry.get()))) #Read the input from the textbox 
    mixer.music.play()

def play_csgo():
    pg.mixer.music.load("CSGO.mp3")
    pg.mixer.music.play()    
 

"""Buttons for the soundboard"""


button_1 = tk.Button(master=screen, text='Play your own song', padx=45, 
                    pady=5, width=3, command = your_song)
button_1.grid(row=1, column=1, pady=2)

button_2 = tk.Button(master=screen, text='CSGO', padx=15,
                     pady=5, width=3, command = play_csgo)
button_2.grid(row=1, column=1, pady=2)

root.mainloop()

root.mainloop()