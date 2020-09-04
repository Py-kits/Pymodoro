import os
import time
import tkinter as tk

#app.iconbitmap('path/to/ico/icon.ico')

Pymo_app = tk.Tk()
Pymo_app.geometry('350x250')
Pymo_app.title("Pymodoro")

#def Pymostart():
#	ime = 0
#	print ime

# show timer at 00:00:00 -- display time
# add one increment +1 per second -- 	 
# Lap button adds current time to a list -- lap_list = []
# add list onclick Add(button)
# Stop button stops timer Stop(button)
# 

start_btn = tk.Button (
	text="Start",
	width=10,
	height=2,
#	fg="black",	
#	bg="blue"
)

stop_btn  = tk.Button (
	text="Stop",
	width=10,
	height=2,
#	fg="black",	
#	bg="blue"
)

lap_btn  = tk.Button (
	text="Lap",
	width=10,
	height=2,
#	fg="black",	
#	bg="blue"
)

start_btn.pack(side="right")
stop_btn.pack(side="right")
lap_btn.pack(side="right")

# Resume_button  = tk.Button (
#	text="Resume",
#	width="",
#	height="",
#	fg="black",	
#	bg="lightgrey"

#	)


Pymo_app.mainloop()