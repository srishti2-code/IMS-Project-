import tkinter as tk
from tkinter import *
import os
import time
import sqlite3
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
                            bg="yellow", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=30, width=150)

        # === Clock Label (Dynamic) ===
        self.lbl_clock = Label(
            self.root,
            text="Welcome to Inventory Management System(IMS)\t\t Date: \t\t Time:",
            font=("times new roman", 15),
            bg="#4d636d",
            fg="white",
        )
        self.lbl_clock.place(x=1, y=70, relwidth=1, height=30)
        self.update_time()

        # === Left Menu ===
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        Button(LeftMenu, text="Employee", command=self.open_employee_window,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Supplier", command=self.open_supplier_window,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Category", command=self.open_category_window,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Products", command=self.open_product_window,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Sales", command=self.open_sales_window,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)
        Button(LeftMenu, text="Exit", command=self.root.destroy,
               font=("times new roman", 20), bg="white", bd=4, cursor="hand2").pack(side=TOP, fill=X)

        # === Dashboard Boxes ===
        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE,
                               bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # === Footer ===
        lbl_footer = Label(
            self.root,
            text="IMS - Inventory Management System | Developed by Srishti Sharma",
            font=("times new roman", 12),
            bg="#4d636d",
            fg="white",
        )
        lbl_footer.pack(side=BOTTOM, fill=X)

        # === Update dashboard data ===
        self.update_dashboard_counts()

    # === Update Clock Function ===
    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(
            text=f"Welcome to Inventory Management System(IMS)\t\t Date: {current_date}\t\t Time: {current_time}"
        )
        self.root.after(1000, self.update_time)

    # === Update Count Data from DB ===
    def update_dashboard_counts(self):
        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()

            cur.execute("SELECT COUNT(*) FROM employee")
            emp = cur.fetchone()[0]
            self.lbl_employee.config(text=f"Total Employee\n[ {emp} ]")

            cur.execute("SELECT CO   UNT(*) FROM supplier")
            sup = cur.fetchone()[0]
            self.lbl_supplier.config(text=f"Total Supplier\n[ {sup} ]")

            cur.execute("SELECT COUNT(*) FROM category")
            cat = cur.fetchone()[0]
            self.lbl_category.config(text=f"Total Category\n[ {cat} ]")

            cur.execute("SELECT COUNT(*) FROM product")
            prod = cur.fetchone()[0]
            self.lbl_product.config(text=f"Total Product\n[ {prod} ]")

            sales_dir = "sales"  # Make sure this folder exists
            total_sales = len(os.listdir(sales_dir)) if os.path.exists(sales_dir) else 0
            self.lbl_sales.config(text=f"Total Sales\n[ {total_sales} ]")

            con.close()
        except Exception as ex:
            print("Error updating dashboard counts:", ex)

    def logout(self):
        self.root.destroy()

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


# === Launch App ===
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()




