# imports
from tkinter import *
import tkinter as tint
import time
from datetime import date

# frame the clock window
the_clock = tint.Tk()
the_clock.title("Digital Clock")


# give the app an image icon
picon = tint.PhotoImage(file="gallery/clock.png")
the_clock.iconphoto(False, picon)

text_font = ("Boulder", 12, 'bold')


# display the time and date here
label = Label(the_clock, font=text_font, bg="cyan", fg="#363529", bd=12)
label.grid(row=0, column=1)


# clock function
def clock():
    to_day = date.today()
    # the day today
    this_day = time.strftime("%A")
    # the time right now
    the_time = time.strftime("%X")
    # the date today
    day_to_day = to_day.strftime("%d/%m/%Y")
    label.config(text=this_day + "\n" + the_time + "\n" + day_to_day)
    return label.after(200, clock)


clock()


the_clock.mainloop()
