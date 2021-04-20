from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

show_Status_bar = True
showToolbar = True
url = ""
fontFamily = "Times"
fontSize = 12
textChanged = False


class FindDialog(Toplevel):
    def __init__(self, parent, *args, **kwargs):
        Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry("450x200")
        self.title("Find")
        self.resizable(False, False)

        # labels
        txtFind = Label(self, text="Find: ")
        txtReplace = Label(self, text="Replace: ")
        txtReplace.place(x=20, y=60)
        txtFind.place(x=20, y=20)

        # Entries
        self.findInput = Entry(self, width=30)
        self.replaceInput = Entry(self, width=30)
        self.findInput.place(x=100, y=20)
        self.replaceInput.place(x=100, y=60)

        # Buttons
        self.btnFind = ttk.Button(self, text="Find", command=self.parent.findwords)
        self.btnReplace = ttk.Button(self, text="Replace", command=self.parent.replacewords)
        self.btnFind.place(x=160, y=90)
        self.btnReplace.place(x=240, y=90)


class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # File
        self.open_icon = PhotoImage(file='icons/icons8-open-envelope-30.png')
        self.file = Menu(self, tearoff=0)
        self.file.add_command(label="New", compound=LEFT, accelerator='Ctrl+N', command=self.parent.newFile)
        self.file.add_command(label='Open', accelerator='Ctrl+O', compound=LEFT,
                              command=self.parent.openFile)
        self.file.add_command(label='Save', accelerator='Ctrl+S', compound=LEFT, command=self.parent.saveFile)
        self.file.add_command(label='Save As', accelerator='Ctrl+Shift+S', compound=LEFT,
                              command=self.parent.save_as_File)
        self.file.add_command(label='Exit', compound=LEFT, command=self.parent.exit)

        # Edit Menu
        self.edit = Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: self.parent.text_editor.
                              event_generate("<Control c>"))
        self.edit.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: self.parent.text_editor.
                              event_generate("<Control v>"))
        self.edit.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: self.parent.text_editor.
                              event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', accelerator='Ctrl+Alt+X', command=lambda: self.parent.text_editor.
                              delete(1.0, END))
        self.edit.add_command(label='Find', accelerator='Ctrl+F', command=self.parent.find)

        # View Menu
        global show_Status_bar
        global showToolbar
        self.view = Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Toolbar", variable=showToolbar,
                                  command=self.parent.hidetoolbar)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Status bar", variable=show_Status_bar,
                                  command=self.parent.hideStatusbar)

        # About Us
        self.about = Menu(self, tearoff=0)

        # Themes menu
        self.themes = Menu(self, tearoff=0)
        self.color_list = {
            'Default': '#000000.#FFFFFF',
            'Tomato': '#ffff00.#ff6347',
            'Lime Green': '#fffff0.#32cd32',
            'Magenta': '#fffafa.#ff00ff',
            'Royal Blue': '#ffffbb.#4169e1',
            'Medium Blue': '#d1e7e0.#0000cd',
            'Dracula': '#ffffff.#000000'
        }
        self.theme_choice = StringVar()
        for i in sorted(self.color_list):
            self.themes.add_radiobutton(label=i, variable=self.theme_choice, command=self.changeTheme)

        self.add_cascade(label='File', menu=self.file)
        self.add_cascade(label='Menu', menu=self.edit)
        self.add_cascade(label="View", menu=self.view)
        self.add_cascade(label="Templates", menu=self.themes)
        self.add_cascade(label="About", command=self.parent.about_Message)

    def changeTheme(self):
        selected_theme = self.theme_choice.get()
        fg_bg_color = self.color_list.get(selected_theme)
        foreground, background = fg_bg_color.split(".")
        self.parent.text_editor.config(background=background, foreground=foreground)


class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap=WORD, relief=FLAT)
        self.pack(expand=True, fill=BOTH)
        scroll = Scrollbar(self, bd=5, relief=SUNKEN)
        self.config(yscrollcommand=scroll.set)
        scroll.config(command=self.yview)
        scroll.pack(side=RIGHT, fill=Y)


class StatusBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=BOTTOM)
        self.config(text='Status Bar')


