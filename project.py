from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter import font


def validateLogin(longitude, Latitude, depth):
    print("Longitude entered :", float(longitude.get()))
    print("Latitude entered :", float(Latitude.get()))
    print("Depth entered :", float(depth.get()))
    return


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('prediction of magnitude')

# username label and text entry box
longitudeLabel = Label(tkWindow, text="Longitude").grid(row=0, column=0)
longitude = StringVar()
longitudeEntry = Entry(tkWindow, textvariable=longitude).grid(row=0, column=1)

# password label and password entry box
latitudeLabel = Label(tkWindow, text="Latitude").grid(row=1, column=0)
Latitude = StringVar()
latitudeEntry = Entry(tkWindow, textvariable=Latitude).grid(row=1, column=1)

depthLabel = Label(tkWindow, text="Depth/km").grid(row=2, column=0)
depth = StringVar()
depthEntry = Entry(tkWindow, textvariable=depth).grid(row=2, column=1)

validateLogin = partial(validateLogin, longitude, Latitude, depth)

# login button
loginButton = ttk.Button(tkWindow, text="Predict Magnitude", command=validateLogin).grid(row=4, column=1)

pred = Label(tkWindow, text='The Predicted magnitude will be: ', font=20).grid(row=5, column=1)
tkWindow.mainloop()
