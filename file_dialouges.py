from tkinter import *
from tkinter import filedialog, colorchooser
root = Tk()
root.geometry("600x600")


def openfile():
    file_name = filedialog.askopenfilename(initialdir='/', title='select a file', filetypes=(("Text Files", ".txt"),
                                           ("All files", "*.*")))
    content = open(file_name).read()
    text_editor.insert(END, content)


def savefile():
    my_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if my_file is None:
        return
    content = text_editor.get(1.0, 'end-1c')
    my_file.write(content)


def change_color():
    color = colorchooser.askcolor()
    text_editor.configure(fg=color[1])


text_editor = Text(root, width=25, height=15)
text_editor.pack()
button = Button(root, text="Open", command=openfile).pack(side=LEFT, padx=(170, 20))
button2 = Button(root, text="Save", command=savefile).pack(side=LEFT)
button3 = Button(root, text="color", command=change_color).pack(side=LEFT)

root.mainloop()
