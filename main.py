from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from addAdmin import AddAdmin
from viewCategory import viewCategory
from addCategory import AddCategory
from addEmploy import AddEmploy
from viewEmploy import viewEmploy
from viewRost import Rost
from viewAttendanceByNameOrID import viewAttendaceByNameOrId
import datetime
import sys
from PIL import ImageTk,Image
class main:
    def btnexit(self):
        sys.exit()
        exit()

    def CallAddAdmin(self,event):
        AddAdmin()


    def __init__(self):
        # self.root = tk.ThemedTk(theme="scidmint")
        self.root = Tk()
        self.root.title("Attendance System")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.config(background='white')

        menubar = Menu(self.root)

        fileMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='File', menu=fileMenu)

        fileMenu.add_command(label='Admin', command=AddAdmin)
        # fileMenu.add_command(label='Change Password')
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit',command=self.btnexit)

        # shortcut key

        self.root.bind('<F1>', self.CallAddAdmin)


        #-----------------------------------------------------

        categoryMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Category', menu=categoryMenu)
        categoryMenu.add_command(label='Add Category', command=AddCategory )
        categoryMenu.add_command(label='View Category', command=viewCategory)

        employMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Employ', menu=employMenu)
        employMenu.add_command(label='Add Employ', command=AddEmploy)
        employMenu.add_command(label='View Employ', command=viewEmploy)

        dutyRostMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Duty Rost', menu=dutyRostMenu)
        dutyRostMenu.add_command(label='Add Duty Rost', command=viewEmploy)
        dutyRostMenu.add_command(label='View Duty Rost', command=Rost)
        self.root.config(menu=menubar)

        viewAttendanceEmploy = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Attendence', menu=viewAttendanceEmploy)
        viewAttendanceEmploy.add_command(label='Attendacne employ by Name', command=viewAttendaceByNameOrId)
        # viewAttendanceEmploy.add_command(label='View Duty Rost', command=Rost)
        self.root.config(menu=menubar)

        Label(self.root, text="Attendance System", font=('arial',24,'bold', 'underline'),background='white').pack(pady=50)

        body = Frame(self.root)
        body.pack()

        leftFrame = Frame(body)
        leftFrame.pack(side=LEFT)

        RightFrame = Frame(body)
        RightFrame.pack(side=RIGHT)
        #-----------clock----------------------------------------------------------
        clock = Label(RightFrame, font=('times', 20, 'bold'), bg='snow')
        date1 = Label(RightFrame, font=('times', 15, 'bold'), bg='snow')
        clock.pack(fill=BOTH, expand=1)
        date1.pack(fill=BOTH, expand=1)
        def tick():
            now = datetime.datetime.now()
            time2 =  str(now.strftime("%I:%M:%S %p"))
            time3 = str(now.strftime("%A,%d-%b-%y"))
            clock.config(text=time2)
            date1.config(text=time3)
            clock.after(200, tick)
        tick()

        # Images
        # image

        path = "./images/download.jpeg"
        img = ImageTk.PhotoImage(Image.open(path))
        lb1 = Label(RightFrame, image=img,bg='snow')
        lb1.pack(padx=150,pady=20)






        self.root.mainloop()




if __name__ == '__main__':
    main()
