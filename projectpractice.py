from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
from tkinter import Listbox
from tkinter import Scrollbar
import mysql.connector
from datetime import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("900x900+0+0")

        self.clock_label = Label(self.root, text="", font=("Arial", 14))
        self.clock_label.pack()
        self.update_clock()

        #=====================================variable==================================================================

        self.member_var=StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdate_var = StringVar()
        self.actualprice_var = StringVar()


        lbltitle = Label(self.root, text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #=================================================DataFrameLeft=========================================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="black", bd=12,
                                   relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", textvariable=self.member_var,
                          font=("arial", 15, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.member_var, width=27,
                                 state="readonly")
        comMember["value"] = ("Admin Staf ", "Student", "Lecturer",)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN No", font=("arial", 15, "bold"),
                          padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)

        lblID_No = Label(DataFrameLeft, bg="powder blue", text="ID No", font=("arial", 15, "bold"),
                         padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.id_var, width=29)
        txtTitle_No.grid(row=2, column=1)

        lblFirst_Name = Label(DataFrameLeft, bg="powder blue", text="First Name", font=("arial", 15, "bold"),
                              padx=2, pady=6)
        lblFirst_Name.grid(row=3, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.firstname_var, width=29)
        txtTitle_No.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("arial", 15, "bold"),
                            padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.lastname_var, width=29)
        txtTitle_No.grid(row=4, column=1)

        lblAddress = Label(DataFrameLeft, bg="powder blue", text="Address", font=("arial", 15, "bold"),
                           padx=2, pady=6)
        lblAddress.grid(row=5, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.address_var, width=29)
        txtTitle_No.grid(row=5, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile", font=("arial", 15, "bold"),
                          padx=2, pady=6)
        lblMobile.grid(row=6, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.mobile_var, width=29)
        txtTitle_No.grid(row=6, column=1)

        lblPost_Code = Label(DataFrameLeft, bg="powder blue", text="Post Code", font=("arial", 15, "bold"),
                             padx=2, pady=6)
        lblPost_Code.grid(row=7, column=0, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.postcode_var, width=29)
        txtTitle_No.grid(row=7, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book Id", font=("arial", 15, "bold"),
                          padx=2, pady=6)
        lblBookId.grid(row=0, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.bookid_var, width=29)
        txtTitle_No.grid(row=0, column=3)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author", font=("arial", 15, "bold"),
                          padx=2, pady=6)
        lblAuthor.grid(row=1, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.author_var, width=29)
        txtTitle_No.grid(row=1, column=3)

        lblDate_Borrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial", 15, "bold"),
                                 padx=2, pady=6)
        lblDate_Borrowed.grid(row=2, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtTitle_No.grid(row=2, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial", 15, "bold"),
                           padx=2, pady=6)
        lblDateDue.grid(row=3, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.datedue_var, width=29)
        txtTitle_No.grid(row=3, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="DaysOnBook", font=("arial", 15, "bold"),
                              padx=4, pady=2)
        lblDaysOnBook.grid(row=4, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.daysonbook_var, width=29)
        txtTitle_No.grid(row=4, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=("arial", 15, "bold"),
                                  padx=2, pady=6)
        lblLateReturnFine.grid(row=5, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.latereturnfine_var, width=29)
        txtTitle_No.grid(row=5, column=3)

        lblDateOverDate = Label(DataFrameLeft, bg="powder blue", text="Date Over Date", font=("arial", 15, "bold"),
                                padx=2, pady=6)
        lblDateOverDate.grid(row=6, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.dateoverdate_var, width=29)
        txtTitle_No.grid(row=6, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("arial", 15, "bold"),
                               padx=2, pady=6)
        lblActualPrice.grid(row=7, column=2, sticky=W)

        txtTitle_No = Entry(DataFrameLeft, font=("arial", 15, "bold"), textvariable=self.actualprice_var, width=29)
        txtTitle_No.grid(row=7, column=3)

        #========================================Data Frame Right========================================================


        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12,
                                   relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.textbox = Text(DataFrameRight, font=("times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.textbox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head Firt Book ','Learn Python Hard Way','Python Programming','Secreate Rahshy','Python Cook Book'
                 ,'Machine Techno','My Python','Machine Python ','Advanced Python','Excel Python','Love Python',
                 'Jungli Python','Python guru','Ai Python','ML Python','java','Advance Java','Excel Java',
                   'Advance Excel Java','Love Java','Machine,Java','Mera Java']

        def SelectBook( event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Head First Book":
                self.bookid_var.set("BO67O9K")
                self.author_var.set("Paul Berry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdate_var.set("No")
                self.actualprice_var.set("Rs.1085")

        listBox=Listbox(DataFrameRight,font=("times new roman", 12, "bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)




        #==============================================Button Frame=====================================================

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=50)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=20,
                            bg="blue"
                            , fg="White")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton, command=self.ShowData, text="Show Data", font=("arial", 12, "bold"), width=20,
                             bg="blue"
                             , fg="White")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(Framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=20,
                           bg="blue"
                           , fg="White")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Framebutton, command=self.delete, text="Delete", font=("arial", 12, "bold"), width=20,
                           bg="blue"
                           , fg="White")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=20, bg="blue"
                          , fg="White")
        btnReset.grid(row=0, column=4)

        btnExit = Button(Framebutton, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=20, bg="blue"
                         , fg="White")
        btnExit.grid(row=0, column=5)

        #========================================Information Frame======================================================

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)


        xscroll = ttk.Scrollbar(FrameDetails, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(FrameDetails, orient=VERTICAL)

        self.libray_table=ttk.Treeview(Table_frame,columns=("Member Type","PRN_No","ID No","First Name","Last Name",
        "Address","Mobile","Post Code","Book Id","Author","Date Borrowed","Date Due","Days On Book","Late Return Fine"
        ,"Date Over Date","Actual Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.libray_table.xview)
        yscroll.config(command=self.libray_table.yview)



        self.libray_table.heading("Member Type",text="Member Type")
        self.libray_table.heading("PRN_No", text="PRN_No")
        self.libray_table.heading("ID No", text="ID No")
        self.libray_table.heading("First Name", text="First Name")
        self.libray_table.heading("Last Name", text="Last Name")
        self.libray_table.heading("Address", text="Address")
        self.libray_table.heading("Mobile", text="Mobile ")
        self.libray_table.heading("Post Code", text="Post Code")
        self.libray_table.heading("Book Id", text="Book Id")
        self.libray_table.heading("Author", text="Author")
        self.libray_table.heading("Date Borrowed", text="DateBorrowed")
        self.libray_table.heading("Date Due", text="Date Due")
        self.libray_table.heading("Days On Book", text="Days On Book")
        self.libray_table.heading("Late Return Fine", text="Late Return Fine")
        self.libray_table.heading("Date Over Date", text="Date Over Date")
        self.libray_table.heading("Actual Price", text="Actual Price")

        self.libray_table["show"]="headings"
        self.libray_table.pack(fill=BOTH,expand=1)



        self.libray_table.column("Member Type", width=100)
        self.libray_table.column("PRN_No", width=100)
        self.libray_table.column("ID No", width=100)
        self.libray_table.column("First Name", width=100)
        self.libray_table.column("Last Name", width=100)
        self.libray_table.column("Address", width=100)
        self.libray_table.column("Mobile", width=100)
        self.libray_table.column("Post Code", width=100)
        self.libray_table.column("Book Id", width=100)
        self.libray_table.column("Author", width=100)
        self.libray_table.column("Date Borrowed", width=100)
        self.libray_table.column("Date Due", width=100)
        self.libray_table.column("Days On Book", width=100)
        self.libray_table.column("Late Return Fine", width=100)
        self.libray_table.column("Date Over Date", width=100)
        self.libray_table.column("Actual Price", width=100)


        self.fatch_data()
        self.libray_table.bind("<ButtonRelease-1>",self.get_cursor)



    def add_data(self):
        conn = mysql.connector.Connect(host="localhost", user="root", password='kunj@ducat', database='india')
        my_cursor = conn.cursor()




        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
                           self.lastname_var.get(), self.address_var.get(), self.postcode_var.get(),
                           self.mobile_var.get(), self.bookid_var.get(), self.author_var.get(), self.dateborrowed_var.get(),
                           self.dateoverdate_var.get(), self.datedue_var.get(), self.daysonbook_var.get(),
                           self.latereturnfine_var.get(), self.actualprice_var.get()))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success", "Member has been inserted successfully")


    def ShowData(self):
        self.textbox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.textbox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.textbox.insert(END, "Id No:\t\t" + self.id_var.get() + "\n")
        self.textbox.insert(END, "First Name:\t\t" + self.firstname_var.get() + "\n")
        self.textbox.insert(END, "Last Name:\t\t" + self.lastname_var.get() + "\n")
        self.textbox.insert(END, "Address:\t\t" + self.address_var.get() + "\n")
        self.textbox.insert(END, "Mobile:\t\t" + self.mobile_var.get() + "\n")
        self.textbox.insert(END, "PostCode:\t\t" + self.postcode_var.get() + "\n")
        self.textbox.insert(END, "Book Id:\t\t" + self.bookid_var.get() + "\n")
        self.textbox.insert(END, "Author:\t\t" + self.author_var.get() + "\n")
        self.textbox.insert(END, "Date Borrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.textbox.insert(END, "Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.textbox.insert(END, "Days On Book:\t\t" + self.daysonbook_var.get() + "\n")
        self.textbox.insert(END, "Late Return Fine:\t\t" + self.latereturnfine_var.get() + "\n")
        self.textbox.insert(END, "Date Over Date:\t\t" + self.dateoverdate_var.get() + "\n")
        self.textbox.insert(END, "Actual Price:\t\t" + self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address_var.set("")
        self.mobile_var.set("")
        self.postcode_var.set("")
        self.bookid_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.daysonbook_var.set("")
        self.datedue_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdate_var.set("")
        self.actualprice_var.set("")

    def iExit(self):
        iExit=tkinter.messagebox.askyesno('Library Management System ','Do You Want to Exit')
        if iExit>0:
            self.root.destroy()
            return

    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password='kunj@ducat', database='india')
        my_cursor = conn.cursor()

        update_query = """
        UPDATE library 
        SET Member=%s, `Id No`=%s, `First Name`=%s, `Last Name`=%s, Address=%s, Mobile=%s,
            `Post Code`=%s, `Book Id`=%s, Author=%s, `Date Borrowed`=%s, `Date Due`=%s, 
            `Days On Book`=%s, `Late Return Fine`=%s, `Date Over Date`=%s, `Actual Price`=%s 
        WHERE PRN_No=%s
        """

        values = (self.member_var.get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(),
                  self.address_var.get(), self.mobile_var.get(), self.postcode_var.get(), self.bookid_var.get(),
                  self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook_var.get(),
                  self.latereturnfine_var.get(), self.dateoverdate_var.get(), self.actualprice_var.get(),
                  self.prn_var.get())

        my_cursor.execute(update_query, values)

        conn.commit()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member Has Been Updated")

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select The Member ")
        else:
            conn = mysql.connector.Connect(host="localhost", user="root", password='kunj@ducat', database='india')
            my_cursor = conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.reset()
            conn.close()
            messagebox.showinfo("Sucess","Member Has been deleted")

    def fatch_data(self):
            conn=mysql.connector.Connect(host="localhost",user="root",password='kunj@ducat',database='india')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from library")
            rows=my_cursor.fetchall()

            if len(rows)!=0:
                self.libray_table.delete(*self.libray_table.get_children())
                for i in rows:
                    self.libray_table.insert("",END,values=i)
                conn.commit()
                conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.libray_table.focus()
        content = self.libray_table.item(cursor_row)
        row = content['values']
        if row:
            self.member_var.set(row[0])
            self.prn_var.set(row[1])
            self.id_var.set(row[2])
            self.firstname_var.set(row[3])
            self.lastname_var.set(row[4])
            self.address_var.set(row[5])
            self.postcode_var.set(row[6])
            self.mobile_var.set(row[7])
            self.bookid_var.set(row[8])
            self.author_var.set(row[9])
            self.dateborrowed_var.set(row[10])
            self.datedue_var.set(row[11])
            self.daysonbook_var.set(row[12])
            self.dateoverdate_var.set(row[13])
            self.latereturnfine_var.set(row[14])
            self.actualprice_var.set(row[15])
        else:
            messagebox.showwarning("No Selection", "Please select a row.")

    def update_clock(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
