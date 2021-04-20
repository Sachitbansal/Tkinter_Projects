from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("650x650")


def callback(event):
    item = treeview.identify('item', event.x, event.y)
    print("You Clicked on {}".format(treeview.item(item, "text")))


treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text='First item')
treeview.insert('', '1', 'item2', text='Second item')
treeview.insert('', '2', 'item3', text='third item')
treeview.insert('', '3', 'item4', text='fourth item')
treeview.move('item3', 'item1', 'end')
treeview.bind('<Double-1>', callback)


root.mainloop()
