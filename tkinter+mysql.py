from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

def main():
    root = Tk()
    app = Window1(root)
    
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Order Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame,text = "Order Management System", font=('arial',40,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=10)

        self.Loginframe1 = Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2 = Frame(self.frame,width=1010,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3 = Frame(self.frame,width=1200,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)

        self.lblUsername = Label(self.Loginframe1,text = "Username", font=('arial',30),bd=20)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername = Entry(self.Loginframe1, font=('arial',30),bd=20,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword = Label(self.Loginframe1,text = "Password", font=('arial',30),bd=20)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword = Entry(self.Loginframe1, font=('arial',30),bd=20,textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)


        self.btnLogin = Button(self.Loginframe2,text="Login",width=20,font=('arial',20),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset = Button(self.Loginframe2,text="Reset",width=20,font=('arial',20))
        self.btnReset.grid(row=0,column=1)

        self.btnExit = Button(self.Loginframe2,text="Exit",width=20,font=('arial',20))
        self.btnExit.grid(row=0,column=2)

        self.btnCompany = Button(self.Loginframe3,text="Company Master",command=self.Company_window,width=20,font=('arial',14),state= DISABLED)
        self.btnCompany.grid(row=0,column=0)

        self.btnRate = Button(self.Loginframe3,text="Rate Master",command=self.Rate_window,width=20,font=('arial',14),state= DISABLED)
        self.btnRate.grid(row=0,column=1)

        self.btnOrder = Button(self.Loginframe3,text="Orders",command=self.Order_window,width=20,font=('arial',14),state= DISABLED)
        self.btnOrder.grid(row=0,column=2)        

    def Login_System(self):
        user = (self.Username.get())
        passw = (self.Password.get())

        if (user == str(1234) and (passw == str(2345))):
            self.btnCompany.config(state = NORMAL)
            self.btnRate.config(state = NORMAL)
            self.btnOrder.config(state = NORMAL)
        else:
            tkinter.messagebox.askokcancel("Order Management System","Incorrect Username or Password")
            self.btnCompany.config(state = DISABLED)
            self.btnRate.config(state = DISABLED)
            self.btnOrder.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")

    def Company_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Rate_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def Order_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)



class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Company Master")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        pass

class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Rate Master")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        pass

class Window4:
    def __init__(self,master):
        self.master = master
        self.master.title("Orders")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        pass

if __name__=='__main__':
    main()

