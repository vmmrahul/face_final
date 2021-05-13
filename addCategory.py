from connections import makeConnections
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class AddCategory:
    def __init__(self):
        BACKGROUND_COLOR = '#e6ffff'
        PY = 10
        PX = 10
        EN_WIDTH = 50
        FONT = ('arial',15)
        BTN_BACKGORUN = '#061a00'
        BTN_FORGROUND = 'white'

        self.root= Tk()
        self.root.title("Add Category")
        self.root.config(bg=BACKGROUND_COLOR)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        Label(self.root, text="Add Category", font=('arial', 28, 'bold'),bg=BACKGROUND_COLOR).pack(pady=20)
        main = Frame(self.root, bg=BACKGROUND_COLOR)
        main.pack()



        self.name = Label(main, text='Name', bg=BACKGROUND_COLOR, font=FONT)
        self.en_name = Entry(main, width=EN_WIDTH, font=FONT)
        self.name.grid(row=0, column=0, pady=PY,padx=PX)
        self.en_name.grid(row=0, column=1, pady=PY,padx=PX)

        self.description = Label(main, text='description', bg=BACKGROUND_COLOR, font=FONT)
        self.en_description = Entry(main, width=EN_WIDTH, font=FONT)
        self.description.grid(row=1, column=0, pady=PY,padx=PX)
        self.en_description.grid(row=1, column=1, pady=PY,padx=PX)

        self.salary = Label(main, text='salary', bg=BACKGROUND_COLOR, font=FONT)
        self.en_salary = Entry(main, width=EN_WIDTH, font=FONT)
        self.salary.grid(row=2, column=0, pady=PY,padx=PX)
        self.en_salary.grid(row=2, column=1, pady=PY,padx=PX)

        self.number_of_leave_allowed = Label(main, text='Number of Leave Allowed', bg=BACKGROUND_COLOR, font=FONT)
        self.en_number_of_leave_allowed = Entry(main, width=EN_WIDTH, font=FONT)
        self.number_of_leave_allowed.grid(row=3, column=0, pady=PY,padx=PX)
        self.en_number_of_leave_allowed.grid(row=3, column=1, pady=PY,padx=PX)

        self.deduction_leave = Label(main, text='Deduction leave', bg=BACKGROUND_COLOR, font=FONT)
        self.en_deduction_leave = Entry(main, width=EN_WIDTH, font=FONT)
        self.deduction_leave.grid(row=4, column=0, pady=PY,padx=PX)
        self.en_deduction_leave.grid(row=4, column=1, pady=PY,padx=PX)

        btn = Button(main, text='Submit', command=self.btnSumit, bg=BTN_BACKGORUN, fg=BTN_FORGROUND, width=20,font=FONT)
        btn.grid(row=5,column=1, pady=PY,padx=PX)
        self.root.mainloop()


    def btnSumit(self):
        name= self.en_name.get()
        description= self.en_description.get()
        salary= self.en_salary.get()
        number_of_leave_allowed= self.en_number_of_leave_allowed.get()
        deduction_leave= self.en_deduction_leave.get()
        if not(name=="" or description=='' or salary == '' or number_of_leave_allowed == '' or deduction_leave==''):
            query = "select * from category where name ='{}'".format(name)
            conn = makeConnections()
            cr = conn.cursor()
            cr.execute(query)
            result = cr.fetchall()
            if len(result)>0:
                messagebox.showinfo("","allready in Added.")
            else:
                query = f"INSERT INTO `category`(`name`, `description`, `salary`, `number_of_leave_allowed`, `deduction_leave`) VALUES ('{name}','{description}','{salary}','{number_of_leave_allowed}','{deduction_leave}')"
                cr.execute(query)
                conn.commit()
                messagebox.showinfo('',"Added SuccessFully!! {}".format(name))
        else:
            messagebox.showinfo("","All Fields Are required!!")





if __name__ == '__main__':
    AddCategory()