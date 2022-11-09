from calendar import Calendar
# from calendar import Calendar, DateEntry
import subprocess
from tkinter import *
import tkinter
from tkinter.font import BOLD
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3,os
from tokenize import String
from typing import ValuesView
# from feein import feein,prints
# from tkcalender import Calender
global newadm
global said,sname,sphnno,semail,scourse,sdate
global view,lab,w1,btn_log11

# newadm=Tk()
def onclicklogout(z):
    if z ==1:
        dashboard.destroy()
        subprocess.call(["python", "login.py"])
    if z==2:
        newadm.destroy()
        subprocess.call(["python", "login.py"])
    if z==3:
        # feein.destroy()
        subprocess.call(["python", "login.py"])
    if z==4:
        # prints.destroy()
        subprocess.call(["python", "login.py"])
    if z==5:
        view.destroy()
        subprocess.call(["python", "login.py"])

def onclickadd():
    conn = sqlite3.connect("class.db")
    cursor = conn.cursor()
    #creating New User table
    cursor.execute("CREATE TABLE IF NOT EXISTS studinfo (sid INTEGER PRIMARY KEY  NOT NULL, sname TEXT, sphnno TEXT, semail TEXT,scourse TEXT,sdate TEXT)")
    said1=said.get()
    sname1=sname.get()
    sphnno1=sphnno.get()
    semail1=semail.get()
    scourse1=scourse.get()
    sdate1=sdate.get()
    
    if said1=='' or sname1==''or sphnno1=='' or semail1=='' or scourse1=='' or sdate1=='':
        tkMessageBox.showinfo("Warning","All fields are Mandatory . . .")
    elif (sphnno1.isdigit()) :
        if (len(sphnno1)==10):
            special_ch=['-']
            if (len(sdate1)!=10):
                msg = ' Date Format  " dd/mm/yyyy"'
                tkMessageBox.showinfo('Warning', msg)

            elif not any(ch in special_ch for ch in sdate1):
                msg = ' Date Format  " dd-mm-yyyy"'
                tkMessageBox.showinfo('Warning', msg)
                   
            else:      
                    d=0
                    cursor.execute('SELECT * FROM studinfo')
                    check = cursor.fetchall()
                        
                    for i in check:
                        # # print(i[0])
                        # print(i)
                        p=i[0]
                        # print(aid1,p)
                        if (str(said1)== str(p)):
                            
                            msg='Student Already Exist'
                            tkMessageBox.showinfo('Warning', msg)
                            # print('Invaliddd')
                            d=1
                    if d!=1:
                        conn.execute('INSERT INTO studinfo (sid,sname,sphnno,semail,scourse,sdate)  VALUES (?,?,?,?,?,?)',(said1,sname1,sphnno1,semail1,scourse1,sdate1));
                        conn.commit()
                        # print('hi444')
                        msg="Stored successfully"   
                        said.set('')
                        sphnno.set('') 
                        sname.set('')
                        semail.set('')
                        scourse.set('')
                        sdate.set('') 
                        tkMessageBox.showinfo('Warning', msg)

                            
        else:
            tkMessageBox.showinfo("Warning","Phone Number should be of 10 digits . . .")    

            
    else:
      tkMessageBox.showinfo("Warning","Incorrect Format . . .")

def onclickfee(x):
    # print(x)
    if x==1:
            newadm.destroy()
        # print('jhio'/)
            subprocess.call(["python", "feein.py"])

    elif x==2:
            view.destroy()
            subprocess.call(["python", "feein.py"])

    else :
            dashboard.destroy()
            subprocess.call(["python", "feein.py"])
def onselect():
    lab.destroy()
    w1.destroy()
    btn_log11.destroy()
    s = ttk.Style()
    s.theme_use('clam')

    # Configure the style of Heading in Treeview widget
    s.configure('Treeview.Heading', background="#F0FFFF")

    tree = ttk.Treeview(view, column=("c1", "c2", "c3","c4"), show='headings')

    tree.column("#1", anchor=tkinter.CENTER)

    tree.heading("#1", text="Student Id")

    tree.column("#2", anchor=tkinter.CENTER)

    tree.heading("#2", text="Student Name")

    tree.column("#3", anchor=tkinter.CENTER)

    tree.heading("#3", text="Student Phone No")
    tree.column("#4", anchor=tkinter.CENTER)

    tree.heading("#4", text="Student Admission Date")

    tree.place (x=350,y=150)

    tree.tag_configure('t1',background='black')

    sea=scourse1.get()
    conn = sqlite3.connect("class.db")
    cursor = conn.cursor()
    d=0
    cursor.execute('SELECT sid,sname,sphnno,sdate FROM studinfo where scourse = (?)', (sea,))
    check = cursor.fetchall()

    for record in check:
        tree.insert("", END, values=record)
def dummy():
    view.destroy()
    subprocess.call(["python", "test.py"])


