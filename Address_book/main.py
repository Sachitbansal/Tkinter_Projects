from tkinter import *
import datetime
from Address_book import About_us, Add_people, my_people

date = datetime.datetime.now().date()


def func_add_people():
    addpeoplewindow = Add_people.AddPeople()


def openMy_People():
    people = my_people.my_people()


class Application(object):
    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=150, bg='white', )
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file='icons/address.png')
        self.top_image_label = Label(self.top, bg='white')
        self.top_image.place(x=100, y=10)
        self.heading = Label(self.top, text="My Address Book App", font="arial 15 bold", fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)
        self.date_label = Label(self.top, text="Today's date: " + str(date), font='times 12 bold', bg='white',
                                fg='#ffa500')
        self.date_label.place(x=450, y=5)

        self.person_button = Button(self.bottom, text="My People  ", font='arial 12 bold', command=openMy_People)
        self.person_button.place(x=250, y=10)

        self.addperson_button2 = Button(self.bottom, text="Add People", font='arial 12 bold', command=func_add_people)
        self.addperson_button2.place(x=250, y=70)

        self.aboutperson_button3 = Button(self.bottom, text="About Us    ", font='arial 12 bold', command=About_us.main)
        self.aboutperson_button3.place(x=250, y=130)


def main():
    root = Tk()
    app = Application(root)
    root.title("Address Book app")
    root.geometry("650x550")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
