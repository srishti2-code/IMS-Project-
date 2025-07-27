import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1920x1080")
        self.root.state('zoomed')
        self.root.title("Inventory Management System")
        self.root.config(bg="lightyellow")
        self.root.focus_force()

        # All variables
        self.var_searchtxt = StringVar(master)

        self.var_sup_invoice = StringVar(master)
        self.var_contact = StringVar(master)
        self.var_name = StringVar(master)

        # Search Frame
        search_frame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="lightyellow")
        search_frame.place(x=50, y=10, width=600, height=60)

        lbl_search = Label(search_frame, text="Search by Invoice No.", bg="lightyellow", font=("goudy old style", 15))
        lbl_search.place(x=10, y=5)

        txt_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="white")
        txt_search.place(x=230, y=5, width=180)

        btn_search = Button(search_frame, text="Search", command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=420, y=2, width=100, height=30)

        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 15,"bold"), bg="#0f4d7d", fg="lightyellow").place(x=50, y=80, width=1000,height=40)

        # Row 1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.:", font=("goudy old style", 15), bg="lightyellow").place(x=50, y=140)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=140, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Name:", font=("goudy old style", 15), bg="lightyellow").place(x=50, y=180)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=180, width=180)

        # Row 3
        lbl_contact = Label(self.root, text="Contact:", font=("goudy old style", 15), bg="lightyellow").place(x=50, y=220)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=220, width=180)

        # Row 4
        lbl_desc = Label(self.root, text="Description:", font=("goudy old style", 15), bg="lightyellow").place(x=50, y=260)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=190, y=260, width=450, height=160)

        # Buttons
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="lightyellow", cursor="hand2").place(x=180, y=440, width=110, height=35)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="lightyellow", cursor="hand2").place(x=300, y=440, width=110, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="lightyellow", cursor="hand2").place(x=420, y=440, width=110, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="lightyellow", cursor="hand2").place(x=540, y=440, width=110, height=35)

        # Supplier Table Frame
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=800, y=140, width=600, height=500)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "description"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("description", text="Description")
        self.supplierTable["show"] = "headings"

        self.supplierTable.column("invoice", width=100)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("description", width=200)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice Must be Required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Invoice no. already assigned, try different!", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice, name, contact, desc) values(?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get("1.0", END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = (self.supplierTable.item(f))
        row = content['values']
        if row:
            self.var_sup_invoice.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.txt_desc.delete('1.0', END)
            self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. Must be Required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.!", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?, contact=?, desc=? where invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get("1.0", END),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice no. Must be Required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.!", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirmation", "Do you really want to delete it?", parent=self.root)
                    if op:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Details Deleted Successfully!", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice LIKE ?", ('%' + self.var_searchtxt.get() + '%',))
                rows = cur.fetchall()
                if rows:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
