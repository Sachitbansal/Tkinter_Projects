from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("650x650")


def print_me():
    selected_items = list_book.curselection()
    for item in selected_items:
        print(list_book.get(item))


def delete_me():
    selected_items = list_book.curselection()
    for item in selected_items:
        list_book.delete(item)


list_book = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
list_book.insert(0, "Python")
list_book.insert(1, "C++")
list_book.insert(3, "C")
list_book.insert(4, "PHP")
button = ttk.Button(root, text="Print", command=print_me).place(x=250, y=300)
button2 = ttk.Button(root, text="Delete", command=delete_me).place(x=350, y=300)

list_book.pack(pady=25, )

root.mainloop()
