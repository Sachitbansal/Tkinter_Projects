from tkinter import *

root = Tk()
root.geometry("200x200")

label = Label(root, text="Hello World")
label.config(fg='red', bg='yellow')
label.config(font="Arial")
label.config(wraplength=150)
label.config(justify=RIGHT)
label.pack()

root.mainloop()
