
from connections import makeConnections, checkNumber, checkEmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import datetime



class viewAttendace:
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
        btnSearch = Button(main, text='Search')
        btnSearch.grid(row=0, column=2)

        columns = ('id', 'name', 'date', 'time')
        self.tree = ttk.Treeview(self.root, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        # self.tree.bind("<Double-1>", self.onDoubleClick)

        footer= Frame(self.root)
        footer.pack(pady=30)

        self.root.mainloop()


    def btnViewAttend(self):
        query ="SELECT * FROM `Attendance`"

if __name__ == '__main__':
    viewAttendace()