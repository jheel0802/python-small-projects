from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class product_class:
    def __init__(self,root):
        self.root = root
        self.root.geometry("950x560+315+105")
        self.root.title("Product Master")
        self.root.config (bg="pink")
        self.root.focus_force()
        #=============================================
        self.var_product_id=StringVar()
        self.var_name=StringVar()
        self.var_rate=StringVar()

        title=Label(self.root,text="Product Master",font=("arial",30,"bold")).place(x=0,y=0,relwidth=1,height=60)   

        lbl_product_id=Label(self.root,text="Product ID",font=("Times New Roman",15),bg="white").place(x=10,y=70,width=190,height=30) 
        lbl_product_name=Label(self.root,text="Product Name",font=("Times New Roman",15),bg="white").place(x=10,y=120,width=190,height=30)
        lbl_rate=Label(self.root,text="Rate",font=("Times New Roman",15),bg="white").place(x=10,y=170,width=190,height=30)
        
        txt_product_id=Entry(self.root,textvariable=self.var_product_id,font=("Times New Roman",15),bg="white").place(x=210,y=70,width=190,height=30) 
        txt_product_name=Entry(self.root,textvariable=self.var_name,font=("Times New Roman",15),bg="white").place(x=210,y=120,width=190,height=30)
        txt_rate=Entry(self.root,textvariable=self.var_rate,font=("Times New Roman",15),bg="white").place(x=210,y=170,width=190,height=30)
       
        btn_add=Button(self.root,text="Add",command=self.add,font=("arial",12),cursor="hand2").place(x=10,y=470,width=190,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("arial",12),cursor="hand2").place(x=210,y=470,width=190,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("arial",12),cursor="hand2").place(x=10,y=510,width=190,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("arial",12),cursor="hand2").place(x=210,y=510,width=190,height=30)

        self.producttable=ttk.Treeview(self.root,columns=("ID","Name","Rate"))
        
        self.producttable.place(x=410,y=70,width=530,height=480)

        self.producttable.heading("ID",text="Product ID")
        self.producttable.heading("Name",text="Name")
        self.producttable.heading("Rate",text="Rate")
        self.producttable["show"]="headings"

        self.producttable.column("ID",width=80)
        self.producttable.column("Name",width=80)
        self.producttable.column("Rate",width=80)
        self.producttable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#==================================================================================

    def add(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_product_id.get()=="" or self.var_name.get()=="" or self.var_product_id.get()=="" or self.var_rate.get()=="":
                messagebox.showerror("Error","All fields required required",parent=self.root)
            else:
                cur.execute("Select * from product where ID=?",(self.var_product_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","The ID has been assigned, try different ID",parent=self.root)
                else:
                    cur.execute("Insert into product (ID,Name,Rate) values(?,?,?)",(self.var_product_id.get(),self.var_name.get(),self.var_rate.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'oms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.producttable.delete(*self.producttable.get_children())
            for row in rows:
                self.producttable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.producttable.focus()
        content=(self.producttable.item(f))
        row=content['values']
        #print(row)
        self.var_product_id.set(row[0])
        self.var_name.set(row[1])
        self.var_rate.set(row[2])

    def update(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error","Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from product where ID=?",(self.var_product_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute("Update product set Name=?,Rate=? where ID=?",(self.var_name.get(),self.var_rate.get(),self.var_product_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_product_id.get()=="":
                messagebox.showerror("Error","Invalid Product ID",parent=self.root)
            else:
                cur.execute("Select * from product where ID=?",(self.var_product_id.get(),))
                row=cur.fetchone()
                if row==None:
                    #=========================
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where ID=?",(self.var_product_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_product_id.set("")
        self.var_name.set("")
        self.var_rate.set("")
        self.show()


if __name__=="__main__":
    root=Tk()
    obj=product_class(root)
    root.mainloop()