from tkinter import *

root = Tk()
root.geometry("450x450")

title = Label(root, text="Place geometry manager", font=("Verdana", 15))
name_text = Label(root, text="Name :")
pass_text = Label(root, text="Password :")
name_input = Entry(root, width="30")
pass_input = Entry(root, width="30")
button = Button(root, text="Save")
button2 = Button(root, text="Click me", bg="red").place(relx=0.5, rely=0.5, anchor="center")

title.place(x=100, y=20)
name_text.place(x=20, y=80)
name_input.place(x=100, y=80)
pass_text.place(x=20, y=110)
pass_input.place(x=100, y=110)
button.place(x=250, y=140)


root.mainloop()
