from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x400")

probar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
probar.pack(pady=20)
probar.config(mode='indeterminate')
probar.start()
probar.stop()
probar.config(mode='determinate', maximum=50.0, value=10.0)
probar.start()
probar.stop()

value = DoubleVar()

probar.config(variable=value)
scale = ttk.Scale(root, orient=HORIZONTAL, length=200, var=value, from_=0.0, to=50.0)
scale.pack()


root.mainloop()
