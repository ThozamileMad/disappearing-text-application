from tkinter import *
from tkinter import messagebox


def countdown(count=3):
    global text_before
    if count > -1:
        counter = window.after(1000, countdown, count-1)
    if count == 0 and text_before == text_after:
        window.after_cancel(counter)
        countdown()
        textbox.delete('1.0', END)
    if count == 0 and text_before != text_after:
        window.after_cancel(counter)
        countdown()
        text_before = text_after

def text_counter(e):
    global text_after
    text_after = textbox.get(1.0, END + "-1c") + e.char
    
    
window = Tk()

text_before = ""
text_after = ""

title = Label(text="Disappearing Text Application", font=("forte", 20))
title.grid(row=0, column=0)

textbox = Text(font=("Helvetica", 0), height=5)
textbox.grid(row=1, column=0)

start_button = Button(text="Begin", command=lambda: [countdown(), textbox.delete('1.0', END)])
start_button.grid(row=2, column=0)

info_button = Button(text="Info?", command=lambda: messagebox.showinfo(title="How this works", message="Write anything. But know that if you stop writing for too long the text will be cleared and saved into a file.") )
info_button.place(x=7, y=5)

textbox.bind("<Key>", text_counter)

window.mainloop()
