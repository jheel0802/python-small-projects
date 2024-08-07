from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class company_class:
    def __init__(self,root):
        self.root = root
        self.root.geometry("950x560+240+105")
        self.root.title("Company Master")
        self.root.config (bg="pink")
        self.root.focus_force()
        #=============================================
        self.var_comp_id=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_gst_no=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

        title=Label(self.root,text="Company Master",font=("arial",30,"bold")).place(x=0,y=0,relwidth=1,height=60)   

        lbl_comp_id=Label(self.root,text="Company ID",font=("Times New Roman",15),bg="white").place(x=10,y=70,width=190,height=30) 
        lbl_comp_name=Label(self.root,text="Company Name",font=("Times New Roman",15),bg="white").place(x=10,y=120,width=190,height=30)
        lbl_gst_no=Label(self.root,text="GST No.",font=("Times New Roman",15),bg="white").place(x=10,y=170,width=190,height=30)
        lbl_phone=Label(self.root,text="Phone",font=("Times New Roman",15),bg="white").place(x=10,y=220,width=190,height=30)
        lbl_email=Label(self.root,text="Email",font=("Times New Roman",15),bg="white").place(x=10,y=270,width=190,height=30)
        lbl_address=Label(self.root,text="Address",font=("Times New Roman",15),bg="white").place(x=10,y=320,width=190,height=30)

        txt_comp_id=Entry(self.root,textvariable=self.var_comp_id,font=("Times New Roman",15),bg="white").place(x=210,y=70,width=190,height=30) 
        txt_comp_name=Entry(self.root,textvariable=self.var_name,font=("Times New Roman",15),bg="white").place(x=210,y=120,width=190,height=30)
        txt_gst_no=Entry(self.root,textvariable=self.var_gst_no,font=("Times New Roman",15),bg="white").place(x=210,y=170,width=190,height=30)
        txt_phone=Entry(self.root,textvariable=self.var_phone,font=("Times New Roman",15),bg="white").place(x=210,y=220,width=190,height=30)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("Times New Roman",15),bg="white").place(x=210,y=270,width=190,height=30)
        self.txt_address=Entry(self.root,textvariable=self.var_address,font=("Times New Roman",15),bg="white").place(x=210,y=320,width=190,height=30)

        btn_add=Button(self.root,text="Add",command=self.add,font=("arial",12),cursor="hand2").place(x=10,y=470,width=190,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("arial",12),cursor="hand2").place(x=210,y=470,width=190,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("arial",12),cursor="hand2").place(x=10,y=510,width=190,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("arial",12),cursor="hand2").place(x=210,y=510,width=190,height=30)

        comp_frame=Frame(self.root,bd=3,relief=RIDGE).place(x=410,y=70,width=530,height=480)

        self.companytable=ttk.Treeview(self.root,columns=("ID","Name","GST","Phone","Email","Address"))
               
        self.companytable.place(x=410,y=70,width=530,height=480)
        self.companytable.heading("ID",text="Company ID")
        self.companytable.heading("Name",text="Name")
        self.companytable.heading("GST",text="GST no.")
        self.companytable.heading("Phone",text="Phone")
        self.companytable.heading("Email",text="Email")
        self.companytable.heading("Address",text="Address")
        self.companytable["show"]="headings"

        self.companytable.column("ID",width=80)
        self.companytable.column("Name",width=80)
        self.companytable.column("GST",width=80)
        self.companytable.column("Phone",width=80)
        self.companytable.column("Email",width=80)
        self.companytable.column("Address",width=80)
        self.companytable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#=========================================================================
    def add(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_comp_id.get()=="" or self.var_address.get()=="" or self.var_email.get()=="" or self.var_gst_no.get()=="" or self.var_name.get()=="" or self.var_phone.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            if self.var_phone.get().isdigit()==False:               
                messagebox.showerror("Error","Phone must contain numbers only",parent=self.root)
            else:
                cur.execute("Select * from company where ID=?",(self.var_comp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","The ID has been assigned, try different ID",parent=self.root)
                else:
                    cur.execute("Insert into company (ID,Name,GST,Phone,Email,Address) values(?,?,?,?,?,?)",(self.var_comp_id.get(),self.var_name.get(),self.var_gst_no.get(),self.var_phone.get(),self.var_email.get(),self.var_address.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'oms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from company")
            rows=cur.fetchall()
            self.companytable.delete(*self.companytable.get_children())
            for row in rows:
                self.companytable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.companytable.focus()
        content=(self.companytable.item(f))
        row=content['values']
        #print(row)
        self.var_comp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_gst_no.set(row[2])
        self.var_phone.set(row[3])
        self.var_email.set(row[4])
        self.var_address.set(row[5])

    def update(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_comp_id.get()=="":
                messagebox.showerror("Error","Company ID must be required",parent=self.root)
            else:
                cur.execute("Select * from company where ID=?",(self.var_comp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute("Update company set Name=?,GST=?,Phone=?,Email=?,Address=? where ID=?",(self.var_name.get(),self.var_gst_no.get(),self.var_phone.get(),self.var_email.get(),self.var_address.get(),self.var_comp_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_comp_id.get()=="":
                messagebox.showerror("Error","Invalid Company ID",parent=self.root)
            else:
                cur.execute("Select * from company where ID=?",(self.var_comp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Company ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from company where ID=?",(self.var_comp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Company Deleted Successfully",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_comp_id.set("")
        self.var_name.set("")
        self.var_gst_no.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.show()

if __name__=="__main__":
    root=Tk()
    obj=company_class(root)
    root.mainloop()