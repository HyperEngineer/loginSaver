"""
    This is a program to save login information.
    The information recorded (if present) are:
        title of the login
        date of the entry
        website associated with the login
        username
        password
        notes
    The functions are
        submit
        submit and exit
        exit
        clear
        print
"""

import sqlite3
from tkinter import *
import os
import tkinter.messagebox
import time
import calendar
import datetime
import calendar

import sys

# set up the gui
root = Tk()
root.geometry('800x500+100+100')
root.title('Login Saver')

bg_color = ['#557FFF', '#55FF7F', '#7F55FF', '#7FFF55', '#FF557F', '#FF7F55']

root.config(bg = bg_color[4])

# text boxes we need are title, website, username, password, notes
# labels we need are title, website, username, password, notes
# buttons we need are submit, submit and exit, exit, clear

frame_main = Frame(root, width = 800, height = 500, bd = 5, bg= bg_color[2], relief = RIDGE)
frame_main.grid(row = 0, column = 0, sticky = N + S + E + W)

# frame_left for the edit boxes with their labels
# frame_right for the date
frame_left = LabelFrame(frame_main, text = 'login info', width = 100)
frame_left.grid(row = 0, column = 0, padx = (5, 0), pady = (5, 5), sticky = N + W + E + S)
frame_right = LabelFrame(frame_main, text = 'entry date', width = 100, bg = '#FFFF00')
frame_right.grid(row = 0, column = 1, padx = (5, 5), pady = (5, 5), sticky = N + E + W + S)
# frame_left = LabelFrame(frame_main, text = 'login info', width = 200)
# frame_left.pack(padx = (5, 0), pady = (5, 5), anchor = NW)
# frame_right = LabelFrame(frame_main, text = 'entry date', width = 200, height = 300)
# frame_right.pack(padx = (0, 5), pady = (5, 5), anchor = NE)
frame_bottom = LabelFrame(frame_main, text = 'notes', width = 400)
frame_bottom.grid(row = 1, column = 0, columnspan = 2, padx = (5, 5), pady = (5, 5), sticky = S + E + W)

label_title = Label(frame_left, text = 'Title:', width = 10, anchor = W)
label_title.grid(row = 0, column = 0, padx = (5, 0), pady = (5, 0), sticky = W)

the_month = '' # calendar.month(2020, 3, 3)

label_date = Label(frame_right, text = the_month, width = 4, justify = LEFT, font = ('courier new', 8, 'bold'), anchor = W)
label_date.grid(row = 0, column = 2, pady = (5, 0), padx = (5,0), sticky = W)
label_website = Label(frame_left, text = 'Website:', anchor = W)
label_website.grid(row = 2, column = 0, padx = (5, 0), pady = (5, 0), sticky = W)
label_username = Label(frame_left, text = 'Username:', anchor = W)
label_username.grid(row = 4, column = 0, padx = (5, 0), pady = (5, 0), sticky = W)
label_password = Label(frame_left, text = 'Password:', anchor = W)
label_password.grid(row = 6, column = 0, padx = (5, 0), pady = (5, 0), sticky = W)
label_classification = Label(frame_left, text = 'Classification:', anchor = W)
label_classification.grid(row = 8, column = 0, padx = (5, 0), pady = (5, 0), sticky = W)
label_notes = Label(frame_bottom, text = 'Notes:', width = 100, height = 15, anchor = N + W)
label_notes.grid(row = 0, column = 0, padx = (5, 5), pady = (0, 7), sticky = N + S + E + W)

entry_title = Entry(frame_left, width = 30)
entry_title.grid(row = 0, column = 1, padx = (5, 5), pady = (5, 0), sticky = W)
entry_website = Entry(frame_left, width = 40)
entry_website.grid(row = 2, column = 1, padx = (5, 5), pady = (5, 0), sticky = W)

# wait for the title to be inputted

# is entry in the database
# if yes populate fields, give focus to the date field
# if no leave fields as is, give focus to the date field

# wait for an action
# if submit, save to the db, give focus to the title field

# if submit and exit, make sure this is desired
# if yes save to the db, quit the program
# if no do nothing, resume from last place

# if exit, make sure exit is desired
# if yes - quit, if no - nothing

# if clear, make sure this is desired
# if yes - clear all fields, if no - resume from last place

# if print, print out the info
# check if it tabular or columnar

# if print all print out the db
# check if it tabular or columnar


root.mainloop()