from tkinter import*
from tkinter.colorchooser import *

root = Tk()
root.title('Color Chooser')
root.geometry('300x300+200+200')

def mycolor() :
    color =askcolor()
    mylabel = Label(text='This is your selected colour', fg=color[1]).pack()

btn = Button(text='Choose colour', fg='red', command= mycolor).pack()

root.mainloop()


