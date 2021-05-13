import cv2

from connections import makeConnections, checkNumber, checkEmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import datetime


class viewEmploy:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Employ")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        Label(self.root, text="View Employ", font=('arial', 28, 'bold')).pack(pady=20)
        main = Frame(self.root)
        main.pack(pady=20)
        search = Label(main, text='Search by  Employ Name')
        self.en_search = Entry(main)
        search.grid(row=0, column=0)
        self.en_search.grid(row=0, column=1)
        btnSearch = Button(main, text='Search', command=self.showemployData)
        btnSearch.grid(row=0, column=2)

        columns = ('id', 'name', 'dob', 'catName', 'photo', 'email', 'mobile', 'remarks' )
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        self.tree.bind("<Double-1>", self.onDoubleClick)

        footer= Frame(self.root)
        footer.pack(pady=30)

        btnEdit = Button(footer, text='Edit', command=self.btnEdit)
        btnEdit.grid(row=0,column=0)

        dutyRoaster = Button(footer, text="Duty Roaster", command=self.btnDutyRoaster)
        dutyRoaster.grid(row=0,column=1)

        self.showemployData()

        self.root.mainloop()

    def btnDutyRoaster(self):
        currentItem = self.tree.item(self.tree.focus())['values']
        if not (currentItem == ''):
            self.rost = Toplevel()

            self.rost.title("Edit Employ")
            self.rost.geometry("{0}x{0}+0+0".format(self.rost.winfo_screenwidth(), self.rost.winfo_screenheight()))
            Label(self.rost, text="Edit Employ", font=('arial', 28, 'bold')).pack(pady=20)
            main = Frame(self.rost)
            main.pack()

            self.Epmloyid = Label(main, text='Epmloyid')
            self.en_Epmloyid = Entry(main)
            self.en_Epmloyid.insert(0, currentItem[0])
            self.en_Epmloyid.config(state='readonly')

            self.Epmloyid.grid(row=0, column=0)
            self.en_Epmloyid.grid(row=0, column=1)

            # =================================Start Duty===============================================
            startdutyDateFramelb= Label(main, text= 'Start Duty Date')
            startdutyDateFrame = Frame(main)
            startdutyDateFramelb.grid(row=1, column=0)
            startdutyDateFrame.grid(row=1, column=1)

            startDutyDate_day = Label(startdutyDateFrame, text='Day')
            startDutyDate_day.grid(row=0, column=0)
            self.startDutyDate_en_day = Spinbox(startdutyDateFrame, from_=1, to=31)
            self.startDutyDate_en_day.grid(row=1, column=0)

            startDutyDate_month = Label(startdutyDateFrame, text='month')
            startDutyDate_month.grid(row=0, column=1)
            self.startDutyDate_en_month = Spinbox(startdutyDateFrame, from_=1, to=12)
            self.startDutyDate_en_month.grid(row=1, column=1)

            startDutyDate_year = Label(startdutyDateFrame, text='year')
            startDutyDate_year.grid(row=0, column=2)
            self.startDutyDate_en_year = Spinbox(startdutyDateFrame, from_=2021, to=2050)
            self.startDutyDate_en_year.grid(row=1, column=2)

            # ==========================End duty====================================================
            enddutyDateFramelb = Label(main, text='End duty Date ')
            enddutyDateFrame = Frame(main)
            enddutyDateFramelb.grid(row=2, column=0)
            enddutyDateFrame.grid(row=2, column=1)

            endDutyDate_day = Label(enddutyDateFrame, text='Day')
            endDutyDate_day.grid(row=0, column=0)
            self.endDutyDate_en_day = Spinbox(enddutyDateFrame, from_=1, to=31)
            self.endDutyDate_en_day.grid(row=1, column=0)

            endDutyDate_month = Label(enddutyDateFrame, text='month')
            endDutyDate_month.grid(row=0, column=1)
            self.endDutyDate_en_month = Spinbox(enddutyDateFrame, from_=1, to=12)
            self.endDutyDate_en_month.grid(row=1, column=1)

            endDutyDate_year = Label(enddutyDateFrame, text='year')
            endDutyDate_year.grid(row=0, column=2)
            self.endDutyDate_en_year = Spinbox(enddutyDateFrame, from_=2021, to=2050)
            self.endDutyDate_en_year.grid(row=1, column=2)

            # ================================Start time=============================
            start_time = Label(main, text='Start Time')
            start_timeFrame = Frame(main)
            start_time.grid(row=3, column=0)
            start_timeFrame.grid(row=3, column=1)

            start_time_Hour = Label(start_timeFrame, text='Hour')
            start_time_Hour.grid(row=0, column=0)
            self.start_time_en_Hour = Spinbox(start_timeFrame, from_=1, to=12)
            self.start_time_en_Hour.grid(row=1, column=0)

            start_time_Min = Label(start_timeFrame, text='Min')
            start_time_Min.grid(row=0, column=1)
            self.start_time_en_Min = Spinbox(start_timeFrame, from_=0, to=60)
            self.start_time_en_Min.grid(row=1, column=1)

            start_time_sec = Label(start_timeFrame, text='sec')
            start_time_sec.grid(row=0, column=2)
            self.start_time_en_sec = Spinbox(start_timeFrame, from_=0, to=60)
            self.start_time_en_sec.grid(row=1, column=2)

            #======================================= End Time====================================
            End_time = Label(main, text='End Time')
            End_timeFrame = Frame(main)
            End_time.grid(row=4, column=0)
            End_timeFrame.grid(row=4, column=1)

            End_time_Hour = Label(End_timeFrame, text='Hour')
            End_time_Hour.grid(row=0, column=0)
            self.End_time_en_Hour = Spinbox(End_timeFrame, from_=1, to=24)
            self.End_time_en_Hour.grid(row=1, column=0)

            End_time_Min = Label(End_timeFrame, text='Min')
            End_time_Min.grid(row=0, column=1)
            self.End_time_en_Min = Spinbox(End_timeFrame, from_=0, to=60)
            self.End_time_en_Min.grid(row=1, column=1)

            End_time_sec = Label(End_timeFrame, text='sec')
            End_time_sec.grid(row=0, column=2)
            self.End_time_en_sec = Spinbox(End_timeFrame, from_=0, to=60)
            self.End_time_en_sec.grid(row=1, column=2)


            btnRostSubmit = Button(main, text='Submit', command= self.btnRostSubmit)
            btnRostSubmit.grid(row=5,column=1)

            self.rost.mainloop()
        else:
            messagebox.showinfo('','Select one Row in Table?')


    def btnRostSubmit(self):
        en_Epmloyid = self.en_Epmloyid.get()
        startDutyDate = f"{self.startDutyDate_en_day.get()}-{self.startDutyDate_en_month.get()}-{self.startDutyDate_en_year.get()}"
        endDutyDate = f"{self.endDutyDate_en_day.get()}-{self.endDutyDate_en_month.get()}-{self.endDutyDate_en_year.get()}"
        start_time = f"{self.start_time_en_Hour.get()}:{self.start_time_en_Min.get()}:{self.start_time_en_sec.get()}"
        end_time = f"{self.End_time_en_Hour.get()}:{self.End_time_en_Min.get()}:{self.End_time_en_sec.get()}"
        date1 = datetime.datetime.strptime('1-5-2021', '%d-%m-%Y')
        date2 = datetime.datetime.strptime('1-10-2021', '%d-%m-%Y')
        mydates = pd.date_range(date1, date2).tolist()
        conn = makeConnections()
        cr = conn.cursor()
        for i in mydates:
            query= f"INSERT INTO `dutyRoaster`(`dutyDate`, `startTime`, `EndTime`, `employID`) VALUES ('{i}','{start_time}','{end_time}','{en_Epmloyid}')"
            cr.execute(query)
            conn.commit()

        messagebox.showinfo("",'Success Fully Added Duty Time')
        self.rost.destroy()


    def showemployData(self):
        search = self.en_search.get()
        if search == '':
            query = "SELECT * FROM `employ`"
        else:
            query = "SELECT * FROM `employ` where name LIKE '%{}%'".format(search)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)


    def onDoubleClick(self,event):
        currentItem = self.tree.item(self.tree.focus())['values']
        ans = messagebox.askquestion('', 'Are you sure to delete')
        if ans == 'yes':
            query = "DELETE FROM `employ` WHERE id='{}'".format(currentItem[0])
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            conn.commit()
            self.showemployData()
            messagebox.showinfo("", 'Deleted {} is  successfully!!!'.format(currentItem[0]))

    def btnEdit(self):
        self.filename = []
        self.win = Toplevel()
        self.win.title("Edit Employ")
        self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))

        Label(self.win, text="Edit Employ", font=('arial', 28, 'bold', 'underline')).pack()

        body = Frame(self.win)
        body.pack()

        self.name = Label(body, text='Name', font=("times new roman", 12))
        self.en_name = Entry(body)
        self.name.pack()
        self.en_name.pack()

        self.Lbdob = Label(body, text='Date of Birth', font=("times new roman", 12))
        dob = Frame(body)
        self.Lbdob.pack()
        dob.pack()

        day = Label(dob, text='Day')
        day.grid(row=0, column=0)
        self.day = Spinbox(dob, from_=1, to=31)
        self.day.grid(row=1, column=0)

        day = Label(dob, text='month')
        day.grid(row=0, column=1)
        self.month = Spinbox(dob, from_=1, to=12)
        self.month.grid(row=1, column=1)

        day = Label(dob, text='year')
        day.grid(row=0, column=2)
        self.year = Spinbox(dob, from_=1950, to=2050)
        self.year.grid(row=1, column=2)

        query = "select name from category"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()
        catList = []
        for row in result:
            catList.append(row[0])

        self.catname = Label(body, text="Category Name", font=("times new roman", 12))
        self.en_catname = ttk.Combobox(body, values=catList, state='readonly')
        self.catname.pack()
        self.en_catname.pack()

        self.Email = Label(body, text='Email', font=("times new roman", 12))
        self.en_Email = Entry(body)
        self.Email.pack()
        self.en_Email.pack()

        self.Mobile = Label(body, text='Mobile', font=("times new roman", 12))
        self.en_Mobile = Entry(body)
        self.Mobile.pack()
        self.en_Mobile.pack()

        self.Remark = Label(body, text='Remark', font=("times new roman", 12))
        self.en_Remark = Entry(body)
        self.Remark.pack()
        self.en_Remark.pack()

        self.file = Label(body, text='choose File', font=("times new roman", 12))
        self.file_button = Button(body, text="choose File(.png)", command=self.chooseFile)
        self.file.pack()
        self.file_button.pack()

        btn = Button(body, text="Submit", command=self.btnUpdate)
        btn.pack()

        self.root.mainloop()

    def btnUpdate(self):
        pass


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
    viewEmploy()