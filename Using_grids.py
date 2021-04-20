from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x400")


def callback():
    print("Your name is: {0}".format(entry.get()))
    print("Your pass is: {0}".format(entry2.get()))
    if chvar.get == 1:
        print("Remembered")
    else:
        print("Didn't remember")
    print(gender.get())
    print(month.get())


entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30, show='*')
entry.insert(0, 'PLs Enter your name')
entry2.insert(0, 'PLs Enter your name')
button = ttk.Button(root, text="Enter", command=callback)
lbltitle = ttk.Label(root, text="Our  tittle here", font=("Arial", 22))
lblname = ttk.Label(root, text="Your name: ")
lblpass = ttk.Label(root, text="Your password: ")

lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W + E, pady=5)

chvar = IntVar()
chvar.set(0)

chbox = Checkbutton(root, text="Remember me", variable=chvar, font=("Arial", 15))
chbox.grid(row=4, column=0, columnspan=2, sticky=E)

gender = StringVar()
ttk.Radiobutton(root, text="male", var=gender, value="Male").grid(row=5, column=0)
ttk.Radiobutton(root, text="female", var=gender, value="female").grid(row=5, column=1)

month = StringVar()
combobox = ttk.Combobox(root, textvariable=month, state="readonly", value=('January', 'February', 'March', 'April',
                                                                             'May', 'June', 'July', 'August',
                                                                             'September', 'October', 'November',
                                                                             'December')).grid(row=6, column=1)

year = StringVar()
Spinbox(root, from_=1990, to=2020, textvariable=year, state="readonly").grid(row=6, column=1)

root.mainloop()