def onclickview(z):
    # print("vd",z)
    if z==0:
        newadm.destroy()
        global view,lab,w1,btn_log11,scourse1
        view=Tk()
        view.geometry("1200x600+270+50")
        view.config(background="#F0FFFF")
        view.title("View Records")
        newcan=Canvas(view,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(view, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        lab=Label(view, text="Enter Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black")
        lab.place(x=340,y=140)
        scourse1=StringVar(view)
        scourse1.set("CCC") 
        w1 = OptionMenu(view, scourse1, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w1.config(bg='#F0FFFF',fg='black',font=("Arial", 16,BOLD))
        w1.place(x=590,y=140)


        btn_log11 = Button(view, text="View Records", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onselect)
        btn_log11.place(x=610,y=250)
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(view, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=dummy)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(view, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=160)
        btn_logout = Button(view, text="View Students",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(view, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(5))
        btn_logout.place(x=116,y=560)
    if z==1:
        newadm.destroy()
        # global view
        view=Tk()
        view.geometry("1200x600+270+50")
        view.config(background="#F0FFFF")
        view.title("View Records")
        newcan=Canvas(view,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(view, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        lab=Label(view, text="Enter Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black")
        lab.place(x=340,y=140)
        scourse1=StringVar(view)
        scourse1.set("CCC") 
        w1 = OptionMenu(view, scourse1, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w1.config(bg='#F0FFFF',fg='black',font=("Arial", 16,BOLD))
        w1.place(x=590,y=140)


        btn_log11 = Button(view, text="View Records", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onselect)
        btn_log11.place(x=610,y=250)      
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(view, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=dummy)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(view, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=160)
        btn_logout = Button(view, text="View Students",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(view, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(5))
        btn_logout.place(x=116,y=560)
    else:
        
        view=Tk()
        view.geometry("1200x600+270+50")
        view.config(background="#F0FFFF")
        view.title("View Records")
        newcan=Canvas(view,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(view, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        lab=Label(view, text="Enter Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black")
        lab.place(x=340,y=140)
        scourse1=StringVar(view)
        scourse1.set("CCC") 
        w1 = OptionMenu(view, scourse1, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w1.config(bg='#F0FFFF',fg='black',font=("Arial", 16,BOLD))
        w1.place(x=590,y=140)


        btn_log11 = Button(view, text="View Records", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onselect)
        btn_log11.place(x=590,y=250)
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(view, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=dummy)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(view, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=160)
        btn_logout = Button(view, text="View Students",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(view, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(view, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(5))
        btn_logout.place(x=116,y=560)
        view.mainloop()
    
def onclicknewstud(y):
    # print('hi')
    # newadm.destroy()
    # dashboard.destroy()
    if y==1:
        dashboard.destroy()
        global newadm
        newadm=Tk()
        newadm.geometry("1200x600+270+50")
        newadm.config(background="#F0FFFF")
        newadm.title("New Admission")
        newcan=Canvas(newadm,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(newadm, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        global said,sname,sphnno,semail,scourse,sdate
        said=StringVar()
        sname=StringVar()
        sphnno=StringVar()
        semail=StringVar()
        scourse=StringVar(newadm)
        sdate=StringVar()
        Label(newadm, text="Enter Student Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=100)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=said).place(x=590,y=100)
        Label(newadm, text="Enter Student Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=160)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sname).place(x=590,y=160)
        Label(newadm, text="Enter Student Phone No  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=220)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=sphnno).place(x=590,y=220)
        Label(newadm, text="Enter Student Email id ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=280)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=semail).place(x=590,y=280)
        Label(newadm, text="Enter Student's Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=340)
        scourse.set("CCC") 
        w = OptionMenu(newadm, scourse, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w.config(bg='#F0FFFF',fg='black',font=("Arial", 16,"bold"))
        w.place(x=590,y=340)
        Label(newadm, text="Enter Admission Date ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=400)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sdate).place(x=590,y=400)
        # cal = Date/ady=20)
        # cal = Calendar(root, selectmode='day',
        #                year=2020, month=5,
        #                day=22)

        # cal.pack(pady=20)

        btn_log = Button(newadm, text="Add", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onclickadd)
        btn_log.place(x=610,y=480)
        
        
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(newadm, text="New Admission",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(newadm, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=lambda:onclickfee(1))
        btn_logout.place(x=70,y=160)
        btn_logout = Button(newadm, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(newadm, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(2))
        btn_logout.place(x=116,y=560)
    elif y==2:
        # print("r4df",y)
        view.destroy()
        # global newadm
        newadm=Tk()
        newadm.geometry("1200x600+270+50")
        newadm.config(background="#F0FFFF")
        newadm.title("New Admission")
        newcan=Canvas(newadm,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(newadm, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        # global said,sname,sphnno,semail,scourse,sdate
        said=StringVar()
        sname=StringVar()
        sphnno=StringVar()
        semail=StringVar()
        scourse=StringVar(newadm)
        sdate=StringVar()
        Label(newadm, text="Enter Student Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=100)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=said).place(x=590,y=100)
        Label(newadm, text="Enter Student Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=160)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sname).place(x=590,y=160)
        Label(newadm, text="Enter Student Phone No  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=220)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=sphnno).place(x=590,y=220)
        Label(newadm, text="Enter Student Email id ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=280)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=semail).place(x=590,y=280)
        Label(newadm, text="Enter Student's Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=340)
        scourse.set("CCC") 
        w = OptionMenu(newadm, scourse, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w.config(bg='#F0FFFF',fg='black',font=("Arial", 16,"bold"))
        w.place(x=590,y=340)
        Label(newadm, text="Enter Admission Date ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=400)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sdate).place(x=590,y=400)
        # cal = Date/ady=20)
        # cal = Calendar(root, selectmode='day',
        #                year=2020, month=5,
        #                day=22)

        # cal.pack(pady=20)

        btn_log = Button(newadm, text="Add", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onclickadd)
        btn_log.place(x=610,y=480)
        
        
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(newadm, text="New Admission",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(newadm, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=lambda:onclickfee(1))
        btn_logout.place(x=70,y=160)
        btn_logout = Button(m=newadm, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(newadm, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(2))
        btn_logout.place(x=116,y=560)
    else:
        
        newadm=Tk()
        newadm.geometry("1200x600+270+50")
        newadm.config(background="#F0FFFF")
        newadm.title("New Admission")

        newcan=Canvas(newadm,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(newadm, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        lbl_text.pack(fill=X)
        said=StringVar()
        sname=StringVar()
        sphnno=StringVar()
        semail=StringVar()
        scourse=StringVar(newadm)
        sdate=StringVar()
        Label(newadm, text="Enter Student Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=100)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=said).place(x=590,y=100)
        Label(newadm, text="Enter Student Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=160)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sname).place(x=590,y=160)
        Label(newadm, text="Enter Student Phone No  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=220)
        Entry(newadm,font=("Arial",16,"bold"),textvariable=sphnno).place(x=590,y=220)
        Label(newadm, text="Enter Student Email id ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=280)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=semail).place(x=590,y=280)
        Label(newadm, text="Enter Student's Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=340)
        scourse.set("CCC") 
        w = OptionMenu(newadm, scourse, "CCC", "Tally", "DTP","Adv.Excell","Hardware","Networking","Java",".Net","Typing","DCA","C/C++","Web Designing")
        w.config(bg='#F0FFFF',fg='black',font=("Arial", 16,"bold"))
        w.place(x=590,y=340)
        Label(newadm, text="Enter Admission Date ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=400)
        Entry(newadm, font=("Arial", 16,"bold"),textvariable=sdate).place(x=590,y=400)
        # cal = Date/ady=20)
        # cal = Calendar(root, selectmode='day',
        #                year=2020, month=5,
        #                day=22)

        # cal.pack(pady=20)

        btn_log = Button(newadm, text="Add", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onclickadd)
        btn_log.place(x=610,y=480)
        
        
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(newadm, text="New Admission",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(newadm, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=lambda:onclickfee(1))
        btn_logout.place(x=70,y=160)
        btn_logout = Button(newadm, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(newadm, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(newadm, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(2))
        btn_logout.place(x=116,y=560) 
        newadm.mainloop()

    
def onclickdashboard():
    global dashboard
    # global #
    dashboard=Tk()
    dashboard.geometry("1200x600+270+50")
    dashboard.config(background="#F0FFFF")
    dashboard.title("Dashboard")
    dashcan=Canvas(dashboard,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
    lbl_text = Label(dashboard, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
    width=600,bg="#00FFFF")
    lbl_text.pack(fill=X)
    # = Frame(dashboard).pack()
    
    bg1 = PhotoImage(file = "dash.png")
    label1 = Label( dashboard, image = bg1)
    label1.place(x = 303, y = 110)
    Label(dashboard, text="Loc : Dombivli West ", font=("Arial", 15),bg="#F0FFFF",fg="black").place(x=793,y=530)
    Label(dashboard, text="Contact :  +91 8104583778", font=("Arial", 12,BOLD),bg="#F0FFFF",fg="black").place(x=793,y=560)
    
    btn_logout = Button(dashcan, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogout)
    btn_logout.place(x=116,y=560)
    btn_logout = Button(dashcan, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=lambda:onclicknewstud(1))
    btn_logout.place(x=70,y=100)
    btn_logout = Button(dashcan, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=70,y=160)
    btn_logout = Button(dashcan, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=76,y=280)
    btn_logout = Button(dashcan, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=76,y=220)
    btn_logout = Button(dashcan, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onclicklogout(1))
    btn_logout.place(x=116,y=560)
    dashboard.mainloop()
    
    
    
    
# onclickdashboard()