'''import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.state('zoomed')
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
#--------------------variables-----
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=10,width=530,height=590)#450,480
#---title---

        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").pack(side=TOP,fill=X)

        lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 15), bg="white").place(x=30,y=60)
        lbl_supplier = Label(product_Frame, text="supplier", font=("goudy old style", 15), bg="white").place(x=30,y=110)
        lbl_Product_name = Label(product_Frame, text="Product Name", font=("goudy old style", 15), bg="white").place(x=30,y=160)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 15), bg="white").place(x=30,y=210)
        lbl_quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30,y=260)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30,y=310)


       
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=("Select"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=("Select"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_qty= Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15),bg="lightyellow").place(x=150,y=260,width=200)
         
        cmb_status= ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active","Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        # Buttons
        btn_add=Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete,font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear,font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=400, width=100, height=40)

            # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=700, y=10, width=600, height=80)

        # Options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)


              #Product Details----

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=400, y=100, width=600, height=390)

        

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(p_frame,columns=("pid","category","supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("pid",text="Product ID")
        self.EmployeeTable.heading("category",text="Category")
        self.EmployeeTable.heading("supplier",text="Supplier")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("price",text="Price")
        self.EmployeeTable.heading("quantity",text="Quantity")
        self.EmployeeTable.heading("status",text="Status")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("pid",width=90)
        self.EmployeeTable.column("category",width=100)
        self.EmployeeTable.column("supplier",width=100)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("price",width=100)
        self.EmployeeTable.column("quantity",width=100)
        self.EmployeeTable.column("status",width=100)


        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        self.fetch_cat_sup()

#-------------------------------------------------------------------------
def fetch_cat_sup(self):
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    try:
        cur.execute("SELECT name FROM category")
        cat = [row[0] for row in cur.fetchall()]
        self.cmb_cat['values']

        cur.execute("SELECT name FROM supplier")
        sup = [row[0] for row in cur.fetchall()]
        self.cmb_sup['values']

        return cat, sup

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

  
 

def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select"or self.var_sup.get()=="Select" or self.var_name.get()=="" :
                messagebox.showerror("Error", "All fields Required", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),) 
                )
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","This product already exists,try different",parent=self.root)
                else:
                    cur.execute("Insert into product (category,supplier,name,price,quantity,status) values(?,?,?,?,?,?)",(
                    self.var_cat.get(),
                    self.var_sup.get(),
                    self.var_name.get(),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                   
                    ))
                con.commit()
                messagebox.showinfo("Success","Product Added Successfully!",parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
            

def show(self):
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Select * from product")
                rows=cur.fetchall()
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('',END,values=row)

            except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

def get_data(self,ev):
      f=self.ProductTable.focus()
      content=(self.ProductTable.item(f))
      row=content['values']
      print(row)
      self.var_emp_id.set(row[0]),
      self.var_name.set(row[1]),
      self.var_email.set(row[2]),
      self.var_gender.set(row[3]),
      self.var_contact.set(row[4]),

      self.var_dob.set(row[5]),
      self.var_doj.set(row[6]),
      
      self.var_pass.set(row[7]),
      self.var_utype.set(row[8]),
      self.txt_address.insert(END,row[9])
      self.var_salary.set(row[10])

def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be Required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),) 
                )
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invalid Employee ID!",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_contact.get(),

                    self.var_dob.get(),
                    self.var_doj.get(),

                    self.var_pass.get(),
                    self.var_utype.get(),
                    self.txt_address.get("1.0", END),
                    self.var_salary.get(),
                    self.var_emp_id.get()
                    ))
                con.commit()
                messagebox.showinfo("Success","Employee Updated Successfully!",parent=self.root)
                self.show()
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be Required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),) 
                )
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID!",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirmation","Do you really want to delete it?",parent=self.root)
                    if op:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Details Deleted Successfully!",parent=self.root)
                    
                    self.clear()
                 

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
        
def clear(self):
         self.var_emp_id.set(""),
         self.var_name.set(""),
         self.var_email.set(""),
         self.var_gender.set(""),
         self.var_contact.set(""),

         self.var_dob.set(""),
         self.var_doj.set(""),
      
         self.var_pass.set(""),
         self.var_utype.set("Admin"),
         self.txt_address.delete('1.0',END)
         self.var_salary.set("")
         self.show()

def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error","Select Search By Option",parent=self.root)
                elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error","Search input should be required",parent=self.root)
                else:
                    cur.execute(f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE ?", ('%' + self.var_searchtxt.get() + '%',))

                    
                rows=cur.fetchall()
                if len(rows)!=0:
                   self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                   for row in rows:
                    self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!",parent=self.root)
        except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
'''
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

