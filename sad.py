from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from tkinter import *
main_window=Tk()
def login():
    e1=entry1.get()
    e2=entry2.get()
    f = open("aun1.txt", "r")
    c = f.readlines()

    f.close()
    if  c[0]==e1 and c[1]==e2:
        tkMessageBox.showerror("error", "you logged in ")
    else:
        tkMessageBox.showerror("error", "there is issue with some information")


def sign_up():
    e1 = entry1.get()
    e2 = entry2.get()
    f=open("aun1.txt","a")
    f.writelines(e1)
    f.writelines('\n')
    f.writelines(e2)
    f.close()
    pass
main_window.geometry("1500x1500")
l1=Label(main_window,text="enter email ".capitalize(),font="lucida  36 bold ",width=15,fg="black",bg="light green").place(x=10,y=10)
l2=Label(main_window,text="enter pasword".capitalize(),font="lucida  36 bold ",width=15,fg="black",bg="light green").place(x=10,y=100)
entry1 = Entry(main_window,  width=20,bg="light green",fg="black",font="Times 36 bold")
entry1.place(x=400,y=10)
entry2 = Entry(main_window,  width=20,bg="light green",fg="black",font="Times 36 bold")
entry2.place(x=400,y=100)
btn_add = Button(main_window, width=10, text="login", command=login, bg="light blue",fg='black', font=("Times bold",36))
btn_add.place(x=10,y=200)
btn_view = Button(main_window, width=20, text="create account", command=sign_up, bg="light blue",fg='black', font=("Times bold",36))
btn_view.place(x=250,y=200)



main_window.mainloop()