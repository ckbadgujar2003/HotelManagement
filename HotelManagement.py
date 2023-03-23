from tkinter import *
from tkinter import messagebox
import datetime
from time import strftime
import sqlite3


#Database connection
con = sqlite3.connect('customerdet.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS HotelManagement(CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,TableNo "
            "INTEGER,Menu TEXT,TotalBill INTEGER)")


#functions
def newBill():
    user = custidentry.get()
    table = entrytable.get()
    newMenu = display.get(1.0, "end-1c")
    newTotalBill = totalcost.get()

    cur.execute("SELECT COUNT(*) from HotelManagement WHERE CustomerID=' " + user + "'")
    result = cur.fetchone()

    try:
        if int(result[0]) > 0:
            messagebox.showerror("Customer ID exists already")
        else:

            cur.execute("INSERT INTO HotelManagement(CustomerID,table_no,menu,TotalBill) VALUES(?,?,?,?)",
                        (user, table, newMenu, newTotalBill))
            con.commit()
            messagebox.showinfo("added data successfully")
    except:
        print('Enter Customer ID and Table number')

def time():
    string = strftime('%H:%M:%S')
    timelabel.config(text=string, bg='black', fg='white')
    timelabel.after(1000, time)

def displayitem(menu):
    item = menu.split("-")
    display.insert(END, "{} {}\n".format(item[0], item[1]))
    c = item[1].split()

    global total
    total = total + int(c[1])
    print(total)

def totalbill():
    totalcost.insert(0,"rs {}/-".format(total))

    # sum_digit=0
    # res = []
    # for x in y:
    #     if x.isnumeric() == True:
    #         res.append(x)
    #         print(res)
    #         res = str(res)
    #         res = int(float(res))
    #         # total = sum(res)
    #         # z = int(x)
    #         # print(z)
    #         # sum_digit=sum_digit+z
    #         k.set(total)

# def show():
# 	display.config( text = menu.get() )
#
# def add():
#     con = sqlite3.connect('menu.db')
#     cur = con.cursor()
#
#     cur.execute('SELECT Dish FROM MenuCard WHERE Dish = "CHINESE BHEL"')
#     print(cur.fetchone())
#     display.config(text=cur.fetchone())


#Main Window
window = Tk()
window.title("MAMA DA DHABA")
window.geometry("920x700")

mainframe = Frame(window, relief=RIDGE, width=460, height= 288)
mainframe.grid(row=0, column=0, columnspan=2)
title = Label(mainframe, text="               MAMA DA DHABA               ", relief=GROOVE, borderwidth=5, font=('Copperplate Gothic Bold', 40), bg='gray', fg='white', justify=CENTER)
title.pack()


#Menu Frame
menuframe = Frame(window, border=3, background='black', relief=RIDGE)
menuframe.grid(row=1, column=0)
space = Label(menuframe, text='    ', justify=RIGHT, bg='black').grid(row=0, column=1, columnspan=2)
menulabel = Label(menuframe, text="           MENU           ", font=('Copperplate Gothic Bold', 20), bg='black', fg='white')
menulabel.grid(row=1, column=0,pady=5)
space = Label(menuframe, text="                      ", bg='black').grid(row=2, column=0)
menu = StringVar()
menu.set("PLACE YOUR ORDER")
menucard = [
    "CHINESE BHEL              - RS. 50",
    "HAKKA NOODLE              - Rs. 70",
    "SCHEZWAN NOODLE           - Rs. 80",
    "VEG MANCHURIAN            - Rs. 60",
    "CHICKEN MANCHURIAN        - Rs. 70",
    "TRIPLE SCHEZWAN FRIED RICE- Rs. 90",
    "EGG RICE                  - Rs. 90"
]


drop = OptionMenu(menuframe, menu, *menucard, command=displayitem).grid(row=3, column=0)
space = Label(menuframe, text='    ', justify=RIGHT, bg='black').grid(row=4, column=1, columnspan=2)
add = Button(menuframe, text='Add', command=newBill).grid(row=5, column=0, columnspan=2)


#Billing Frame
billframe = Frame(window, relief=RIDGE, border=3, background='black', width=460, height=576)
billframe.grid(row=1, column=1, rowspan=2)
space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=0, column=1, columnspan=2)

billdetail = Label(billframe, text="BILLING  DETAILS", font=('Copperplate Gothic Bold', 20), bg='black', fg='white')
billdetail.grid(row=1, column=0, columnspan=2)
space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=2, column=0, columnspan=2)

custid = Label(billframe, text=' ENTER CUSTOMER ID ', justify=LEFT)
custid.grid(row=3, column=0, padx=17)
cust = StringVar()
custidentry = Entry(billframe, textvariable=cust)
custidentry.grid(row=4, column=0, padx=17)

tableno = Label(billframe, text=' ENTER TABLE NO. ', justify=LEFT).grid(row=3, column=1, padx=25)
tab = StringVar()
entrytable = Entry(billframe, textvariable=tab, width=17)
entrytable.grid(row=4, column=1, padx=17)

space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=5, column=1, columnspan=2, padx=17)
display = Text(billframe, fg='black', width=34, height=20)
display.grid(row=6, column=0, columnspan=2)

space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=7, column=1, columnspan=2, padx=17)
date= datetime.datetime.now()
datelabel = Label(billframe, text=f"{date:%d %B, %Y}", bg='black', fg='white')
datelabel.grid(row=8, column=0, padx=30)
timelabel = Label(billframe)
timelabel.grid(row=8, column=1, padx=30)
time()

space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=9, column=1, columnspan=2)
total = Button(billframe, text='TOTAL:', bg='black', fg='white', command=totalbill)
total.grid(row=10, column=0)
k = StringVar()
total = 0
totalcost = Entry(billframe)
totalcost.grid(row=10, column=1)
space = Label(billframe, text='    ', justify=RIGHT, bg='black').grid(row=11, column=1, columnspan=2)



#Statistics
statsframe = Frame(window, relief=RIDGE, border=3, bg='black')
statsframe.grid(row=2, column=0)
space = Label(statsframe, text='    ', justify=RIGHT, bg='black').grid(row=0, column=0, columnspan=2)
billdetail = Label(statsframe, text="       STATISTICS      ", font=('Copperplate Gothic Bold', 20), bg='black',fg='white').grid(row=1, column=0, columnspan=5)
space = Label(statsframe, text='    ', justify=RIGHT, bg='black').grid(row=2, column=0, columnspan=2)



window.mainloop()
