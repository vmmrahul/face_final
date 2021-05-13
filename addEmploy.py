import cv2

from connections import makeConnections, checkNumber, checkEmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime


class AddEmploy:
    def __init__(self):
        BACKGROUND_COLOR = '#e6ffff'
        PY = 5
        PX = 10
        EN_WIDTH = 50
        SPIN = 15
        FONT = ('arial', 15)
        BTN_BACKGORUN = '#061a00'
        BTN_FORGROUND = 'white'

        self.filename =[]
        self.root = Tk()
        self.root.title("Add Employ")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.config(bg=BACKGROUND_COLOR)
        Label(self.root, text="Add Employ", font=('arial', 28, 'bold', 'underline'), bg=BACKGROUND_COLOR).pack()

        body = Frame(self.root, bg=BACKGROUND_COLOR)
        body.pack(pady=60)

        self.name = Label(body, text='Name', font=FONT, bg=BACKGROUND_COLOR)
        self.en_name = Entry(body, relief=SUNKEN,borderwidth=3, width=EN_WIDTH)
        self.name.pack()
        self.en_name.pack(pady=PY)

        self.Lbdob = Label(body, text='Date of Birth', font=FONT, bg=BACKGROUND_COLOR)
        dob = Frame(body, bg=BACKGROUND_COLOR)
        self.Lbdob.pack()
        dob.pack(pady=PY)

        day = Label(dob, text='Day', bg=BACKGROUND_COLOR)
        day.grid(row=0, column=0)
        self.day = Spinbox(dob, from_=1, to=31, width=SPIN)
        self.day.grid(row=1, column=0)

        day = Label(dob, text='month', bg=BACKGROUND_COLOR)
        day.grid(row=0, column=1)
        self.month = Spinbox(dob, from_=1, to=12, width=SPIN)
        self.month.grid(row=1, column=1)

        day = Label(dob, text='year', bg=BACKGROUND_COLOR)
        day.grid(row=0, column=2)
        self.year = Spinbox(dob, from_=1950, to=2050, width=SPIN)
        self.year.grid(row=1, column=2)

        query = "select name from category"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()
        catList = []
        for row in result:
            catList.append(row[0])

        self.catname = Label(body, text="Category Name", font=FONT, bg=BACKGROUND_COLOR)
        self.en_catname = ttk.Combobox(body, values=catList, state='readonly', width=EN_WIDTH)
        self.catname.pack(pady=PY)
        self.en_catname.pack(pady=PY)

        self.Email = Label(body, text='Email', font=FONT, bg=BACKGROUND_COLOR)
        self.en_Email = Entry(body, width=EN_WIDTH)
        self.Email.pack(pady=PY)
        self.en_Email.pack(pady=PY)

        self.Mobile = Label(body, text='Mobile', font=FONT, bg=BACKGROUND_COLOR)
        self.en_Mobile = Entry(body, width=EN_WIDTH)
        self.Mobile.pack(pady=PY)
        self.en_Mobile.pack(pady=PY)

        self.Remark = Label(body, text='Remark', font=FONT, bg=BACKGROUND_COLOR)
        self.en_Remark = Entry(body, width=EN_WIDTH)
        self.Remark.pack(pady=PY)
        self.en_Remark.pack(pady=PY)

        self.file = Label(body, text='choose File', font=FONT, bg=BACKGROUND_COLOR)
        self.file_button = Button(body, text="choose File(.png)", command=self.chooseFile)
        self.file.pack()
        self.file_button.pack(pady=PY)

        btn = Button(body, text="Submit", command=self.btnSubmit)
        btn.pack()

        self.root.mainloop()

    def btnSubmit(self):
        fileName = self.filename
        name = self.en_name.get()
        catname = self.en_catname.get()
        email = self.en_Email.get()
        mobile = self.en_Mobile.get()
        Remark = self.en_Remark.get()
        dob = f"{self.year.get()}-{self.month.get()}-{self.day.get()}"
        dob = datetime.strptime(dob, '%Y-%m-%d')
        if name =='' or catname=='' or mobile=='' or email=='':
            messagebox.showinfo("","All Fields Are Required !!")
        else:
            if len(self.filename) != 0:
                if checkNumber(mobile):
                    if checkEmail(email):
                        query = f"INSERT INTO `employ`(`name`, `dob`, `catName`, `email`, `mobile`, `remarks`) VALUES ('{name}','{dob}','{catname}','{email}','{mobile}','{Remark}')"
                        conn = makeConnections()
                        cr = conn.cursor()
                        cr.execute(query)
                        conn.commit()
                        id = cr.lastrowid

                        print(fileName)
                        path = f'Images/{str(id)}.png'
                        cv2.imwrite(path, self.img)
                        query = "UPDATE `employ` SET `photo`='{}' WHERE id ='{}'".format(path, id)
                        cr.execute(query)
                        conn.commit()
                        messagebox.showinfo("Success", 'Added Employ ')
                    else:
                        messagebox.showinfo("", "Invalid Email!!")
                else:
                    messagebox.showinfo("", "Invalid Mobile Number!!")
            else:
                messagebox.showinfo("info", "Image is Not Selected")

    def chooseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(('jpg', '*.jpg'), ("png", "*.png"), ('jpeg', '*.jpeg')))
        if len(self.filename) != 0:
            self.img = cv2.imread(self.filename)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.file_button.config(text=self.filename)
        else:
            messagebox.showinfo("info", "Image is Not Selected")


if __name__ == '__main__':
    obj = AddEmploy()
