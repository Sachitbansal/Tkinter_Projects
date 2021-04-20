from tkinter import *

root = Tk()
root.geometry("650x650")
root.title("Using Images")

labell_text = Label(root, text='Using Images ', font=("Times", 15))
logo = PhotoImage(file='icons/Kali Wall.jpg')
label_image = Label(root, image=logo)

labell_text.pack()
label_image.pack()

root.mainloop()
