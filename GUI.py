# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:09:14 2018

@author: Ansari
"""

from tkinter import *
gui = Tk()
gui.state('zoomed')
gui.configure(background='#38A1F3')

#Label-heading
l = Label(gui,text='Welcome to Twitter sentimental Analysis',fg='white',bg= '#38A1F3',height=10)
font = ('times',20,'bold')
l.config(font=font)
l.pack(anchor='center')

#Label-text
label = Label(gui,text='Enter the input Here',bg='#38A1F3',fg='white').pack()
label = Label(gui,text='Enter the input Here',fg='#38A1F3',bg='#38A1F3').pack()

#Input
v = StringVar()
entry = Entry(gui,bd=3,width=45,textvariable=v).pack()
label = Label(gui,text='Enter the input Here',fg='#38A1F3',bg='#38A1F3').pack()


#button
def newframe():
    frame = Toplevel(gui)
    label = Label(frame,text=v.get()).pack()
    button = Button(frame,text='click here to quit',command=frame.destroy).pack()

button = Button(gui,text='Calculate sentiment',command=newframe).pack()

gui.mainloop()
