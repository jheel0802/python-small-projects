from tkinter import*
from tkinter import ttk,messagebox
class OMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x400+350+25")
        self.root.resizable(False, False)
        self.root.title("To-Do List")
        self.root.config (bg="#fff0f5")
        #==========title================
        title=Label(self.root,text="My To-Do List",bg="#02075d",fg="#fff0f5",font=("arial",25,"bold")).place(x=0,y=0,relwidth=1,height=45)
        #==========Menu btns============
        check_box1=Checkbutton(self.root).place(x=50,y=200)
        lbl_menu=Label(self.root,text="Menu",font=("arial",30,"bold"),bg="light blue").place(x=50,y=50,width=100,height=50)
        btn_company=Button(self.root,text="Company Master",font=("arial",20),cursor="hand2").place(x=50,y=50,width=100,height=50)
        btn_product=Button(self.root,text="Product Master",font=("arial",20),cursor="hand2").place(x=50,y=50,width=100,height=50)
        btn_order=Button(self.root,text="Orders",font=("arial",20),cursor="hand2").place(x=50,y=50,width=100,height=50)

if __name__=="__main__":
    root=Tk()
    obj=OMS(root)
    root.mainloop()
