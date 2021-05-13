import cv2
from connections import makeConnections, checkNumber, checkEmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import datetime

class Rost:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Employ")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        Label(self.root, text="View Employ", font=('arial', 28, 'bold')).pack(pady=20)
        main = Frame(self.root)
        main.pack(pady=10)

        search = Label(main, text='Search by Employ id')
        self.en_search = Entry(main)
        search.grid(row=0, column=0)
        self.en_search.grid(row=0, column=1)
        btnSearch = Button(main, text='Search', command=self.showemployData)
        btnSearch.grid(row=0,column=2)

        columns = ('Employ id', 'name', 'dutyRoaster id', 'Duty Date', 'start Time', 'End Time')
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

        footer = Frame(self.root)
        footer.pack()

        self.showemployData()

        self.root.mainloop()

    def onDoubleClick(self,event):
        currentItem = self.tree.item(self.tree.focus())['values']
        ans = messagebox.askquestion('', 'Are you sure to delete')
        if ans == 'yes':
            query = "DELETE FROM `dutyRoaster` WHERE `id`='{}'".format(currentItem[2])
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            conn.commit()
            self.showemployData()
            messagebox.showinfo("", 'Deleted {} is  successfully!!!'.format(currentItem[0]))

    def showemployData(self):
        search = self.en_search.get()
        if search =='':
            query = "select employ.id ,employ.name, dutyRoaster.id, dutyRoaster.dutyDate, dutyRoaster.startTime, dutyRoaster.EndTime from `dutyRoaster` INNER JOIN employ on employ.id = dutyRoaster.employID"
        else:
            query = "select employ.id ,employ.name, dutyRoaster.id, dutyRoaster.dutyDate, dutyRoaster.startTime, dutyRoaster.EndTime from `dutyRoaster` INNER JOIN employ on employ.id = dutyRoaster.employID where dutyRoaster.employID = '{}'".format(search)
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()
        if len(result)>0:
            for k in self.tree.get_children():
                self.tree.delete(k)
            for i in range(0, len(result)):
                self.tree.insert("", value=result[i], index=i)
        else:
            messagebox.showinfo('','No Data Found')


if __name__ == '__main__':
    Rost()