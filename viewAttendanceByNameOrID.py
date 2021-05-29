from connections import makeConnections, checkNumber, checkEmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import datetime


class viewAttendaceByNameOrId:
    def __init__(self):
        self.root = Tk()
        self.root.title("View Attendacne")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        Label(self.root, text="View Attendance", font=('arial', 28, 'bold')).pack(pady=20)
        main = Frame(self.root)
        main.pack(pady=20)
        search = Label(main, text='Search by  Employ Name')
        self.en_search = Entry(main)
        search.grid(row=0, column=0)
        self.en_search.grid(row=0, column=1)
        btnSearch = Button(main, text='Search', command =self.btnViewAttend)
        btnSearch.grid(row=0, column=2)

        columns = ('id', 'name', 'employ', 'dateOfAttendace', 'Entry', 'Exit')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        self.tree.bind("<Double-1>", self.showDutryRost)

        footer = Frame(self.root)
        footer.pack(pady=30)

        self.btnViewAttend()

        self.root.mainloop()

    def btnViewAttend(self):
        search =self.en_search.get()
        if search !='':
            query = f"SELECT Attendance.id, employ.name ,Attendance.employ, Attendance.dateOfAttendace, min(Attendance.timeOfRigister), max(Attendance.timeOfRigister) FROM `Attendance` INNER JOIN employ on employ.id=Attendance.employ where employ.id = '{search}' or employ.name LIKE '%{search}%' GROUP by Attendance.employ , Attendance.dateOfAttendace"
        else:
            query = "SELECT Attendance.id, employ.name ,Attendance.employ, Attendance.dateOfAttendace, min(Attendance.timeOfRigister), max(Attendance.timeOfRigister) FROM `Attendance` INNER JOIN employ on employ.id=Attendance.employ GROUP by Attendance.employ , Attendance.dateOfAttendace"

        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()
        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)

    def showDutryRost(self,event):
        currentItem = self.tree.item(self.tree.focus())['values']
        if not (currentItem == ''):
            query = f"SELECT * FROM `dutyRoaster` WHERE `dutyDate`='{currentItem[3]}' and `employID`='{currentItem[2]}'"
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            result = cr.fetchone()

            print(result)
            if result!=None:

                self.win = Toplevel()

                self.win.title("Employ Detail")
                self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))
                Label(self.win, text="Detail Time", font=('arial', 28, 'bold')).pack(pady=20)


                body = Frame(self.win)
                body.pack()

                Label(body, text=f"ID: {currentItem[2]}", padx= 20).grid(row=0, column=0)
                Label(body, text=f"Name: {currentItem[1]}", padx= 20).grid(row=0, column=1)
                Label(body, text=f"Date: {currentItem[3]}", padx= 20).grid(row=0, column=2)

                #
                Label(body, text=f"Actual Time of Entry And Exit", padx= 20, pady=20,font=('arial',18,'bold')).grid(row=1, column=0)

                Label(body, text=f"Entry Time: {str(result[2])}", padx= 20 ).grid(row=2, column=0)
                Label(body, text=f"Exit Time: {str(result[3])}", padx= 20 ).grid(row=2, column=1)

                #
                Label(body, text=f"Time He/She Entry And Exit", padx= 20, pady=20,font=('arial',18,'bold')).grid(row=3, column=0)

                Label(body, text=f"Entry Time: {str(currentItem[4])}", padx= 20 ).grid(row=4, column=0)
                Label(body, text=f"Exit Time: {str(currentItem[5])}", padx= 20 ).grid(row=4, column=1)




                self.win.mainloop()
            else:
                messagebox.showinfo("","No assign Time Entery and exit to this user!!!!")
        else:
            messagebox.showinfo('','Select 1 row in Table')


if __name__ == '__main__':
    viewAttendaceByNameOrId()
