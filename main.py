import tkinter as tk
import ttkbootstrap as tb 
import csv
import keyboard
import os
import sys

# ---------- cantidad de textos ------------
count = 0
# ----------- functions -------------------

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        #PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


csvfile = resource_path("tree.csv")

def remove():
    
    x = tree.selection()[0]  

    values = tree.item(x,"values")

    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        rows_keep = [row for row in reader if row[0] != values[0] and values[1] != row[1] and values[2] != row[2]]


    with open(csvfile, "w", newline="") as wrt:
        writer = csv.writer(wrt)
        for row in rows_keep:
            writer.writerow(row)
   
            
    tree.delete(x)

    keyboard.unhook_all()
    with open(csvfile, "r", newline='') as myfile:
        csvreader = csv.reader(myfile, delimiter=',')
        
        for row in csvreader:
             keyboard.add_abbreviation(row[2], row[1])
        


    global count
       
def add():
    global count
    count += 1
    str = "not possible"
    if ne.get() == ''  or te.get() == '' or se.get() == '':
         return str
    tree.insert(parent="",index="end",iid=count,values=(ne.get(),te.get(),se.get()))
    
    ne.delete(0,tk.END)
    te.delete(0,tk.END)
    se.delete(0,tk.END)

    with open(csvfile, "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        
        for row_id in tree.get_children():
            row = tree.item(row_id)['values']
            print('save row:', row)
            csvwriter.writerow(row)
            
    keyboard.unhook_all()
    with open(csvfile, "r", newline='') as myfile:
        csvreader = csv.reader(myfile, delimiter=',')
        
        for row in csvreader:
             keyboard.add_abbreviation(row[2], row[1])      
# --------------------- vetana GUI ------------------------------
window =tb.Window(themename="solar")
window.geometry("600x600")
window.title("Total Keys")
window.attributes("-topmost",True)
window.resizable(width=False, height=True)

icon = resource_path("tk.ico")

window.iconbitmap(icon)

title_label = tk.Label(text="Total Keys", font=("Montserrat medium",36))
title_label.pack(pady=10)

tree = tb.Treeview(window,bootstyle="primary" )
tree['columns'] = ("Name","Text","Shortcut")

tree.column("#0",width=0,stretch=tk.NO)
tree.column("Name",anchor=tk.CENTER,width=140)
tree.column("Text",anchor=tk.CENTER,width=160)
tree.column("Shortcut",anchor=tk.CENTER,width=140)

tree.heading("#0",text="Label",anchor=tk.CENTER)
tree.heading("Name", text="Name",anchor=tk.CENTER)
tree.heading("Text",text="Text",anchor=tk.CENTER)
tree.heading("Shortcut",text="Shortcut",anchor=tk.CENTER)

tree.pack(pady=20)

add_frame = tk.Frame(window)
add_frame.pack(pady=20)
#--------------------------labels ------------------------------------
nl = tk.Label(window, text="Name")
nl.place(x=15,y=390)

tl = tk.Label(window,text="Text")
tl.place(x=212,y=390)

sl = tk.Label(window,text="Shortcut")
sl.place(x=410,y=390)
#--------------------------entrys ------------------------------------
ne = tb.Entry(window,bootstyle = "primary")
ne.place(x=15,y=420)

te = tb.Entry(window,bootstyle = "primary")
te.place(x=212,y=420)

se = tb.Entry(window,bootstyle = "primary")
se.place(x=410,y=420)
#--------------------------button ------------------------------------
add = tb.Button(window,text="Add Shortcut",command=add,bootstyle="success,outline")
add.pack(side = "left",pady=20,padx= 40)

remove = tb.Button(window,text="Remove",command=remove,bootstyle="danger,outline")
remove.pack(side = "left",pady= 20,padx = 10)
#------------------------------ leer csv al inicio del programa para insertar los valores guardados --------------------------------------
with open(csvfile, "r", newline='') as myfile:
        csvreader = csv.reader(myfile, delimiter=',')
        
        for row in csvreader:
             tree.insert(parent="",index="end",iid=count,values=(row[0],row[1],row[2]))
             count += 1
             keyboard.add_abbreviation(row[2], row[1])

window.mainloop()
