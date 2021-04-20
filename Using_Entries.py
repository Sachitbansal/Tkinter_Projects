from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x200")


def callback():
    var1 = entry.get()
    var2 = entry2.get()
    print("Your name is : {0}".format(var1))
    print("Your password is : {0}".format(var2))


entry = ttk.Entry(root, width=20)
entry2 = ttk.Entry(root, width=20)
entry.insert(0, 'Please enter your name')
entry2.config(show='.')
button = ttk.Button(root, text="Submit!", command=callback)
entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly'])

entry.pack()
entry2.pack()
button.pack()

root.mainloop()
