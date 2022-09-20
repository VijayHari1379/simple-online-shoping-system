from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox

#main screen
master = Tk()
master.title("Banking App")
master.geometry('500x500')
master.configure(background="bisque")
#functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    phone_no = temp_phone_no.get()
    address = temp_address.get()
    email = temp_email.get()
    password = temp_password.get()
    
    all_accounts = os.listdir()
    

    if name == "" or age == "" or phone_no ==  "" or password == "" or address == "" or email ==  ""  :
        notif.config(fg="red",text="All field requried * ")
        return
    for email_check in all_accounts:
        if email == email_check:
            notif.config(fg="red",text="Accounts already existes")
            return
        else:
            new_file = open(email,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(phone_no+'\n')
            new_file.write(address+'\n')
            new_file.write(email+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green",text="Account has been created")

def reset():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    s6.set("")
    s7.set("")
    s8.set("")
    s9.set("")
    s10.set("")
    s11.set("")
    s12.set("")
    

def register():

    #var
    global temp_name
    global temp_age
    global temp_phone_no
    global temp_password
    global temp_email
    global temp_address
    global temp_password
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_phone_no=StringVar()
    temp_password=StringVar()
    temp_email=StringVar()
    temp_address=StringVar()
    
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry('500x500')
    register_screen.configure(background="grey")
    

    #Label
    l1=Label(register_screen,text="PLEASE ENTER YOUR DETAILS",font=("Lucida Calligraphy",19,"bold"))
    l1.place(x=5,y=15)
    l2=Label(register_screen,text="Name:",font=("Lucida Calligraphy",16,'bold'))
    l2.place(x=30,y=90)
    l3=Label(register_screen,text="Age:",font=("Lucida Calligraphy",16,'bold'))
    l3.place(x=30,y=140)
    l4=Label(register_screen,text="Phone no:",font=("Lucida Calligraphy",16,'bold'))
    l4.place(x=30,y=190)
    l5=Label(register_screen,text="Address:",font=("Lucida Calligraphy",16,"bold"))
    l5.place(x=30,y=240)
    l6=Label(register_screen,text="Email:",font=("Lucida Calligraphy",16,'bold'))
    l6.place(x=30,y=290)
    l7=Label(register_screen,text="Password:",font=("Lucida Calligraphy",16,"bold"))
    l7.place(x=30,y=340)
    notif= Label(register_screen,font=("Lucida Calligraphy",16,"bold"))
    notif.grid(row=6,sticky=N,pady=10)

    #Entrys
    e1=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_name,width=15)
    e1.place(x=220,y=90)
    e2=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_age,width=15)
    e2.place(x=220,y=140)
    e3=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_phone_no,width=15)
    e3.place(x=220,y=190)
    e4=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_address,width=15)
    e4.place(x=220,y=240)
    e5=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_email,width=15)
    e5.place(x=220,y=290)
    e6=Entry(register_screen,font=("Lucida Calligraphy",16,"bold"),bg='lightpink',textvariable=temp_password,show="*",width=15)
    e6.place(x=220,y=340)


    #Buttons
    b1=Button(register_screen,text="Register",command=finish_reg,font=("Lucida Calligraphy",16,"bold"),bg='lightblue')
    b1.place(x=70,y=400)
    b2=Button(register_screen,text="Cancel",command=register_screen.destroy,font=("Lucida Calligraphy",16,"bold"),bg='lightblue')
    b2.place(x=300,y=400)

def info():
    messagebox.showinfo("ORDER","Payment Successfully")
    


    

def payment():
    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
    
    payment = Toplevel(master)
    payment.title('Register')
    payment.geometry('500x500')
    payment.configure(background="sky blue")

    lbl_pay=Label(payment,font=("aria",20,"bold"),text="PAYMENT PAGE",width=30,fg="lightyellow",bg="black")
    lbl_pay.place(x=0,y=15)

    

    b1=Button(payment,text="PAY",font=("Lucida Calligraphy",12,"bold"),bg="green",width=8,command=info)
    b1.place(x=80,y=400)

    b1=Button(payment,text="CANCEL",font=("Lucida Calligraphy",12,"bold"),bg="green",width=8,command=payment.destroy)
    b1.place(x=300,y=400)

    rb=Radiobutton(payment,text="CREDIT CARD",variable=v1,value=1,font=("Lucida Calligraphy",15,"bold"))
    rb.place(x=150,y=100)

    rb1=Radiobutton(payment,text="DEBIT CARD",variable=v1,value=2,font=("Lucida Calligraphy",15,"bold"))
    rb1.place(x=150,y=200)

    rb2=Radiobutton(payment,text="CASH ON DELIVERY",variable=v1,value=3,font=("Lucida Calligraphy",15,"bold"))
    rb2.place(x=150,y=300)

    

    

    
    

