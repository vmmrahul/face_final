from connections import makeConnections
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class viewCategory:
    def __init__(self):
        self.root = Tk()
        self.root.title("Add Category")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        Label(self.root, text="View Category", font=('arial', 28, 'bold')).pack(pady=20)
        main = Frame(self.root)
        main.pack()

        columns = ("Name", "description", 'salary', 'Number of Leave Allowed', 'Deduction leave')
        self.tree = ttk.Treeview(main, selectmode='browse',
                                 column=columns)
        vsb = ttk.Scrollbar(main, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        for row in columns:
            self.tree.heading(row, text=row)

        self.tree.pack(side="top", fill="both", expand=1)
        self.tree.column('#0', stretch=False, minwidth=0, width=0)

        self.tree.bind("<Double-1>", self.onDoubleClick)

        btnEdit = Button(self.root, text='Edit', command=self.btnEdit)
        btnEdit.pack()

        self.showCategoryData()

        self.root.mainloop()

    def btnEdit(self):
        currentItem = self.tree.item(self.tree.focus())['values']
        print(currentItem)
        if not (currentItem == ''):
            self.win = Toplevel()
            self.win.title("Edit Category")
            self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))
            Label(self.win, text="Edit Category", font=('arial', 28, 'bold')).pack(pady=20)
            main = Frame(self.win)
            main.pack()

            self.name = Label(main, text='Name')
            self.en_name = Entry(main)
            self.en_name.insert(0, currentItem[0])
            self.en_name.config(state='readonly')

            self.name.grid(row=0, column=0)
            self.en_name.grid(row=0, column=1)

            self.description = Label(main, text='description')
            self.en_description = Entry(main)
            self.en_description.insert(0, currentItem[1])
            self.description.grid(row=1, column=0)
            self.en_description.grid(row=1, column=1)

            self.salary = Label(main, text='salary')
            self.en_salary = Entry(main)
            self.en_salary.insert(0, currentItem[2])
            self.salary.grid(row=2, column=0)
            self.en_salary.grid(row=2, column=1)

            self.number_of_leave_allowed = Label(main, text='Number of Leave Allowed')
            self.en_number_of_leave_allowed = Entry(main)
            self.en_number_of_leave_allowed.insert(0, currentItem[3])
            self.number_of_leave_allowed.grid(row=3, column=0)
            self.en_number_of_leave_allowed.grid(row=3, column=1)

            self.deduction_leave = Label(main, text='Deduction leave')
            self.en_deduction_leave = Entry(main)
            self.en_deduction_leave.insert(0, currentItem[4])
            self.deduction_leave.grid(row=4, column=0)
            self.en_deduction_leave.grid(row=4, column=1)

            btn = Button(main, text='Submit', command=self.btnUpdate)
            btn.grid(row=5, column=1)
            self.win.mainloop()
        else:
            messagebox.showinfo("", "select one Category from Table")

    def btnUpdate(self):
        name = self.en_name.get()
        description = self.en_description.get()
        salary = self.en_salary.get()
        number_of_leave_allowed = self.en_number_of_leave_allowed.get()
        deduction_leave = self.en_deduction_leave.get()
        if not (
                name == "" or description == '' or salary == '' or number_of_leave_allowed == '' or deduction_leave == ''):
            conn = makeConnections()
            cr = conn.cursor()
            query = f"UPDATE `category` SET `description`='{description}',`salary`='{salary}',`number_of_leave_allowed`='{number_of_leave_allowed}',`deduction_leave`='{deduction_leave}' WHERE `name`='{name}'"
            cr.execute(query)
            conn.commit()
            messagebox.showinfo('', "Update SuccessFully!! {}".format(name))
            self.showCategoryData()
            self.win.destroy()
        else:
            messagebox.showinfo("", "All Fields Are required!!")

    def onDoubleClick(self, event):
        currentItem = self.tree.item(self.tree.focus())['values']
        ans = messagebox.askquestion('', 'Are you sure to delete')
        print(ans)
        if ans == 'yes':
            query = "DELETE FROM `category` WHERE name='{}'".format(currentItem[0])
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            conn.commit()
            self.showCategoryData()
            messagebox.showinfo("", 'Deleted {} is  successfully!!!'.format(currentItem[0]))

    def showCategoryData(self):
        query = "SELECT `name`, `description`, `salary`, `number_of_leave_allowed`, `deduction_leave` FROM `category`"
        conn = makeConnections()
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchall()

        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(result)):
            self.tree.insert("", value=result[i], index=i)


if __name__ == '__main__':
    viewCategory()
