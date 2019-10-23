from tkinter import *
from tkinter import  simpledialog
import sqlite3
import threading
import time
label=None
def exit_app():
    root.destroy()
def get_me1():
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    name=simpledialog.askstring("Имя","plese enter")
    sorname = simpledialog.askstring("Фамилия", "plese enter")
    phone = simpledialog.askstring("ТЕЛЕФОН", "plese enter")
    data=[name,sorname,phone]
    cursor.execute('INSERT INTO users(name,surname,phone) VALUES(?,?,?)', data)
    con.commit()
    cursor.close()
def get_me2():
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    name = simpledialog.askstring("Имя", "please enter")
    select = """SELECT id, name, surname, phone
                FROM users
                WHERE name = '{0}' 
                """
    cursor.execute(select.format(name))
    results=cursor.fetchall()
    global label
    root=Tk()
    label=Label(root,text=results)
    label.pack()
    root.mainloop()

    print(results)


    row = cursor.fetchone()

    second_item.add_cascade(label=results)



    row=cursor.fetchone()

    con.commit()
    cursor.close()

def get_me3():
        con = sqlite3.connect('users.db')
        cursor = con.cursor()
        surname = simpledialog.askstring("Фамилия", "please enter")
        select = """SELECT id, name, surname, phone
                FROM users
                WHERE surname = '{0}' 
                """
        cursor.execute(select.format(surname))

        results=cursor.fetchall()
        global label
        root = Tk()
        label = Label(root, text=results)
        label.pack()
        root.mainloop()
        print(results)
        con.commit()
        cursor.close()
def get_me4():
    con = sqlite3.connect('users.db')
    cursor = con.cursor()
    phone = simpledialog.askinteger("Телефон", "please enter")
    select = """SELECT id, name, surname, phone
                FROM users
                WHERE phone = '{0}' 
                """
    cursor.execute(select.format(phone))
    results=cursor.fetchall()
    global label
    root = Tk()
    label = Label(root, text=results)
    label.pack()
    root.mainloop()
    print(results)
    row = cursor.fetchone()

    con.commit()
    cursor.close()

root=Tk()
main_menu=Menu(root)
root.configure(menu=main_menu)
first_item=Menu(main_menu)
main_menu.add_cascade(label="Создать контакт",command=get_me1)
#main_menu.add_cascade(label="Найти контакт",menu=first_item)
main_menu.add_cascade(label="Отредактировать контакт")
main_menu.add_cascade(label="Удалить контакт")
main_menu.add_cascade(label="Выйти из программы ",command=exit_app)
second_item= Menu(main_menu)
main_menu.add_cascade(label="Найти контакт",menu=second_item)
second_item.add_cascade(label="По имени",command=get_me2)
second_item.add_cascade(label="По фамилии",command=get_me3)
second_item.add_cascade(label="По телефону",command=get_me4)

root.mainloop()