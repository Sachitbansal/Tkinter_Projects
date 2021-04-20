import webbrowser
from tkinter import *

root = Tk()
root.title("WebBrowser")
root.geometry("300x200")

print("This little program will take you to any website you want to.")
print()
assignment_name = str(input("Pls enter the URL of the assignment:"))
print("Now Navigate yourself to Python Tkinter app which has been opened in you system and click the button")


def copy_assignment():
    webbrowser.open(assignment_name)


def google():
    webbrowser.open("www.google.com")


copy_assignment = Button(root, text="Copy assignment", command=copy_assignment).pack()
my_google = Button(root, text="Open Google", command=google).pack(pady=20)

root.mainloop()
