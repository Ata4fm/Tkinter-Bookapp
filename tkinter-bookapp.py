from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3 as db


def add_data():
    con = db.connect("C://Users//Reza//Desktop//py//mydb.db")
    cursor = con.cursor()
    cursor.execute("create table if not exists book(title text primary key,author text,year int,isbn text)")
    n = title_textbox.get()
    a = author_textbox.get()
    y = year_textbox.get()
    isb = isbn_textbox.get()
    if n and a and y and isb:
        cursor.execute(f"insert into book values('{n}','{a}',{y},'{isb}')")
        messagebox.showinfo("موفقيت", "با موفقيت ثبت شد")
        con.commit()
        con.close()
    else:
        messagebox.showwarning("خطا", "لطفا فيلد هارا وارد کنيد")


def show_data():
    w.delete(0, END)
    con = db.connect("C://Users//Reza//Desktop//py//mydb.db")
    cursor = con.cursor()
    cursor.execute("select * from book")
    info = cursor.fetchall()
    for i in info:
        w.insert(END, i)
    con.commit()
    con.close()


def search_data():
    w.delete(0, END)
    list = []
    con = db.connect("C://Users//Reza//Desktop//py//mydb.db")
    cursor = con.cursor()
    n = title_textbox.get()
    if n:
        info = cursor.execute("select * from book").fetchall()
        for data in info:
            list.append(data[0])
        if n in list:
            cursor.execute(f"select * from book where title='{n}'")
            info = cursor.fetchall()
            for i in info:
                w.insert(END, i)
            con.commit()
            con.close()
        else:
            messagebox.showwarning("خطا", "اين کتاب پيدا نشد!")

    else:
        messagebox.showwarning("خطا", "لطفا براي جستجو نام را وارد کنيد")


def delete_data():
    w.delete(0, END)
    list = []
    con = db.connect("C://Users//Reza//Desktop//py//mydb.db")
    cursor = con.cursor()
    n = title_textbox.get()
    if n:
        info = cursor.execute("select * from book").fetchall()
        for data in info:
            list.append(data[0])
        if n in list:
            cursor.execute(f"delete from book where title='{n}'")
            con.commit()
            con.close()
            messagebox.showinfo("موفقيت آميز", f"با موفقيت {n} کتاب حذف شد")

        else:
            messagebox.showwarning("خطا", "اين کتاب پيدا نشد!")
    else:
        messagebox.showwarning("خطا", "ابتدا نام کتاب را وارد کنيد")


def btn_close():
    root.destroy()


root = Tk()
root.geometry("550x250")
root.resizable(height=False, width=False)

title_label = Label(root, text="نام کتاب: ").place(x=10, y=20)
title_textbox = Entry(root)
title_textbox.place(x=80, y=20)

author_label = Label(root, text="نام نويسنده: ").place(x=220, y=20)
author_textbox = Entry(root)
author_textbox.place(x=300, y=20)

year_label = Label(root, text="سال انتشار: ").place(x=10, y=50)
year_textbox = Entry(root)
year_textbox.place(x=80, y=50)

isbn_label = Label(root, text="ISBN: ").place(x=220, y=50)
isbn_textbox = Entry(root)
isbn_textbox.place(x=300, y=50)

w = Listbox(root, width=65, )
w.place(x=10, y=80)

btn_add = Button(root, text="اضافه کردن", command=add_data, width=10)
btn_add.place(x=450, y=20)

btn_show = Button(root, text="مشاهده کردن", command=show_data, width=10)
btn_show.place(x=450, y=60)

btn_search = Button(root, text="جستجو", command=search_data, width=10)
btn_search.place(x=450, y=100)

btn_search = Button(root, text="حذف", command=delete_data, width=10)
btn_search.place(x=450, y=140)

btn_close = Button(root, text="بستن", command=btn_close, width=10)
btn_close.place(x=450, y=180)

root.mainloop()



