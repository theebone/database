from tkinter import *

import psycopg2
from psycopg2 import pool

root = Tk()
root.title("Škola a databáze")
root.geometry("300x280")
root.resizable(False,False)

db_pool = pool.SimpleConnectionPool(1,10,   
                                    dbname="student",
                                    user="postgres",
                                    password="neřeknu",
                                    host="localhost",
                                    port="5432")
#fce
def create_table():
    with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE if NOT EXISTS teacher(
                ID SERIAL,
                NAME TEXT,
                AGE INT,
                ADDRESS TEXT
    )""")
            conn.commit()
        db_pool.putconn(conn)



def insert_data(name, age, address):
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_address.delete(0, END)

    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            query = """INSERT INTO teacher(name, age, address) VALUES(%s, %s, %s)"""
            cur.execute(query, (name, age, address))
            conn.commit()
    finally:
        db_pool.putconn(conn)
    
    display_all()

def search(id):
     with db_pool.getconn() as conn:
        with conn.cursor() as cur:
            query = """select * from teacher where id =%s"""
            cur.execute(query,(id,))
            row = cur.fetchone()
            if row:
                display_search(row)
            else:
                display_search("ID nenalezeno")
        db_pool.putconn(conn)
            
def display_search(data):
    listbox = Listbox(root,width=20,height=1)
    listbox.grid(row=8,column=1)
    listbox.insert(0,data)

def display_all():
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cur:
            query = """SELECT * FROM teacher"""
            cur.execute(query)
            all_data = cur.fetchall()

            listbox = Listbox(root, width=25, height=5)
            listbox.grid(row=9, column=1)

            scrollbar = Scrollbar(root)
            scrollbar.grid(row=9, column=2, sticky="nsw")
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            for one_row in all_data:
                listbox.insert(0, one_row)
    finally:
        db_pool.putconn(conn)


create_table()
display_all()








label_general = Label(root,text="Add data")
label_general.grid(row=0,column=1)

label_name = Label(root,text="Name: ")
label_name.grid(row=1,column=0)
#jména
entry_name = Entry(root)
entry_name.grid(row=1,column=1)
#věk
label_age = Label(root,text="Age: ")
label_age.grid(row=2,column=0)

entry_age = Entry(root)
entry_age.grid(row=2,column=1)
#adresa
label_address = Label(root,text="Address: ")
label_address.grid(row=3,column=0)

entry_address = Entry(root)
entry_address.grid(row=3,column=1)

#tlačítka

button = Button(root,text="Add",command=lambda:insert_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

#vyhledavání

label_search = Label(root,text="search data: ")
label_search.grid(row=5,column=1)
label_id = Label(root,text="search by ID: ")
label_id.grid(row=6,column=0)

entry_id = Entry(root)
entry_id.grid(row=6,column=1)

button_search = Button(root,text="Search",command=lambda:search(entry_id.get()) if entry_id.get().strip()else None)
button_search.grid(row=6,column=2)






root.mainloop()