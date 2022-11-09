import subprocess
from tkinter import *
from tkinter.font import BOLD
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3,os
from tokenize import String
from PIL import Image
from dashboard import *

signtop = Tk()




    



# Backend for signup page                     ........................................
def onclicksignup1():
  aid1=aid.get()
  fname1=fname.get()
  phnno1=phnno.get()
  pwd1=pwd.get()
  global msg 
  msg=''
  if aid1=='' or fname1==''or phnno1=='' or pwd1=='':
      tkMessageBox.showinfo("Warning","All fields are Mandatory . . .")
  elif (phnno1.isdigit()) :
    if (len(phnno1)==10):
            password=pwd1
            special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']        
            if len(password) < 8:
                msg = 'Password must be minimum of 8 characters!'
            elif not any(ch in special_ch for ch in password):
                msg = 'Atleast 1 special character required!'
            elif not any(ch.isupper() for ch in password):
                msg = 'Atleast 1 uppercase character required!'
            elif not any(ch.islower() for ch in password):
                msg = 'Atleast 1 lowercase character required!'
            elif not any(ch.isdigit() for ch in password):
                msg = 'Atleast 1 number required!'           
            else:
                  d=0
                  cursor.execute('SELECT * FROM signup')
                  check = cursor.fetchall()
                      
                  for i in check:
                      # # print(i[0])
                      # print(i)
                      p=i[0]
                      # print(aid1,p)
                      if (str(aid1)== str(p)):
                        
                          msg='Admin Already Exist'
                          # print('Invaliddd')
                          d=1
                  if d!=1:
                    conn.execute('INSERT INTO signup (aid,fname,phnno,password)  VALUES (?,?,?,?)',(aid1,fname1,phnno1,password));
                    conn.commit()
                    # print('hi444')
                    msg="Stored successfully"   
                    aid.set('')
                    phnno.set('') 
                    fname.set('')
                    pwd.set('')            
            tkMessageBox.showinfo('Warning', msg)          
    else:
      tkMessageBox.showinfo("Warning","Phone Number should be of 10 digits . . .")    
  else:
      tkMessageBox.showinfo("Warning","Incorrect Format . . .")
      
      
      
      
# Backend for login page                   ..............................................
def onclicklogin():
  laid1=laid.get()
  lpwd1=lpwd.get()
  global msg 
  msg=''
  if laid1=='' or lpwd1=='':
      tkMessageBox.showinfo("Warning","All fields are Mandatory . . .")
  else:           
                  conn = sqlite3.connect("class.db")
                  cursor = conn.cursor()
                  d=0
                  cursor.execute('SELECT * FROM signup')
                  check = cursor.fetchall()
                  e=0
                  for i in check:
                      p=i[0]
                      q=i[3]
                      if (str(laid1)== str(p)  and  str(lpwd1)== str(q)):   
                            display_screen.destroy()                    
                            # subprocess.call(["python", "dashboard.py"])
                            onclickdashboard()
                            break
                      else:
                        msg="Wrong Credentials "
                        laid.set('')
                        lpwd.set('') 
                        e=e+1                                       
                        if (e==1):   
                            tkMessageBox.showinfo('Warning', msg)
                            e=2
                         
                  
                 
                  
                  
                    
                    
  
  
  
# Signup Page               ..........................................
def onclicksignup():
    
    display_screen.destroy()
    global signtop
    signtop = Tk()
    signtop.geometry("1000x600+270+50")
    signtop.config(background="#F0FFFF")
    signtop.title("Sign Up")
    bg1 = PhotoImage(file = "reg.png")
    label1 = Label( signtop, image = bg1)
    label1.place(x = 310, y = 50)
    global conn, cursor,aid,fname,phnno,pwd
    aid=StringVar()
    fname=StringVar()
    phnno=StringVar()
    pwd=StringVar()
    # creating contact database
    conn = sqlite3.connect("class.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    cursor.execute("CREATE TABLE IF NOT EXISTS signup (aid INTEGER PRIMARY KEY  NOT NULL, fname TEXT, phnno TEXT, password TEXT)")
    lbl_text = Label(signtop, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
    width=600,bg="#00FFFF")
    lbl_text.pack(fill=X)
    Label(signtop, text="Enter Admin Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=340)
    Entry(signtop,font=("Arial",16,"bold"),textvariable=aid).place(x=520,y=340)
    Label(signtop, text="Enter First Name ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=390)
    Entry(signtop, font=("Arial", 16,"bold"),textvariable=fname).place(x=520,y=390)
    Label(signtop, text="Enter Phone Number ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=440)
    Entry(signtop,font=("Arial",16,"bold"),textvariable=phnno).place(x=520,y=440)
    Label(signtop, text="Enter Password ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=490)
    Entry(signtop, font=("Arial", 16,"bold"),textvariable=pwd,show='*').place(x=520,y=490)  
    Label(signtop, text="Already have an account ?  ", font=("Arial", 12),bg="#F0FFFF",fg="black").place(x=400,y=570)
    btn_log = Button(signtop, text="Sign Up", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onclicksignup1)
    btn_log.place(x=460,y=530)
    btn_sign = Button(signtop, text="Login",fg="red", bg="#F0FFFF",font=("Arial",12,"bold") ,borderwidth=0,command=onclicklogin1)
    btn_sign.place(x=590,y=567)
    signtop.mainloop()
 
 
 
 
 
# Login page                    .......................................................
def onclicklogin1():
  signtop.destroy()
  global display_screen
  display_screen = Tk()
  display_screen.geometry("1000x600+270+50")
  display_screen.config(background="#F0FFFF")
  display_screen.title("Login")
  bg1 = PhotoImage(file = "img.png")
  label1 = Label( display_screen, image = bg1)
  label1.place(x = 250, y = 50)
  global conn, cursor,laid,lpwd
  laid=StringVar()
  lpwd=StringVar()
  lbl_text = Label(display_screen, text="      S  M   I N F O T E C H      ", font=('Arial', 36 , BOLD), 
  width=600,bg="#00FFFF")
  lbl_text.pack(fill=X)
  lbl_text.pack(fill=X)
  Label(display_screen, text="Enter Admin Id  ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=400)
  Entry(display_screen,font=("Arial",16,"bold"),textvariable=laid).place(x=460,y=400)
  Label(display_screen, text="Enter Password ", font=("Arial", 16),bg="#F0FFFF",fg="black").place(x=300,y=460)
  Entry(display_screen, font=("Arial", 16,"bold"),textvariable=lpwd,show='*').place(x=460,y=460)
  Label(display_screen, text="Dont have an account ?  ", font=("Arial", 12),bg="#F0FFFF",fg="black").place(x=400,y=570)
  btn_log = Button(display_screen, text="Login", bg="#F0FFFF",font=("Arial",16,"bold") ,borderwidth=1,command=onclicklogin)
  btn_log.place(x=460,y=520)
  btn_sign = Button(display_screen, text="Sign Up",fg="red", bg="#F0FFFF",font=("Arial",12,"bold") ,borderwidth=0,command=onclicksignup)
  btn_sign.place(x=578,y=567)
  display_screen.mainloop()
 
 
onclicklogin1()
 

