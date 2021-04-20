from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("380x450")
root.resizable(True, False)


def enterNumber(x):
    if entry_box.get() == "O":
        entry_box.delete(0, END)
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def enter_operator(x):
    if entry_box.get() != "O":
        length = len(entry_box.get())
        entry_box.insert(length, button_operator[x]['text'])


def func_clear():
    entry_box.delete(0, END)
    entry_box.insert(0, "O")


# result = 0
result_list = []


def func_operator():
    content = entry_box.get()
    print(content)
    result = eval(content)
    print(result)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    statusBar.configure(text='History: '+'|'.join(result_list[:5]))


def func_delete():
    length = len(entry_box.get())
    entry_box.delete(length-1, END)
    if length == 1:
        entry_box.insert(0, "O")


entry_box = Entry(font='verdana 14 bold', width=22, bd=5, justify=RIGHT, bg='white')
entry_box.insert(0, 'O')

button_number = []
for i in range(10):
    button_number.append(Button(width=4, text=str(i), font="Times 15 bold", bd=2,
                                command=lambda x=i: enterNumber(x)))

button_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        button_number[button_text].place(x=25 + j*90, y=70 + i*70)
        print(j, i)
        button_text += 1

button_operator = []
for i in range(4):
    button_operator.append(Button(width=4, font='Times 15 bold', bd=1, command=lambda x=i: enter_operator(x)))

button_operator[0]['text'] = '+'
button_operator[1]['text'] = '-'
button_operator[2]['text'] = '*'
button_operator[3]['text'] = '/'

for i in range(4):
    button_operator[i].place(x=290, y=70+i*70)

button_0 = Button(width=19, text='0', font='times 15 bold', bd=1, command=lambda x=0: enterNumber(x))
button_clear = Button(width=4, text='C', font='times 15 bold', bd=1, command=func_clear)
button_dot = Button(width=4, text='.', font='times 15 bold', bd=1, command=lambda x=".": enterNumber(x))
button_equal = Button(width=4, text='=', font='times 15 bold', bd=1, command=func_operator)
button_delete = Button(width=4, text='Del', font='times 15 bold', bd=1, command=func_delete)

statusBar = Label(root, text='History: ', height=3, anchor=W, font='Times 11 bold')
statusBar.pack(side=BOTTOM, fill=X)

button_equal.place(x=200, y=340)
entry_box.place(x=20, y=10)
button_clear.place(x=25, y=340)
button_dot.place(x=110, y=340)
button_delete.place(x=290, y=340)
button_0.place(x=25, y=280)

root.mainloop()
