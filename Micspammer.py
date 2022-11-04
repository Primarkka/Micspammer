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

root.mainloop()