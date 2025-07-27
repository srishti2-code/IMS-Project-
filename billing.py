import tkinter as tk
from tkinter import *
import os
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # === Title without Image ===
        title = Label(
            self.root,
            text="Inventory Management System",
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx=20
        ).place(x=1, y=1, relwidth=1, height=70)
        
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=30, width=150)

        # === Clock ===
        self.lbl_clock = Label(
            self.root,
            text="Welcome to Inventory Management System(IMS)\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d",
            fg="white",
        )
        self.lbl_clock.place(x=1, y=70, relwidth=1, height=30)


        #----Product_Frame-----
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)
        text_search=Label(ProductFrame2,textvariable= self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=125,y=47,width=150,height=22)
# === Run the App ===
if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()


