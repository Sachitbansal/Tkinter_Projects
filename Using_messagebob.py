from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("250x250")


def callback():
    mbox = messagebox.askquestion("Delete", "Are you sure you want to delete ?", icon='warning')
    if mbox == 'yes':
        print("Deleted")
    else:
        print("Failed to delete")


def callback2():
    messagebox.showinfo("Success", "Well Done")
    print("You Clicked Okay")


button = ttk.Button(root, text="Delete", command=callback).grid(row=0, column=0)
button2 = ttk.Button(root, text="info", command=callback2).grid(row=0, column=1, padx=10)

root.mainloop()
