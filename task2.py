"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import math
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("85x130")

eoutput = StringVar()
eoutput.set("Output goes here")

def factor():
    a = 1
    b = e1.get()
    c = e2.get()
    b = float(b)
    c = float(c)

    x1 = float(-b + math.sqrt(b ** 2 - 4 * 1 * c) / 2) 
    x2 = float(-b - math.sqrt(b ** 2 - 4 * 1 * c) / 2)
    if x1 > 0 and x2 > 0:
        x1 = str(x1)
        x2 = str(x2)
        answer = "(x+" + x1 + ")" + "(x+" + x2 + ")"
    elif x1 > 0 and x2 < 0:
        x1 = str(x1)
        x2 = str(x2)
        answer = "(x+" + x1 + ")" + "(x" + x2 + ")"
    elif x1 < 0 and x2 > 0:
        x1 = str(x1)
        x2 = str(x2)
        answer = "(x" + x1 + ")" + "(x+" + x2 + ")"
    elif x1 < 0 and x2 < 0:
        x1 = str(x1)
        x2 = str(x2)
        answer = "(x" + x1 + ")" + "(x" + x2 + ")"
    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = Label(win, text = "x^2 + bx + c")
l2 = Label(win, text="b= ")
l3 = Label(win, text="c= ")
e1 = Entry(win, width = 3)
e2 = Entry(win, width = 3)
b1 = Button(win, text="Click to factor", command = factor)
a_label = Label(win, text="The result is: ")
a_entry = Entry(win, width = 15, textvariable = eoutput)

l1.place(x=0,y=0)
l2.place(x=0,y=20)
l3.place(x=50,y=20)
e1.place(x=22,y=20)
e2.place(x=70,y=20)
b1.place(x=0,y=40)
a_label.place(x=0,y=65)
a_entry.place(x=0,y=90)

win.mainloop()