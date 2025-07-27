'''
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from networkx import is_path
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product  import productClass
from sales import salesClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # === Title ===
        # Retain a reference to the PhotoImage object
        self.icon_title = PhotoImage(file=r"C:\Users\Admin\Desktop\IMS PROJECT\shopping-cart.png")
         # Open the image using Pillow
        image = Image.open(r"C:\Users\Admin\Desktop\IMS PROJECT\shopping-cart.png")
        # Resize the image (width=50, height=50, adjust as needed)
        resized_image = image.resize((50, 50), Image.Resampling.LANCZOS)
        # Convert to PhotoImage
        self.icon_title = ImageTk.PhotoImage(resized_image)
        title = Label(
            self.root,
            text="Inventory Management System",
            image=self.icon_title,
            compound=LEFT,
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx=20
        ).place(x=1, y=1, relwidth=1, height=70)
        #--btn_logout--#
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=30,width=150)

        #==clock--#
        self.lbl_clock = Label(
            self.root,
            text="Welcome to Inventory Management System(IMS)\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d",
            fg="white",
        )
        self.lbl_clock.place(x=1, y=70, relwidth=1, height=30)

        #left menu--#
        self.MenuLogo=Image.open(r"C:\Users\Admin\Desktop\IMS PROJECT\IMS.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee = Button(
            LeftMenu, text="Employee", command = self.open_employee_window,
            font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2"
        )
        btn_employee.pack(side=TOP, fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.open_supplier_window,font=("times new roman",23,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.open_category_window,font=("times new roman",23,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)
        btn_products=Button(LeftMenu,text="Products",command=self.open_product_window,font=("times new roman",23,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.open_sales_window,font=("times new roman",23,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",font=("times new roman",23,"bold"),bg="white",bd=4,cursor="hand2").pack(side=TOP,fill=X)

        

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #==footer--#
        lbl_footer = Label(
            self.root,
            text="IMS-Inventory Management System | Developed by Srishti Sharma",
            font=("times new roman", 12),
            bg="#4d636d",
            fg="white",
        )
        lbl_footer.pack(side=BOTTOM,fill=X)
#===========================================================================

    def open_employee_window(self):
        # Opens the Employee Window
          new_win = Toplevel(self.root)
          employeeClass(new_win)
        
    def open_supplier_window(self):
        # Opens the supplier Window
          new_win = Toplevel(self.root)
          supplierClass(new_win)

    def open_category_window(self):
        # Opens the category Window
          new_win = Toplevel(self.root)
          categoryClass(new_win)

    def open_product_window(self):
        # Opens the product Window
          new_win = Toplevel(self.root)
          productClass(new_win)

    def open_sales_window(self):
        # Opens the product Window
          new_win = Toplevel(self.root)
          salesClass(new_win)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

'''

"""import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # === Title ===
        image = Image.open(r"C:\Users\Admin\Desktop\IMS PROJECT\shopping-cart.png")
        resized_image = image.resize((50, 50), Image.Resampling.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(resized_image)

        title = Label(
            self.root,
            text="Inventory Management System",
            image=self.icon_title,
            compound=LEFT,
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w",
            padx=20
        ).place(x=1, y=1, relwidth=1, height=70)

        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=30, width=150)

        # Clock
        self.lbl_clock = Label(
            self.root,
            text="Welcome to Inventory Management System(IMS)\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15),
            bg="#4d636d",
            fg="white",
        )
        self.lbl_clock.place(x=1, y=70, relwidth=1, height=30)

        # Left Menu
        image_menu = Image.open(r"C:\Users\Admin\Desktop\IMS PROJECT\IMS.png")
        image_menu = image_menu.resize((200, 200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(image_menu)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)

        Button(LeftMenu, text="Employee", command=self.open_employee_window, font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Supplier", command=self.open_supplier_window, font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Category", command=self.open_category_window, font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Products", command=self.open_product_window, font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Sales", command=self.open_sales_window, font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Exit", font=("times new roman", 23, "bold"), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)

        # Dashboard Summary
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # Footer
        lbl_footer = Label(
            self.root,
            text="IMS-Inventory Management System | Developed by Srishti Sharma",
            font=("times new roman", 12),
            bg="#4d636d",
            fg="white",
        )
        lbl_footer.pack(side=BOTTOM, fill=X)

    # Window Functions
    def open_employee_window(self):
        new_win = Toplevel(self.root)
        employeeClass(new_win)

    def open_supplier_window(self):
        new_win = Toplevel(self.root)
        supplierClass(new_win)

    def open_category_window(self):
        new_win = Toplevel(self.root)
        categoryClass(new_win)

    def open_product_window(self):
        new_win = Toplevel(self.root)
        productClass(new_win)

    def open_sales_window(self):
        new_win = Toplevel(self.root)
        salesClass(new_win)


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
"""