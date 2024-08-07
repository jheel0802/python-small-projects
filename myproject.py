from tkinter import*
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",font=("Times New Roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP, fill=X)

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=80,width=450,height=570)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("Times New Roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=0,padx=20,sticky="w")
        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=0,padx=20,sticky="w")
        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=0,padx=20,sticky="w")
        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=0,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,font=("Times New Roman",14,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=1,pady=1)

        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=0,padx=20,sticky="w")
        txt_contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=0,padx=20,sticky="w")
        txt_dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=0,padx=20,sticky="w")
        txt_address=Text(Manage_Frame,width=25,height=4)
        txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=500,width=410)

        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)        

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=80,width=750,height=570)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=18,y=20,width=705,height=515)

root=Tk()
ob=Student(root)
root.mainloop()