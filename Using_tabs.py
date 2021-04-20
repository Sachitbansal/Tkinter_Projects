from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("650x650")

icon = PhotoImage()
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=True)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text="First Tab")
tabs.add(tab2, text="Second Tab")
label = ttk.Label(tab1, text="Hello").place(x=200, y=200)
button = ttk.Button(tab2, text="Click Me").place(x=250, y=50)


root.mainloop()