class Toolbar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=TOP, fill=X)

        # Font Size and Family
        self.cbFont = ttk.Combobox(self)
        self.cbFont_size = ttk.Combobox(self)
        self.cbFont.pack(side=LEFT, padx=(5, 10))
        self.cbFont_size.pack(side=LEFT)

        # bold
        self.bold_icon = PhotoImage(file='icons/icons8-bold-24.png')
        buttonBold = ttk.Button(self, image=self.bold_icon, command=self.parent.change_bold)
        buttonBold.pack(side=LEFT, padx=5)

        # italic
        self.italic_icon = PhotoImage(file='icons/icons8-italic-26.png')
        buttonItalic = ttk.Button(self, image=self.italic_icon, command=self.parent.change_italic)
        buttonItalic.pack(side=LEFT, padx=5)

        # Underline
        self.underline_icon = PhotoImage(file='icons/icons8-underline-26.png')
        button_underline = ttk.Button(self, image=self.underline_icon, command=self.parent.change_underline)
        button_underline.pack(side=LEFT, padx=5)

        # Font Color
        self.font_color_icon = PhotoImage(file='icons/icons8-text-color-26.png')
        button_font_color = ttk.Button(self, image=self.font_color_icon, command=self.parent.changeFontColor)
        button_font_color.pack(side=LEFT, padx=5)

        # Align LEFT
        self.align_left_icon = PhotoImage(file='icons/icons8-align-left-26.png')
        button_align_left = ttk.Button(self, image=self.align_left_icon, command=self.parent.align_left)
        button_align_left.pack(side=LEFT, padx=5)

        # Align Middle
        self.align_middle_icon = PhotoImage(file='icons/icons8-align-justify-24.png')
        button_align_middle = ttk.Button(self, image=self.align_middle_icon, command=self.parent.align_center)
        button_align_middle.pack(side=LEFT, padx=5)

        # Align right
        self.align_right_icon = PhotoImage(file='icons/icons8-align-right-26.png')
        button_align_right = ttk.Button(self, image=self.align_right_icon, command=self.parent.align_right)
        button_align_right.pack(side=LEFT, padx=5)

        fonts = font.families()
        fontList = []
        fontSizeList = []

        for i in range(8, 80):
            fontSizeList.append(i)

        for i in fonts:
            fontList.append(i)

        self.fontVar = StringVar()
        self.cbFont.config(values=fontList, textvariable=self.fontVar)
        self.cbFont.current(0)
        self.cbFont_size.config(values=fontSizeList)
        self.cbFont_size.current(4)

        self.cbFont.bind('<<ComboboxSelected>>', self.parent.getFont)
        self.cbFont_size.bind('<<ComboboxSelected>>', self.parent.getFont_size)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)
        self.status_bar = StatusBar(self)

        # creating widgets
        self.main_menu = MainMenu(self)
        self.toolbar = Toolbar(self)
        self.text_editor = TextEditor(self)

        # parent Menu construction
        self.parent.config(menu=self.main_menu)

        # Setting focus
        self.text_editor.focus()
        self.text_editor.config(font='arial 12')
        self.text_editor.bind('<<Modified>>', self.changed)

    def getFont(self, *args):
        global fontFamily
        fontFamily = self.toolbar.cbFont.get()
        self.text_editor.config(font=(fontFamily, fontSize))

    def getFont_size(self, *args):
        global fontSize
        fontSize = self.toolbar.cbFont_size.get()
        self.text_editor.config(font=(fontFamily, fontSize))

    def change_bold(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])

        if text_pro.actual('weight') == 'normal':
            self.text_editor.config(font=(fontFamily, fontSize, 'bold'))
        elif text_pro.actual('weight') == 'bold':
            self.text_editor.config(font=(fontFamily, fontSize, 'normal'))

    def change_italic(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])

        if text_pro.actual('slant') == 'roman':
            self.text_editor.config(font=(fontFamily, fontSize, 'italic'))
        elif text_pro.actual('slant') == 'italic':
            self.text_editor.config(font=(fontFamily, fontSize, 'roman'))

    def change_underline(self, *args):
        text_pro = font.Font(font=self.text_editor['font'])

        if text_pro.actual('underline') == 0:
            self.text_editor.config(font=(fontFamily, fontSize, 'underline'))

        elif text_pro.actual('underline') == 1:

            self.text_editor.config(font=(fontFamily, fontSize, 'normal'))

    def changeFontColor(self, *agrs):
        color = colorchooser.askcolor()
        self.text_editor.config(fg=color[1])

    def align_left(self):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config(LEFT, justify=LEFT)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, LEFT)

    def align_center(self):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config(CENTER, justify=CENTER)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, 'center')

    def align_right(self, *args):
        content = self.text_editor.get(1.0, END)
        self.text_editor.tag_config(RIGHT, justify=RIGHT)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(INSERT, content, 'right')

    def changed(self, *args):
        global textChanged
        flag = self.text_editor.edit_modified()
        textChanged = True
        # print(flag)
        if flag:
            word = len(self.text_editor.get(1.0, 'end-1c').split())
            letter = len(self.text_editor.get(1.0, 'end-1c'))
            self.status_bar.config(text="Characters: " + str(letter) + " Words: " + str(word))
        self.text_editor.edit_modified(False)

    def newFile(self, *args):
        global url
        try:
            url = ""
            self.text_editor.delete(1.0, END)
        except:
            pass

    def openFile(self, *args):
        global url
        url = filedialog.askopenfilename(initialdir="/", title="Select a file to open",
                                         filetype=(("Text file", "*.txt"), ("All Files", "*.*")))

        try:
            with open(url, 'r') as file:
                self.text_editor.delete(1.0, END)
                self.text_editor.insert('1.0', file.read())

        except:
            return

        self.parent.title("NotePad - Now Editing " + str(url.split('/')[-1]))

    def saveFile(self, *args):
        global url
        try:
            if url != "":
                content = str(self.text_editor.get(1.0, END))
                with open(url, 'w', encoding='utf-8') as file:
                    file.write(content)
            else:
                url = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                               filetype=(("Txt file", '*.txt'), ("All files", "*.*")))
                content2 = str(self.text_editor.get(1.0, END))
                url.write(content2)
                url.close()
        except:
            return

    def save_as_File(self, *args):
        try:
            content = str(self.text_editor.get(1.0, END))
            url = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                           filetype=(("Txt file", '*.txt'), ("All files", "*.*")))
            url.write(content)
            url.close()
            self.parent.title("NotePad - Now Editing " + str(url.split('/')[-1]))
        except:
            return

    def exit(self):
        global url
        global textChanged

        try:
            if textChanged:
                m_box = messagebox.askyesnocancel("Warning", "Do you want to save the file")
                if m_box:
                    if url != "":
                        content = self.text_editor.get(1.0, END)
                        with open(url, 'w', encoding='utf-8') as file:
                            file.write(content)
                            self.parent.destroy()
                    else:
                        content2 = str(self.text_editor.get(1.0, END))
                        url = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                                       filetype=(("Txt file", '*.txt'), ("All files", "*.*")))
                        url.write(content2)
                        url.close()
                    if m_box is False:
                        self.parent.destroy()
                else:
                    self.parent.destroy()

        except:
            return

    def about_Message(self, *args):
        messagebox.showinfo("About",
                            "This is our about page\nHave a question, contact us at sachitbansal2006@gmail.com")

    def find(self, *args):
        self.find = FindDialog(parent=self)

    def findwords(self, *args):
        words = self.find.findInput.get()
        self.text_editor.tag_remove("match", 1.0, END)
        matches = 0
        if words:
            start_pos = "1.0"
            while True:
                start_pos = self.text_editor.search(words, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(words))
                self.text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.text_editor.tag_config('match', foreground='#ff1a1a', background='#ffff1a')

    def replacewords(self, *args):
        replaceText = self.find.replaceInput.get()
        word = self.find.findInput.get()
        content = self.text_editor.get(1.0, END)
        newValue = content.replace(word, replaceText)
        self.text_editor.delete(1.0, END)
        self.text_editor.insert(1.0, newValue)

    def hidetoolbar(self, *args):
        global showToolbar
        if showToolbar:
            self.toolbar.pack_forget()
            showToolbar = False
        else:
            self.text_editor.pack_forget()
            self.status_bar.pack_forget()
            self.toolbar.pack(side=TOP, fill=X)
            self.text_editor.pack(expand=YES, fill=BOTH)
            self.status_bar.pack(side=BOTTOM)
            showToolbar = False

    def hideStatusbar(self, *args):
        global show_Status_bar
        if show_Status_bar:
            self.status_bar.pack_forget()
            show_Status_bar = False
        else:
            self.status_bar.pack()
            show_Status_bar = True


if __name__ == "__main__":
    root = Tk()
    root.title("Text Editor")
    MainApplication(root).pack(side=TOP, fill=BOTH, expand=YES)
    root.geometry("1250x650+10+10")
    root.mainloop()
