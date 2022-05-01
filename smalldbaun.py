from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from tkinter import *
# import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os
import tkinter.messagebox
from tkinter.constants import SUNKEN
from PIL import Image,ImageTk
main_window=Tk()
main_window.geometry("1500x500")
def viewitem():
    tree.delete(*tree.get_children())
    mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810", database="aundb1")
    mycur = mydb.cursor()
    mycur.execute("select * from emp0 order by empid desc")
    record=mycur.fetchall()
    n=len(record)
    for i in range(n):
        l1=list(record[i])
        empid_1=l1[0]
        empname_1=l1[1]
        tree.insert("", 0, values=(empid_1,empname_1))



def additem():
    e1 = entry1.get()
    e2 = entry2.get()
    if entry1.get() == "" and entry2.get() == "" :

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")

    else:
        result = tkMessageBox.askquestion("Submit", "You are about to enter following details\n" + entry1.get() + "\n"
                                          + entry2.get() )
        entry1.delete(0, END)
        entry2.delete(0, END)

        if (result == "yes"):
                mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="saymyname@2810", database="aundb1")
                mycur = mydb.cursor()
                sql="insert into emp0(empid,na_me) values (%s,%s)"
                val=(e1,e2)
                mycur.execute(sql,val)
                mydb.commit()
        else:
            print("hello")
            # except Exception as e:
            #     print(e)


        # else:
        #     entry1.set("")
        #     entry2.set("")

emp_id=StringVar()
emp_name=StringVar()
frame = Frame(main_window)

frame.pack(fill=X)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("forest2.jpeg"))

# Create a Label Widget to display the text or Image
label = Label(main_window, image = img)
label.pack()
l1=Label(main_window,text="employe id ".capitalize(),font="lucida  36 bold ",width=15,fg="black",bg="light green").place(x=10,y=10)
l2=Label(main_window,text="employe name".capitalize(),font="lucida  36 bold ",width=15,fg="black",bg="light green").place(x=10,y=100)
entry1 = Entry(main_window,  width=20,bg="light green",fg="black",font="Times 36 bold")
entry1.place(x=400,y=10)
entry2 = Entry(main_window,  width=20,bg="light green",fg="black",font="Times 36 bold")
entry2.place(x=400,y=100)
btn_add = Button(main_window, width=10, text="ADD", command=additem, bg="light blue",fg='black', font=("Times bold",36))
btn_add.place(x=10,y=200)
btn_view = Button(main_window, width=20, text="VIEW DETAILS", command=viewitem, bg="light blue",fg='black', font=("Times bold",36))
btn_view.place(x=250,y=200)









tree=ttk.Treeview(main_window,columns=('employee_id','employee_name'),height=200,)
tree.heading('employee_id', text="employee_id", anchor=W)
tree.heading('employee_name', text="employee_name", anchor=W)
tree.column('#0', stretch=NO, width=0)
tree.column('employee_id', stretch=YES, minwidth=0, width=120)
tree.column('employee_name', stretch=YES, minwidth=0, width=600)
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", font=('Times', 25),
                background='lightcyan1',
                foreground='navy blue',
                rowheight=25,
                fieldbackground='lightcyan',
                )
style.configure('Treeview.Heading', font=("Times",20),
                background='lightcyan2',
                foreground='black',
                rowheight=20)
tree.place(x=800,y=1)
main_window.mainloop()
