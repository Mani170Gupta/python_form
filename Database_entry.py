from tkinter import *
import mysql.connector
root = Tk()
root.title("Fill out the form")
root.geometry('500x500')

con = mysql.connector.connect(host ='localhost', user ='root', password ='root',database ='registration')
cur = con.cursor(buffered = True)
try:
    cur.execute('use registration')# this is use database(name of database as registration)
except:
    cur.execute('create database registration')
    cur.execute('use registration')
try:
    cur.execute('describe persons')
except:
    cur.execute('CREATE TABLE persons (id int primary key auto_increment, name varchar(20), age int(4), mobile int(13), email varchar(30), gender varchar(10))')

def registration():
    name = e1.get()
    age = e2.get()
    mobile = e3.get()
    email = e4.get()
    gender = e5.get()

    sql = "INSERT INTO persons (name, age, mobile, email, gender) VALUES (%s, %s, %s, %s, %s)"
    val = (name, age, mobile, email, gender)
    cur.execute(sql, val)
    con.commit()

l0 = Label(root, text = 'Enter the details', font = 'canvas 13 bold').grid(row = 0, column = 14)
l1 = Label(text = 'Name')
l1.grid(row = 1, column = 0)

l2 = Label(text = 'Age')
l2.grid(row = 2, column = 0)
l3 = Label(text = 'Mobile')
l3.grid(row = 3, column = 0)
l4 = Label(text = 'Email')
l4.grid(row = 4, column = 0)
l5 = Label(text = 'Gender')
l5.grid(row = 5, column = 0)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e1.grid(row = 1, column = 2)
e2.grid(row = 2, column = 2)
e3.grid(row = 3, column = 2)
e4.grid(row = 4, column = 2)
e5.grid(row = 5, column = 2)
Button(root, text = 'Submit', command = registration).grid(column = 1)





root.mainloop()