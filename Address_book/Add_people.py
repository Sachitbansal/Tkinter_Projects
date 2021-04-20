from tkinter import *
import sqlite3
from tkinter import messagebox


con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+550+200")
        self.title("Add People")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # self.top_image = PhotoImage(file='')
        self.top_image_label = Label(self.top, bg='white')
        # self.top_image.place(x=120, y=10)
        self.heading = Label(self.top, text="Add People", font="arial 15 bold", fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        self.label_name = Label(self.bottomFrame, text="Name", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_name.insert(0, "Please Enter a name")
        self.entry_name.place(x=150, y=45)

        self.label_surname = Label(self.bottomFrame, text="Surname", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_surname.insert(0, "Please Enter a Surname")
        self.entry_surname.place(x=150, y=85)

        self.label_email = Label(self.bottomFrame, text="E mail", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_email.insert(0, "Please Enter an Email")
        self.entry_email.place(x=150, y=125)

        self.label_phone = Label(self.bottomFrame, text="Phone", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_phone.insert(0, "Please Enter a Phone Number")
        self.entry_phone.place(x=150, y=165)

        self.label_address = Label(self.bottomFrame, text="Address", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=300)
        self.text_address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.text_address.place(x=150, y=200)

        button = Button(self.bottomFrame, text="Add Person", command=self.add_person)
        button.place(x=270, y=460)

    def add_person(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.text_address.get(1.0, 'end-1c')

        if name and surname and email and phone and address != "":
            try:
                query = "INSERT INTO 'persons'(person_name, person_surname, person_email , person_phone, " \
                        "person_address) VALUES(?,?,?,?,?) "
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success", "Successfully added", icon='info')

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields cannot be empty!", icon="warning")
