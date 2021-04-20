from tkinter import *
from tkinter import messagebox
from Address_book import Add_people
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


class my_people(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My People")
        self.resizable(False, False)

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # self.top_image = PhotoImage(file='')
        self.top_image_label = Label(self.top, bg='white')
        # self.top_image.place(x=120, y=10)
        self.heading = Label(self.top, text="My People", font="arial 15 bold", fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        self.sb = Scrollbar(self.bottomFrame, orient=VERTICAL)

        self.listBox = Listbox(self.bottomFrame, width=60, height=31)
        self.listBox.grid(row=0, column=0, padx=(40, 0))
        self.sb.config(command=self.listBox.yview())
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute("SELECT * FROM persons").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listBox.insert(count, str(person[0])+"-"+person[1]+" "+person[2])
            count += 1

        button_add = Button(self.bottomFrame, text='Add', width=12, font='Sans 12 bold', command=self.func_add_people)
        button_add.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        button_update = Button(self.bottomFrame, text='Update', width=12, font='Sans 12 bold',
                               command=self.func_update_person)
        button_update.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        button_display = Button(self.bottomFrame, text='Display', width=12, font='Sans 12 bold', command=self.func_display_person)
        button_display.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        button_delete = Button(self.bottomFrame, text='Delete', width=12, font='Sans 12 bold', command=self.func_delete_people)
        button_delete.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def func_add_people(self):
        add_page = Add_people.AddPeople()
        self.destroy()

    def func_update_person(self):
        global person_id
        select_item = self.listBox.curselection()
        person = self.listBox.get(select_item)
        person_id = person.split("-")[0]
        update_page = Update()

    def func_display_person(self):
        global person_id
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]
        display_page = Display()
        self.destroy()

    def func_delete_people(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split("-")[0]
        message = messagebox.askquestion("Warning", "Are you sure want to delete this person ?", icon='warning')

        if message == 'yes':
            try:
                cur.execute("DELETE FROM persons  WHERE person_id = ?", (person_id))
                con.commit()
                messagebox.showinfo("Success", "Person has been deleted!")
                self.destroy()

            except:
                messagebox.showinfo("Info", "Person has not been deleted!")


class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Update Person")
        self.resizable(False, False)

        global person_id

        person = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        self.top_image_label = Label(self.top, bg='white')
        self.heading = Label(self.top, text="Add People", font="arial 15 bold", fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        self.label_name = Label(self.bottomFrame, text="Name", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_name.insert(0, self.person_name)
        self.entry_name.place(x=150, y=45)

        self.label_surname = Label(self.bottomFrame, text="Surname", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_surname.insert(0, self.person_surname)
        self.entry_surname.place(x=150, y=85)

        self.label_email = Label(self.bottomFrame, text="E mail", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_email.insert(0, self.person_email)
        self.entry_email.place(x=150, y=125)

        self.label_phone = Label(self.bottomFrame, text="Phone", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.place(x=150, y=165)

        self.label_address = Label(self.bottomFrame, text="Address", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.address.insert("1.0", self.person_address)
        self.address.place(x=150, y=200)

        button = Button(self.bottomFrame, text="Update Person", command=self.update_person)
        button.place(x=270, y=460)

    def update_person(self):
        person_id = self.person_id
        person_name = self.entry_name.get()
        person_surname = self.entry_surname.get()
        person_email = self.entry_email
        person_phone = self.entry_phone
        person_address = self.address.get(1.0, "end-1c")

        try:
            query = "UPDATE persons set person_name = ?, person_surname = ?, person_email = ?, person_phone = ?, " \
                    "person_address = ? WHERE person_id = ? "
            cur.execute(query, (person_name, person_surname, person_email, person_phone, person_address, person_id))
            con.commit()
            messagebox.showinfo("Success", "Person has been updated")
            self.destroy()

        except:
            messagebox.showwarning("Warning", "Couldn't update the contact", icon='warning')
            self.destroy()


class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650")
        self.title("Display Person")
        self.resizable(False, False)

        global person_id

        person = cur.execute("SELECT * FROM persons WHERE person_id = ?", (person_id,))
        person_info = person.fetchall()
        print(person_info)
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        self.top_image_label = Label(self.top, bg='white')
        self.heading = Label(self.top, text="Add People", font="arial 15 bold", fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        self.label_name = Label(self.bottomFrame, text="Name", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_name.insert(0, self.person_name)
        self.entry_name.config(state='readonly')
        self.entry_name.place(x=150, y=45)

        self.label_surname = Label(self.bottomFrame, text="Surname", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_surname.insert(0, self.person_surname)
        self.entry_surname.config(state="readonly")
        self.entry_surname.place(x=150, y=85)

        self.label_email = Label(self.bottomFrame, text="E mail", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_email.insert(0, self.person_email)
        self.entry_email.config(state="readonly")
        self.entry_email.place(x=150, y=125)

        self.label_phone = Label(self.bottomFrame, text="Phone", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottomFrame, width=30, bd=2)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.config(state="readonly")
        self.entry_phone.place(x=150, y=165)

        self.label_address = Label(self.bottomFrame, text="Address", font="arial 15 bold", fg='white', bg='#fcc324')
        self.label_address.place(x=40, y=300)
        self.address = Text(self.bottomFrame, width=23, height=15, wrap=WORD)
        self.address.insert("1.0", self.person_address)
        self.address.config(state="disabled")
        self.address.place(x=150, y=200)
