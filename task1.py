"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Madlib")
win.geometry("300x150")

oup1 = StringVar()
oup2 = StringVar()
oup3 = StringVar()
oup1.set("Adjective")
oup2.set("Verb")
oup3.set("Noun")

def buttonfunction():
    re1 = e1.get()
    re2 = e2.get()
    re3 = e3.get()
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en1.insert(0,re1)
    en2.insert(0,re2)
    en3.insert(0,re3)

l1 = Label(win, text="It is a ")
l2 = Label(win, text="day!")
l3 = Label(win, text="Kenny plans to ")
l4 = Label(win, text=" a car to the ")
l5 = Label(win, text=" for lunch.")
e1 = Entry(win, width = 10)
e2 = Entry(win, width = 10)
e3 = Entry(win, width = 10)
en1 = Entry(win, width = 10, textvariable=oup1)
en2 = Entry(win, width = 10, textvariable=oup2)
en3 = Entry(win, width = 10, textvariable=oup3)
b1 = Button(win, text="Click to start", command=buttonfunction)

l1.place(x=5,y=5)
en1.place(x=40,y=5)
e1.place(x=40,y=25)
l2.place(x=105,y=5)
l3.place(x=130,y=5)
en2.place(x=215,y=5)
e2.place(x=215,y=25)
l4.place(x=3,y=55)
en3.place(x=73,y=55)
e3.place(x=73,y=80)
l5.place(x=135,y=55)
b1.place(x=200,y=100)
win.mainloop()








