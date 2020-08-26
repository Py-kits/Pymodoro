import os
import time
import tkinter as tk

app.iconbitmap('path/to/ico/icon.ico')

Pymo_app = tk.Tk()
Pymo_app.geometry('350x250')
Pymo_app.title("Pymodoro")

#def Pymo():
# show timer at 00:00:00 -- display time
# add one increment +1 per second -- 	 
# Lap button adds current time to a list -- lap_list = []
# add list onclick Add(button)
# Stop button stops timer Stop(button)
# 

start_button = tk.Button (
	text="Start",
	width="20",
	height="5",
	fg="black",	
	bg="lightgrey"
)
# stop_button  = tk.Button (
#	text="Stop",
#	width="",
#	height="",
#	fg="black",	
#	bg="lightgrey"

#	)
# Resume_button  = tk.Button (
#	text="Resume",
#	width="",
#	height="",
#	fg="black",	
#	bg="lightgrey"

#	)
# Lap_button  = tk.Button (
#	text="Lap",
#	width="",
#	height="",
#	fg="black",	
#	bg="lightgrey"
#	)