root = Tk()
root.title("Product Management System")

# Automatically maximize window on start
root.state('zoomed')  # For Windows (auto full screen)

class productClass:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar(master)
        self.var_searchtxt = StringVar(master)
        self.var_pid = StringVar(master)
        self.var_cat = StringVar(master)
        self.var_sup = StringVar(master)
        self.sup_list=[]
        self.cat_list=[]
        self.fetch_cat_sup()
        self.var_name = StringVar(master)
        self.var_price = StringVar(master)
        self.var_qty = StringVar(master)
        self.var_status = StringVar(master)

        # Title
        lbl_title = Label(self.root, text="Manage Product Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=410, y=9, width=150, height=30)

        # Product Details
        product_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=100, width=450, height=390)

        lbl_cat = Label(product_Frame, text="Category", font=("goudy old style", 15), bg="white").place(x=30, y=30)
        lbl_sup = Label(product_Frame, text="Supplier", font=("goudy old style", 15), bg="white").place(x=30, y=70)
        lbl_name = Label(product_Frame, text="Name", font=("goudy old style", 15), bg="white").place(x=30, y=110)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 15), bg="white").place(x=30, y=150)
        lbl_qty = Label(product_Frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30, y=190)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30, y=230)

        self.cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("goudy old style", 15))
        self.cmb_cat.place(x=150, y=30, width=200)

        self.cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=("goudy old style", 15))
        self.cmb_sup.place(x=150, y=70, width=200)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=110, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=150, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=190, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=230, width=200)
        cmb_status.current(0)

        # Buttons
        btn_add = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=10, y=270, width=100, height=30)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=120, y=270, width=100, height=30)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=230, y=270, width=100, height=30)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=340, y=270, width=100, height=30)

        # Product Table
        product_Frame2 = Frame(self.root, bd=3, relief=RIDGE)
        product_Frame2.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(product_Frame2, orient=VERTICAL)
        scrollx = Scrollbar(product_Frame2, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(product_Frame2, columns=("pid", "category", "supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid", text="P ID")
        self.ProductTable.heading("category", text="Category")
        self.ProductTable.heading("supplier", text="Supplier")
        self.ProductTable.heading("name", text="Name")
        self.ProductTable.heading("price", text="Price")
        self.ProductTable.heading("qty", text="Quantity")
        self.ProductTable.heading("status", text="Status")
        self.ProductTable["show"] = "headings"

        self.ProductTable.column("pid", width=90)
        self.ProductTable.column("category", width=100)
        self.ProductTable.column("supplier", width=100)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)

        self.ProductTable.pack(fill=BOTH, expand=1)
        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        self.fetch_cat_sup()

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = [row[0] for row in cur.fetchall()]
           
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                   self.cat_list.append(i[0])
        
            

            cur.execute("SELECT name FROM supplier")
            sup = [row[0] for row in cur.fetchall()]
            if len(cat)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in cat:
                   self.sup_list.append(i[0])
           

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row:
                    messagebox.showerror("Error", "Product already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (category, supplier, name, price, quantity, status) VALUES (?,?,?,?,?,?)", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product added successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = self.ProductTable.item(f)
        row = content['values']

        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from the list", parent=self.root)
            else:
                cur.execute("UPDATE product SET category=?, supplier=?, name=?, price=?, quantity=?, status=? WHERE pid=?", (
                    self.var_cat.get(),
                    self.var_sup.get(),
                    self.var_name.get(),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                    self.var_pid.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Product updated successfully", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select product from the list", parent=self.root)
            else:
                cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                con.commit()
                messagebox.showinfo("Success", "Product deleted successfully", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_pid.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM product WHERE {self.var_searchby.get()} LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
