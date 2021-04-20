from tkinter import *

root = Tk()
root.geometry("650x650")
root.title("Frames")

frame = Frame(root, height=300, width=300, bg='red', bd='7', relief=SUNKEN)
button1 = Button(frame, text="Button 1").pack(side=LEFT, padx=20, pady=20)
button2 = Button(frame, text="Button 2").pack(side=LEFT, padx=20, pady=10)

search_bar = LabelFrame(root, padx=20, pady=20, bg='yellow')
label = Label(search_bar, text="Search")
entry = Entry(search_bar)
button = Button(search_bar, text="Search")

label.pack(side=LEFT, padx=10)
button.pack(side=RIGHT, padx=10)
entry.pack(side=LEFT, padx=10)
search_bar.pack(side=TOP, padx=10)
frame.pack(fill=X)

root.mainloop()
