import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aayush@1172004",
    database="EventManagement"
)

root = tkinter.Tk()
root.title("Login")
Label(root, text="UserId").grid(row=0, column=0)
Label(root, text="Password").grid(row=1, column=0)
userid = Entry(root)
userid.grid(row=0, column=1)
userpass = Entry(root, show="*")
userpass.grid(row=1, column=1)


def loginuser(value):
    print(value)
    if value == 1:
        print(value)
        mycur = mydb.cursor()
        uid = userid.get()
        password = userpass.get()

        sql = "select * from Emplogin where empId=%s and empPass=%s"
        mycur.execute(sql, [uid, password])
        res = mycur.fetchall()
        if res:
            messagebox.showinfo("login alert", "Employee login successful")
            openemp(uid)

        else:
            messagebox.showinfo("login alert", "Incorrect credentials")

    elif value == 2:
        print(value)
        mycur1 = mydb.cursor()
        uid = userid.get()
        password = userpass.get()

        sql = "select * from custlogin where custId=%s and custPass=%s"
        mycur1.execute(sql, [uid, password])
        res = mycur1.fetchall()
        if res:
            messagebox.showinfo("login alert", "Customer login successful")
            openemp(uid)

        else:
            messagebox.showinfo("login alert", "Incorrect credentials")
    else:
        messagebox.showwarning("Missing", "Something is missing\nTry Again")

def newCust():
    mycur = mydb.cursor()
    newcust = tkinter.Tk()
    Label(newcust, text="Name").grid(row=0, column=0)
    Label(newcust, text="Id").grid(row=1, column=0)
    Label(newcust, text="Email").grid(row=2, column=0)
    Label(newcust, text="Set Password").grid(row=3, column=2)
    custname = Entry(newcust)
    custname.grid(row=0, column=1)
    cid = IntVar(custname, id(custname))
    custid = Entry(newcust, textvariable=cid)
    custid.grid(row=1, column=1)
    custmail = Entry(newcust)
    custmail.grid(row=2, column=1)
    custpass=Entry(newcust)
    custpass.grid(row=3, column=1)


    def subcust():
        mycur.execute("insert into Customer(custName, custId, custEmail) values(%s,%s,%s)", (custname.get(), custid.get(), custmail.get()))
        mycur.execute("insert into custlogin(custId, custPass) values(%s,%s)", (custid.get(), custpass.get()))
        mydb.commit()
        messagebox.showinfo("Customer", "Yippee\nCustomer Added successfully")
        newcust.destroy()

    def delcust():
        mycur.execute("delete from customer where custID = %s", [custid.get()])
        mycur.execute("delete from custlogin where custID = %s", [custid.get()])
        mydb.commit()
        messagebox.showinfo("Customer", "Customer Removed")
        newcust.destroy()
        return 0

    Button(newcust, text="Delete", command=delcust).grid(row=4, column=0)
    Button(newcust, text="Add", command=subcust).grid(row=4, column=1)

def openemp(val):
    root.destroy()
    emp = tkinter.Tk()
    emp.title("Employee")
    Label(emp, text="WELCOME", fg="red", font=153).pack()
    mycur1 = mydb.cursor()
    sql1 = "select empName,empId from Employee where empId=%s"
    mycur1.execute(sql1, [val])
    res1 = mycur1.fetchall()
    dres = ''
    for rec in res1[0]:
        dres += str(rec) + "  "

    Label(emp, text=dres).pack()
    Button(emp, text="Manage Customer", command=newCust).pack()

def manageEvent():
    return 0

def opencust(val):
    root.destroy()
    cust = tkinter.Tk()
    cust.title("Customer")
    Label(cust, text="WELCOME", fg="red", font=153).pack()
    mycur1 = mydb.cursor()
    sql1 = "select custName,custId from Customer where custId=%s"
    mycur1.execute(sql1, [val])
    res1 = mycur1.fetchall()
    dres = ''
    for rec in res1[0]:
        dres += str(rec) + "  "

    Label(cust, text=dres).pack()
    Button(cust, text="Manage Event", command=manageEvent).pack()

v = IntVar()

Radiobutton(root, text="Employee", variable=v, value=1).grid(row=2, column=0)
Radiobutton(root, text="Customer", variable=v, value=2).grid(row=2, column=1,)
Button(root, text="Forget credentials").grid(row=3, column=0)
Button(root, text="Login", command=lambda: loginuser(v.get())).grid(row=3, column=1)
root.mainloop()
