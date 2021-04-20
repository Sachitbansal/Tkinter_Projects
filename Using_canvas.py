from tkinter import *


root = Tk()
root.geometry("600x600")

canvas = Canvas(root, width=600, height=600)
canvas.pack()
# line = canvas.create_line(100, 250, 360, 25)
# canvas.itemconfig(line, fill='red', width=10)
# line2 = canvas.create_line(25, 50, 150, 150, 250, 140, 20, 50,fill='green', width=5)
# text = canvas.create_text(80, 100, text="Hello python", font=('Times', 15, 'bold'))
rectangle = canvas.create_rectangle(150, 150, 250, 200, fill='green', width=5)
oval = canvas.create_oval(350, 350, 250, 200)
arc = canvas.create_arc(120, 20, 30, 80, fill='red', width=3, start=0, extent=180)


root.mainloop()
