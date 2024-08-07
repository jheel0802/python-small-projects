from tkinter import*
from tkinter import ttk,messagebox
from Company_Master import company_class
from Product_Master import product_class
from Orders import order_class

class OMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Order Management System")
        self.root.config (bg="white")
        #==========title================
        title=Label(self.root,text="Order Management System",font=("arial",35,"bold")).place(x=0,y=0,relwidth=1,height=70)
        #==========Menu btns============
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=10,y=80,width=230,height=600)
        lbl_menu=Label(LeftMenu,text="Menu",font=("arial",30,"bold"),bg="light blue").pack(side=TOP,fill=X)
        btn_company=Button(LeftMenu,text="Company Master",command=self.company,font=("arial",20),cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product Master",command=self.product,font=("arial",20),cursor="hand2").pack(side=TOP,fill=X)
        btn_order=Button(LeftMenu,text="Orders",command=self.order,font=("arial",20),cursor="hand2").pack(side=TOP,fill=X)
        #==========logout btn===========
        btn_logout=Button(LeftMenu,text="Logout",font=("arial",20,"bold"),cursor="hand2",command=root.destroy).pack(side=BOTTOM,fill=X)
        #data
        #lbl_company=Label(self.root,text="Companies\n[ 0 ]",font=("arial",15),bg="light pink",relief=RIDGE).place(x=350,y=100,width=200,height=150)
        #lbl_product=Label(self.root,text="Products\n[ 0 ]",font=("arial",15),bg="orange",relief=RIDGE).place(x=600,y=100,width=200,height=150)
        #lbl_order=Label(self.root,text="Orders\n[ 0 ]",font=("arial",15),bg="yellow",relief=RIDGE).place(x=850,y=100,width=200,height=150)

    def company(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=company_class(self.new_win)

    def product(self):
        self.new_win1=Toplevel(self.root)
        self.new_obj1=product_class(self.new_win1)

    def order(self):
        self.new_win2=Toplevel(self.root)
        self.new_obj2=order_class(self.new_win2)


if __name__=="__main__":
    root=Tk()
    obj=OMS(root)
    root.mainloop()
