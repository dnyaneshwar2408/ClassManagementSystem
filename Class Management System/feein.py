from calendar import Calendar
# from calendar import Calendar, DateEntry
import subprocess
from tkinter import *
from tkinter.font import BOLD
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3,os
from tokenize import String
from dashboard import onclicknewstud, onclickview,onclicklogout
from PIL import ImageGrab

# feein=Tk()
opt=0
p2=0
p4=0
cst=0
p1=0
mon=0
def oncont(pq):
    global opt,cst,mon
    
    opt=int(noin.get())
    ctfl.destroy()
    # #print(pq)
    if pq=="CCC" :
        mon="5 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="12,600", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=12600/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
            
        if opt == 3:
            cst=12600/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=12600/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=12600/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Tally" :
        mon="3 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="9,000", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=9000/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=9000/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=9000/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=9000/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="DTP" :
        mon="2 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="6,300", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=6300/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=6300/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=6300/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=6300/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Adv.Excell" :
        mon="2 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="9,000", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=9000/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=9000/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=9000/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=9000/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Hardware" :
        mon="4 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="16,500", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=16500/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=16500/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=16500/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=16500/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Networking" :
        mon="4 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="12,900", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=12900/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=12900/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=12900/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=12900/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Java" :
        mon="3.5 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="15,000", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=15000/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=15000/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=15000/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=15000/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq==".Net" :
        mon="2.5 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        # emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)("ineeee")
        ctfl1=Label(feein, text="11,700", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=11700/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=11700/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=11700/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=11700/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Typing" :
        mon="5 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="7,500", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=7500/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=7500/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=7500/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=7500/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="DCA" :
        mon="4 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="10,800", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=10800/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=10800/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=10800/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=10800/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="C/C++" :
        mon="5 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="8,400", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=8400/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=8400/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=8400/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=8400/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
    if pq=="Web Designing" :
        mon="2 months"
        Label(feein, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)
        ctfl1=Label(feein, text="13,200", font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=280)
        if opt==2:
            cst=13200/2
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 3:
            cst=13200/3
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 4:
            cst=13200/4
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
        if opt == 5:
            cst=13200/5
            emil=Label(feein, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)

def onlogout(r):
    if r==1:
        feein.destroy()
        onclicklogout(3)
    if r==2:
        prints.destroy()
        onclicklogout(4)
def onclicknewstud1():
    feein.destroy()
    # #print('jhio'/)
    # subprocess.call(["python", "dashboard.py"])
    onclicknewstud(0)
def onsearch():
    global sidse1
    sidse1=sidse.get()
    if(sidse1==''):
        tkMessageBox.showinfo("Warning"," Enter Student Id ")

    else:
                    d=0
                    conn = sqlite3.connect("class.db")
                    cursor = conn.cursor()
                    cursor.execute('SELECT * FROM studinfo')
                    check = cursor.fetchall()
                    global ctf1,p4,w,p2
                    for i in check:
                        # #print(i[0])
                        # #print(i)
                        p=i[0]
                        # #print(sidse1,p)
                        if (str(sidse1)== str(p)):
                            lb1.destroy()
                            e1.destroy()
                            btn_lo1g.destroy()
                            global noin,set,p1
                            noin=StringVar()
                            Label(feein, text="Student Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=100)
                           
                            Label(feein, text="Student Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=160)
                            
                            Label(feein, text="Student's Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=220)
                            
                            Label(feein, text="Course Total Fee", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=280)
                            
                            Label(feein, text="No of  Installment", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=340)
                            # noint=Entry(feein, textvariable=noin, font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=590,y=340)
                            noin.set(" 3 ") 
                            w = OptionMenu(feein, noin, "2","3","4","5")
                            w.config(bg='#F0FFFF',fg='black',font=("Arial", 16,"bold"))
                            w.place(x=590,y=340)
                            Label(feein, text="Per Installment Amount", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=400)
                            
                            Label(feein, text="Course Duration", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=460)
                            


                            cursor.execute('SELECT * FROM studinfo')
                            check = cursor.fetchall()

                            for i in check:
                                # #print(i[0])
                                # #print(i)
                                # global pq
                                p1=i[0]
                                
                                if (str(sidse1)== str(p1)):
                                    p2=i[1]
                                    p4=i[4]
                                    idl=Label(feein, text=p1, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=100)
                                    snl=Label(feein, text=p2, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=160)
                                    scl=Label(feein, text=p4, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=220)
                                    global ctfl
                                    if p4=="CCC" :
                                        set="12,600"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Tally" :
                                        set="9,000"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctf1.place(x=590,y=280)
                                    if p4=="DTP" :
                                        set="6,300"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Adv.Excell" :
                                        set="9,000"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Hardware" :
                                        set="16,500"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Networking" :
                                        set="12,900"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Java" :
                                        set="15,000"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4==".Net" :
                                        set="11,700"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                        
                                        
                                    if p4=="Typing" :
                                        set="7,500"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="DCA" :
                                        set="10,800"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="C/C++" :
                                        set="8,400"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    if p4=="Web Designing" :
                                        set="13,200"
                                        ctfl=Label(feein, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
                                        ctfl.place(x=590,y=280)
                                    
                                btn_log = Button(feein, text="Continue", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=lambda:oncont(p4))
                                btn_log.place(x=610,y=530)
                                    

                                    
                            d=1
                    if d!=1:
                                tkMessageBox.showinfo("Warning"," Student Not Found ")

def onclickview1():
    prints.destroy()
    onclickview(3)   
def onprint():
    ss_region = (360,60,1840,840)
    ss_img = ImageGrab.grab(ss_region)
    
    i=""+ str(p2) +".png"
    ss_img.save(i)

def onclickprint():
    




    if (opt==0 or set==0 or p2==0 or p4==0 or cst==0 or p1==0 or mon ==0):
        # print("00000")
        pass
    else:
        # print("1111111111")
        feein.destroy()
        print(opt,set,p2,p4,cst,p1,mon,sidse1)
        global prints
        prints=Tk()
        prints.geometry("1200x600+270+50")
        prints.config(background="#F0FFFF")
        prints.title("Print Recepit")
        newcan=Canvas(prints,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
        lbl_text = Label(prints, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
        width=600,bg="#00FFFF")
        btn_logout = Button(prints, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0)
        btn_logout.place(x=116,y=560)
        btn_logout = Button(prints, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=100)
        btn_logout = Button(prints, text="Fee Installment",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=70,y=160)
        btn_logout = Button(prints, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=onclickview1)
        btn_logout.place(x=76,y=280)
        btn_logout = Button(prints, text="View Reciept",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
        btn_logout.place(x=76,y=220)
        btn_logout = Button(prints, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onlogout(2))
        btn_logout.place(x=116,y=560)
        lbl_text.pack(fill=X)  



        Label(prints, text="Student Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=100)
                           
        Label(prints, text="Student Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=160)
                            
        Label(prints, text="Student's Course  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=220)
                            
        Label(prints, text="Course Total Fee", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=280)
                            
        Label(prints, text="No of  Installment", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=340)

        Label(prints, text="Per Installment Amount", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=400)
                            
        Label(prints, text="Course Duration", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=340,y=460)

        idl=Label(prints, text=sidse1, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=100)
        snl=Label(prints, text=p2, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=160)
        scl=Label(prints, text=p4, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=220)
        Label(prints, text=opt, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=340)
        Label(prints, text=cst, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=400)
                            
        Label(prints, text=mon, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black").place(x=590,y=460)

        ctfl=Label(prints, text=set, font=("Arial", 16,BOLD),bg="#F0FFFF",fg="black")
        ctfl.place(x=590,y=280)
        btn_log = Button(prints, text="Take Screenshot", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onprint)
        btn_log.place(x=610,y=530)
        prints.mainloop()             
def onclickfee():
    # feein.destroy()
    global feein
    feein=Tk()
    feein.geometry("1200x600+270+50")
    feein.config(background="#F0FFFF")
    feein.title("Fee Installment")
    newcan=Canvas(feein,width=300,height=600,bg='#87CEEB').place(x=0,y=0)
    lbl_text = Label(feein, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
    width=600,bg="#00FFFF")
    btn_logout = Button(feein, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0)
    btn_logout.place(x=116,y=560)
    btn_logout = Button(feein, text="New Admission",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=70,y=100)
    btn_logout = Button(feein, text="Fee Installment",fg="black", bg="silver",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=70,y=160)
    btn_logout = Button(feein, text="View Students",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0)
    btn_logout.place(x=76,y=280)
    btn_logout = Button(feein, text="View Reciept",fg="black", bg="#87CEEB",font=("Arial",16,"bold") ,borderwidth=0,command=onclickprint)
    btn_logout.place(x=76,y=220)
    btn_logout = Button(feein, text="Logout",fg="black", bg="#87CEEB",font=("Arial",12,"bold") ,borderwidth=0,command=lambda:onlogout(1))
    btn_logout.place(x=116,y=560)
    lbl_text.pack(fill=X)



    global sidse,lb1,e1,btn_lo1g
    sidse=StringVar()
    lb1=Label(feein, text="Enter Student id ", font=("Arial", 16),bg="#F0FFFF",fg="black")
    lb1.place(x=340,y=140)
    e1=Entry(feein, font=("Arial", 16,"bold"),textvariable=sidse)
    e1.place(x=590,y=140)

    btn_lo1g = Button(feein, text="Search", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onsearch)
    btn_lo1g.place(x=610,y=250)
    feein.mainloop()

onclickfee()