def total():
    
    
    

    total_amount = Toplevel(master)
    total_amount.title('Register')
    total_amount.geometry('500x500')
    total_amount.configure(background="sea green")
    
    
    try:a1=int(s1.get())
    except: a1=0

    try:a2=int(s2.get())
    except: a2=0

    try:a3=int(s3.get())
    except: a3=0

    try:a4=int(s4.get())
    except: a4=0

    try:a5=int(s5.get())
    except: a5=0

    try:a6=int(s6.get())
    except: a6=0

    try:a7=int(s7.get())
    except: a7=0

    try:a8=int(s8.get())
    except: a8=0

    try:a9=int(s9.get())
    except: a9=0

    try:a10=int(s10.get())
    except: a10=0

    try:a11=int(s11.get())
    except: a11=0

    try:a12=int(s12.get())
    except: a12=0

    c1=600*a1
    c2=300*a2
    c3=600*a3
    c4=1500*a4
    c5=1200*a5
    c6=1800*a6
    c7=2000*a7
    c8=1800*a8
    c9=3000*a9
    c10=4500*a10
    c11=4000*a11
    c12=3500*a12

    lbl_Total=Label(total_amount,font=("aria",20,"bold"),text="TOTAL AMOUNT",width=30,fg="lightyellow",bg="black")
    lbl_Total.place(x=0,y=15)

    lbl_Total=Label(total_amount,font=("arial",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="pink")
    lbl_Total.place(x=110,y=80)

    b1=Button(total_amount,text="Total",font=("Lucida Calligraphy",12,"bold"),bg="green",width=8,command=payment)
    b1.place(x=180,y=150)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

    #f2=Frame(total_amount,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=500,height=300)
    #f2.place(x=0,y=200)

    

    
    


    
    
def login_session():

    


    
    global login_email
    all_accounts = os.listdir()
    login_email = temp_login_email.get()
    login_password = temp_login_password.get()

    for email in all_accounts:
        if email == login_email:
            file = open(email,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]

            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                account_dashboard.geometry('500x500')
                account_dashboard.configure(background="grey65")
                #Labels
                l1=Label(account_dashboard ,text="ITEMS",font=("Lucida Calligraphy",20,"bold"),bg="lightblue")
                l1.place(x=180,y=10)
                l2=Label(account_dashboard ,text="MALE:",font=("Lucida Calligraphy",12,"bold"),bg="royal blue")
                l2.place(x=200,y=60)
                l3=Label(account_dashboard ,text="PANT:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l3.place(x=15,y=100)
                l4=Label(account_dashboard ,text="T-SHIRT:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l4.place(x=15,y=140)
                l5=Label(account_dashboard ,text="SHIRT:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l5.place(x=15,y=180)
                l6=Label(account_dashboard ,text="JEANS:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l6.place(x=250,y=100)
                l7=Label(account_dashboard ,text="RAINCOATS:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l7.place(x=250,y=140)
                l8=Label(account_dashboard ,text="TROUSERS:",font=("Lucida Calligraphy",12,"bold"),bg="gold")
                l8.place(x=250,y=180)

                #male entry
                e1=Entry(account_dashboard,textvariable=s1,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e1.place(x=140,y=100)
                e2=Entry(account_dashboard,textvariable=s2,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e2.place(x=140,y=140)
                e3=Entry(account_dashboard,textvariable=s3,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e3.place(x=140,y=180)
                e4=Entry(account_dashboard,textvariable=s4,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e4.place(x=410,y=100)
                e5=Entry(account_dashboard,textvariable=s5,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e5.place(x=410,y=140)
                e6=Entry(account_dashboard,textvariable=s6,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e6.place(x=410,y=180)

                
                #female Labels
                l9=Label(account_dashboard ,text="FEMALE:",font=("Lucida Calligraphy",12,"bold"),bg="lightpink")
                l9.place(x=200,y=240)
                l10=Label(account_dashboard ,text="SAREES:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l10.place(x=15,y=280)
                l11=Label(account_dashboard ,text="KURTA:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l11.place(x=15,y=320)
                l12=Label(account_dashboard ,text="LEHENGA:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l12.place(x=15,y=360)
                l13=Label(account_dashboard ,text="PALAZZOS:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l13.place(x=250,y=280)
                l14=Label(account_dashboard ,text="DUPATTAS:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l14.place(x=250,y=320)
                l15=Label(account_dashboard ,text="ANARKALI:",font=("Lucida Calligraphy",12,"bold"),bg="turquoise")
                l15.place(x=250,y=360)

                #female entry
                e7=Entry(account_dashboard,textvariable=s7,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e7.place(x=140,y=280)
                e8=Entry(account_dashboard,textvariable=s8,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e8.place(x=140,y=320)
                e9=Entry(account_dashboard,textvariable=s9,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e9.place(x=140,y=360)
                e10=Entry(account_dashboard,textvariable=s10,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e10.place(x=410,y=280)
                e11=Entry(account_dashboard,textvariable=s11,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e11.place(x=410,y=320)
                e12=Entry(account_dashboard,textvariable=s12,font = ("Lucida Calligraphy",12,'bold'),width=4,bg="lightpink")
                e12.place(x=410,y=360)

                
                #Button
                b1=Button(account_dashboard,text="Total",font=("Lucida Calligraphy",12,"bold"),bg="green",width=8,command=total)
                b1.place(x=30,y=430)
                b2=Button(account_dashboard,text="CANCEL",font=("Lucida Calligraphy",12,"bold"),width=8,command=account_dashboard.destroy,bg="red")
                b2.place(x=190,y=430)
                b3=Button(account_dashboard,text="RESET",font=("Lucida Calligraphy",12,"bold"),width=8,command=reset,bg="violet")
                b3.place(x=350,y=430)
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)






                
                return
            else:
                login_notif.config(fg="red",text="Password incorrect!!")
                return
    
    login_notif.config(fg="red",text="No account Found !!!")

def personal_details():
    #vars
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #personal details screen
    personal_details_screen=Toplevel(master)
    personal_details_screen.title("Personal Details")
    personal_details_screen.geometry('500x500')
    personal_details_screen.configure(background="navy")
    
    #Labels
    l1=Label(personal_details_screen,text="Personal Details",font=("Lucida Calligraphy",25,"bold"),bg='blue')
    l1.place(x=60,y=20)
    l2=Label(personal_details_screen,text="Name  : " + details_name,font=("Lucida Calligraphy",19,"bold"))
    l2.place(x=90,y=100)
    l3=Label(personal_details_screen,text="Age  : " + details_age,font=("Lucida Calligraphy",19,"bold"))
    l3.place(x=90,y=200)
    l4=Label(personal_details_screen,text="Gender  : " + details_gender,font=("Lucida Calligraphy",19,"bold"))
    l4.place(x=90,y=300)
    l5=Label(personal_details_screen,text="Balance  : " + details_balance,font=("Lucida Calligraphy",19,"bold"))
    l5.place(x=90,y=400)
    
    
    



    


def login():
    #var
    global temp_login_email
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_email=StringVar()
    temp_login_password=StringVar()
    
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.geometry('500x500')
    login_screen.configure(background="grey")
    #Labels
    l1=Label(login_screen,text="Login Your Account",font=("Lucida Calligraphy",25,"bold"))
    l1.place(x=60,y=15)
    l2=Label(login_screen,text="EMAIL",font=("Lucida Calligraphy",12,"bold"))
    l2.place(x=30,y=150)
    l3=Label(login_screen,text="PASSWORD",font=("Lucida Calligraphy",12,"bold"))
    l3.place(x=30,y=250)
    login_notif = Label(login_screen,font=("Lucida Calligraphy",12,"bold"))
    login_notif.grid(row=4,sticky=N)

    #Entry
    e1=Entry(login_screen,font=("Lucida Calligraphy",16,"bold") ,width=15, textvariable=temp_login_email,bg='lightpink')
    e1.place(x=210,y=150)
    e2=Entry(login_screen ,font=("Lucida Calligraphy",16,"bold"),width=15, textvariable=temp_login_password,show="*",bg='lightpink')
    e2.place(x=210,y=250)

    #Buttons
    b1=Button(login_screen,text="Login",command=login_session,width=10,font=("Lucida Calligraphy",12,"bold"),bg='lightblue')
    b1.place(x=70,y=400)
    b2=Button(login_screen,text="Cancel",command=login_screen.destroy,width=10,font=("Lucida Calligraphy",12,"bold"),bg='lightblue')
    b2.place(x=300,y=400)
    
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()
s9=StringVar()
s10=StringVar()
s11=StringVar()
s12=StringVar()
Total_bill=StringVar()



#labels
l=Label(master, text="SIGNUP PAGE",font=("Lucida Calligraphy",30,"bold"))
l.place(x=100,y=50)



#Label(master, text="The most secure bank you probably used",font=("Lucida Calligraphy",14)).grid(row=1,sticky=N)


#buttons
b1=Button(master,text="Signup",font=("Lucida Calligraphy",14,"bold"),width=15,command=register,bg='pink')
b1.place(x=130,y=150)
b2=Button(master,text="Login",font=("Lucida Calligraphy",14,"bold"),width=15,command=login,bg='pink')
b2.place(x=130,y=250)


master.mainloop()
