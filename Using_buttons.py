from tkinter import *

root = Tk()
root.geometry("300x300")


def callback():
    a = 1
    label.config(text=a, fg='red', bg='yellow')


label = Label(root, text="Hello User")
button = Button(root, text="Click me!", command=callback, state='disabled')
button['state'] = 'normal'

label.pack()
button.pack()

root.mainloop()
