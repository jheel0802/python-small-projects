from sqlite3.dbapi2 import complete_statement
from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class order_class:
    def __init__(self,root):
        self.root = root
        self.root.geometry("950x560+315+105")
        self.root.title("Orders")
        self.root.config (bg="white")
        self.root.focus_force()
        #=========================

        self.var_order=StringVar()
        self.var_company=StringVar()
        self.var_product=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_rate=StringVar()
        self.comp_list=[]
        self.prod_list=[]
        self.rate_list=[]
        self.fetch_company_product_price()
        
        title=Label(self.root,text="Orders",font=("arial",35,"bold"),bg="light blue").pack(side=TOP,fill=X)

        lbl_order=Label(self.root,text="Order ID",font=("Times New Roman",15),bg="pink").place(x=15,y=80,width=150,height=30)
        lbl_company=Label(self.root,text="Company",font=("Times New Roman",15),bg="pink").place(x=15,y=135,width=150,height=30)
        lbl_product=Label(self.root,text="Product",font=("Times New Roman",15),bg="pink").place(x=15,y=190,width=150,height=30)
        lbl_quantity=Label(self.root,text="Quantity",font=("Times New Roman",15),bg="pink").place(x=15,y=245,width=150,height=30)
        lbl_status=Label(self.root,text="Status",font=("Times New Roman",15),bg="pink").place(x=15,y=300,width=150,height=30)

        txt_order=Entry(self.root,textvariable=self.var_order,font=("Arial",15),bg="white").place(x=225,y=80,width=150,height=30)         
        cmb_company=ttk.Combobox(self.root,textvariable=self.var_company,values=self.comp_list,font=("Arial",15),state='readonly',justify=CENTER).place(x=225,y=135,width=150,height=30)        
        cmb_product=ttk.Combobox(self.root,textvariable=self.var_product,values=self.prod_list,font=("Arial",15),state='readonly',justify=CENTER).place(x=225,y=190,width=150,height=30)
        txt_quantity=Entry(self.root,textvariable=self.var_quantity,font=("Arial",15),bg="white").place(x=225,y=245,width=150,height=30)         
        cmb_status=ttk.Combobox(self.root,textvariable=self.var_status,values=('Pending','Delivered','Cancelled'),font=("Arial",15),state='readonly',justify=CENTER).place(x=225,y=300,width=150,height=30)   

        btn_add=Button(self.root,text="Add",command=self.add,font=("arial",12),cursor="hand2").place(x=10,y=470,width=150,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("arial",12),cursor="hand2").place(x=210,y=470,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("arial",12),cursor="hand2").place(x=10,y=510,width=150,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("arial",12),cursor="hand2").place(x=210,y=510,width=150,height=30)

#===================================================================================================================

        self.ordertable=ttk.Treeview(self.root,columns=("ID","Company","Product","Quantity","Rate","Status"))
               
        self.ordertable.place(x=410,y=70,width=530,height=200)
        self.ordertable.heading("ID",text="Order ID")
        self.ordertable.heading("Company",text="Company Name")
        self.ordertable.heading("Product",text="Product Name")
        self.ordertable.heading("Quantity",text="Quantity")
        self.ordertable.heading("Rate",text="Rate")
        self.ordertable.heading("Status",text="Status")
        self.ordertable["show"]="headings"

        self.ordertable.column("ID",width=80)
        self.ordertable.column("Company",width=80)
        self.ordertable.column("Product",width=80)
        self.ordertable.column("Quantity",width=80)
        self.ordertable.column("Rate",width=80)
        self.ordertable.column("Status",width=80)
        self.ordertable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        self.fetch_company_product_price()

        self.detailtable=ttk.Treeview(self.root,columns=("ID","Company","Product","Quantity","Rate","Status"))
               
        self.detailtable.place(x=410,y=300,width=530,height=200)
        self.detailtable.heading("ID",text="Order ID")
        self.detailtable.heading("Company",text="Company Name")
        self.detailtable.heading("Product",text="Product Name")
        self.detailtable.heading("Quantity",text="Quantity")
        self.detailtable.heading("Rate",text="Rate")
        self.detailtable.heading("Status",text="Status")
        self.detailtable["show"]="headings"

        self.detailtable.column("ID",width=80)
        self.detailtable.column("Company",width=80)
        self.detailtable.column("Product",width=80)
        self.detailtable.column("Quantity",width=80)
        self.detailtable.column("Rate",width=80)
        self.detailtable.column("Status",width=80)
        self.detailtable.bind("<ButtonRelease-1>",self.get_data)

        
        

#=======================================================================================================
    
    def fetch_company_product_price(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            cur.execute("Select Name from company")
            comp=cur.fetchall()
            for i in comp:
                self.comp_list.append(i[0])
            cur.execute("Select Name from product")
            prod=cur.fetchall()
            for i in prod:
                self.prod_list.append(i[0])
                        
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_order.get()=="" or self.var_company.get()=="" or self.var_product.get()=="" or self.var_quantity.get()=="" or self.var_status.get()=="":
                messagebox.showerror("Error","All fields required",parent=self.root)
            else:
                cur.execute("Select * from orders where ID=?",(self.var_order.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","The ID has been assigned, try different ID",parent=self.root)
                else:
                    cur.execute("Insert into orders (ID,Company,Product,Quantity,Status) values(?,?,?,?,?)",(self.var_order.get(),self.var_company.get(),self.var_product.get(),self.var_quantity.get(),self.var_status.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'oms.db')
        cur=con.cursor()
        try:
         #   cur.execute("select * from orders")
            cur.execute("select orders.ID,orders.company,orders.product,orders.quantity,product.rate,orders.status from orders,product where orders.product=product.name")
            rows=cur.fetchall()
            self.ordertable.delete(*self.ordertable.get_children())
            for row in rows:
                self.ordertable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.ordertable.focus()
        content=(self.ordertable.item(f))
        row=content['values']
        #print(row)
        self.var_order.set(row[0])
        self.var_company.set(row[1])
        self.var_product.set(row[2])
        self.var_quantity.set(row[3])
        self.var_status.set(row[5])

    def update(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_order.get()=="":
                messagebox.showerror("Error","Order ID must be required",parent=self.root)
            else:
                cur.execute("Select * from orders where ID=?",(self.var_order.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    cur.execute("Update orders set Company=?,Product=?,Quantity=?,Status=? where ID=?",(self.var_company.get(),self.var_product.get(),self.var_quantity.get(),self.var_status.get(),self.var_order.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'oms.db')
        cur = con.cursor()
        try:
            if self.var_order.get()=="":
                messagebox.showerror("Error","Invalid Order ID",parent=self.root)
            else:
                cur.execute("Select * from orders where ID=?",(self.var_order.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Company ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from orders where ID=?",(self.var_order.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Company Deleted Successfully",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):
        self.var_order.set("")
        self.var_company.set("")
        self.var_product.set("")
        self.var_quantity.set("")
        self.var_status.set("")
        self.show()

        

if __name__=="__main__":
    root=Tk()
    obj=order_class(root)
    root.mainloop()