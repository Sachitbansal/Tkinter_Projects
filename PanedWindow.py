from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("650x650")

pw = ttk.PanedWindow(root, orient=HORIZONTAL)
pw.pack(fill=BOTH, expand=True)
frame1 = ttk.Frame(pw, width=100, height=500, relief=SUNKEN)
frame2 = ttk.Frame(pw, width=300, height=500, relief=SUNKEN)
frame3 = ttk.Frame(pw, width=75, height=500, relief=SUNKEN)
pw.add(frame1, weight=1)
pw.add(frame2, weight=3)
pw.insert(1, frame3)

label = Label(frame1, text="Hello").grid(row=0, column=0, pady=25)
button = ttk.Button(frame1, text="Click me").grid(row=1, column=0, padx=20, pady=20)

root.mainloop()
