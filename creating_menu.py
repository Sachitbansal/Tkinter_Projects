from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("650x650")
root.title("Creating Menu")


def func_Exit():
    mbox = messagebox.askquestion("Exit", "Are you sure you want to Exit?")
    if mbox == "yes":
        root.destroy()


menuBar = Menu(root)
root.config(menu=menuBar)
file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file)
file.add_command(label='New')
file.add_separator()
file.add_command(label='Open')
file.add_separator()
file.add_command(label='Save')
file.add_separator()
file.add_command(label='Exit', command=func_Exit)
edit = Menu(menuBar)
about = Menu(menuBar)


root.mainloop()
