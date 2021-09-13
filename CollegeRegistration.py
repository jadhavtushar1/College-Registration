from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import mysql.connector
root = Tk()
root.geometry("1900x950")
root.minsize(1900, 950)
try:
    mydb = mysql.connector.connect(host='localhost', user='root', password='Death@123', database='studentregistration')
    cursor = mydb.cursor()
    def adddata():
        id=var1.get()
        fname1 = fname.get()
        mname1 = MName.get()
        lname1 = Lname.get()
        Date1 = entry_date.get()
        pob = PlaceofBirth.get()
        genval = box1.get()
        da = box2.get()
        bc = box3.get()
        phoneno = (Phone.get())
        phoneno2 = HomePhone.get()
        homeaddress = HomeAdress.get()
        schoolname = currentschoolname.get()
        grade = currentgrade.get()
        percentage2 = percentage.get()
        email = str(Email.get())
        schooladdress = SchoolAddress.get()
        searchbar = ent13.get()
        Date2 = entry_date2.get()
        checkbtn1 = check2.get()
        checkbtn2 = check3.get()
        checkbtn3 = check4.get()
        checkbtn4 = check5.get()
        checkbtn = check.get()
        if da == "" or bc == "" or genval=="" or fname1=="" or lname1=="" or Date1=="" or homeaddress=="" or schoolname=="" or grade=="" or percentage2=="" :
            messagebox.showerror("Check Value"," Please Fill all required Details",parent = lf1)
        elif(phoneno.isdigit() and (len(phoneno) <= 14 and len(phoneno) >= 10)) and  ("@" and "." in email) and("/"and"/" in Date1)and("/" and"/" in Date2) and (check2.get() == 1 and check3.get() == 1 and check5.get() == 1 and check.get()==1) and percentage2.isdigit() and len(id)==7:

            try:
                command = ("insert into details(id,Fname,Mname,Lname,DOB,POB,Gender,DOA,PhyDis,BirthCert,PhoneNo,HomePhone,Email,CompAddress,SchoolName,Grade,Percentage,CurrentSchoolAddress,BC,SLC,FR,CL,TnC) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                vals=(id,fname1,mname1,lname1,Date1,pob,genval,Date2,da,bc,phoneno,phoneno2,email,homeaddress,schoolname,grade,percentage2,schooladdress,str(checkbtn1),str(checkbtn2),str(checkbtn3),str(checkbtn4),str(checkbtn))
                cursor.execute(command,vals)
                mydb.commit()
                messagebox.showinfo("Success","Records Added Successfully",parent=lf1)
                showupdate()
            except Exception as e:
                messagebox.askyesnocancel("Error",f"Error{str(e)}",parent = lf1)
        else:
            messagebox.showerror("values","please fill all fields correctly and submit mandetory documents",parent = lf1)

    def show(row):
        table.delete(*table.get_children())
        for i in row:
            table.insert("", "end", values=i)
    def GetData(event):

        rowid = table.identify_row(event.y)
        item = table.item(table.focus())
        var1.set(item['values'][0])
        fname.set(item['values'][1])
        MName.set(item['values'][2])
        Lname.set(item['values'][3])
        DOB.set(item['values'][4])
        PlaceofBirth.set(item['values'][5])
        box1.set(item['values'][6])
        DOA.set(item['values'][7])
        box2.set(item['values'][8])
        box3.set(item['values'][9])
        Phone.set(item['values'][10])
        HomePhone.set(item['values'][11])
        Email.set(item['values'][12])
        HomeAdress.set(item['values'][13])
        currentschoolname.set(item['values'][14])
        currentgrade.set(item['values'][15])
        percentage.set(item['values'][16])
        SchoolAddress.set(item['values'][17])
        check2.set(item['values'][18])
        check3.set(item['values'][19])
        check4.set(item['values'][20])
        check5.set(item['values'][21])
        check.set(item['values'][22])

    def clear():
        ent23.delete(0,"end")
        ent1.delete(0,"end")
        ent2.delete(0,"end")
        ent3.delete(0,"end")
        ent4.delete(0,"end")
        ent5.delete(0,"end")
        ent6.delete(0,"end")
        ent7.delete(0,"end")
        ent8.delete(0,"end")
        ent9.delete(0,"end")
        ent10.delete(0,"end")
        ent11.delete(0,"end")
        ent12.delete(0,"end")
        ent13.delete(0,"end")
        box1.delete(0,"end")
        box2.delete(0,"end")
        box3.delete(0,"end")
        entry_date.delete(0,"end")
        entry_date2.delete(0,"end")
        check2.set(0)
        check3.set(0)
        check4.set(0)
        check5.set(0)
        check.set(0)
        try:
            cursor = mydb.cursor()
            command = "select * from details"
            cursor.execute(command)
            rows = cursor.fetchall()
            mydb.commit()
            show(rows)
        except Exception as e:
            messagebox.askyesnocancel("Error", f"Error{str(e)}", parent=lf1)
    def showupdate():
        try:
            command = "select * from details"
            cursor.execute(command)
            rows = cursor.fetchall()
            mydb.commit()
            show(rows)
        except Exception as e:
            messagebox.askyesnocancel("Error", f"Error{str(e)}", parent=lf1)
    def Update():
        try:
            vals = (fname.get(), MName.get(), Lname.get(), DOB.get(), PlaceofBirth.get(), box1.get(), DOA.get(), box2.get(), box3.get(),
                    Phone.get(), HomePhone.get(), Email.get(), HomeAdress.get(), currentschoolname.get(),
                    currentgrade.get(), percentage.get(), SchoolAddress.get(), check2.get(), check3.get(), check4.get(), check5.get(),
                    check6.get(),  var1.get())
            command = ('update details set Fname=%s,Mname=%s,Lname=%s,DOB=%s,POB=%s,Gender=%s,DOA=%s,PhyDis=%s,BirthCert=%s,PhoneNo=%s,HomePhone=%s,Email=%s,CompAddress=%s,SchoolName=%s,Grade=%s,Percentage=%s,CurrentSchoolAddress=%s,BC=%s,SLC=%s,FR=%s,CL=%s,TnC=%s where id = %s ')
            cursor.execute(command, vals)
            mydb.commit()
            showupdate()
        except Exception as e:
            messagebox.askyesnocancel("Error", f"Error{str(e)}", parent=lf1)
    def Delete():
        try:
            cusyid =var1.get()
            msg1  =messagebox.askyesno("Confirmation",f"Are you sure do you want to delete {fname.get()}'s data")
            if msg1==True:
                cursor3 = mydb.cursor()
                command3 = 'delete from details where id = '+cusyid
                cursor3.execute(command3)
                mydb.commit()
                clear()
            else:
                pass
        except Exception as e:
            messagebox.askyesnocancel("Error", f"Error{str(e)}", parent=lf1)
    def search():
        try:
            q2 = str(searchbox.get())
            command2 = ("select * from details where id like '%"+q2+"%' or Fname like '%"+q2+"%' or Mname like '%"+q2+"%' or Lname like '%"+q2+"%' or DOB like '%"+q2+"%' or POB like '%"+q2+"%' or Gender like '%"+q2+"%' or DOA like '%"+q2+"%' or PhyDis like '%"+q2+"%' or BirthCert like '%"+q2+"%' or PhoneNo like '%"+q2+"%' or HomePhone like '%"+q2+"%' or Email like '%"+q2+"%' or CompAddress like '%"+q2+"%' or SchoolName like '%"+q2+"%' or Grade like '%"+q2+"%' or Percentage like '%"+q2+"%' or CurrentSchoolAddress like '%"+q2+"%' or BC like '%"+q2+"%' or SLC like '%"+q2+"%' or FR like '%"+q2+"%' or CL like '%"+q2+"%' or TnC like '%"+q2+"%' ")
            cursor.execute(command2)
            rows = cursor.fetchall()
            mydb.commit()
            show(rows)
        except Exception as e:
            messagebox.askyesnocancel("Error", f"Error{str(e)}", parent=lf3)
    def Download():
        with open(f"{fname.get()} {Phone.get()}.txt","w") as file1:
            file1.write(f''' *****APPLICATION FORM*****\nName = { fname.get()}\nMiddle Name = {MName.get()}\nLast Name = {Lname.get()}\nDate of Birth = {DOB.get()}\nPlace of Birth = { PlaceofBirth.get()}\n
    Gender = {box1.get()}\nDisability = {box2.get()}\nDate of Admission = {DOA.get()}\nBirth Certificate = {box3.get()}\nPhone = {Phone.get()}\nHome Phone = { HomePhone.get()}\nEmail = {Email.get()}\nHome Address = {HomeAdress.get()}\n
    Current School Name = {currentschoolname.get()}\ncurrent Grade = {currentgrade.get()}\nPercentage in previous Grade = { percentage.get()}\nSchool Address = { SchoolAddress.get()}\nBirth Cert = {check2.get()}\nschool LC = {check3.get()} (if 1 Submitted if 0 not Submitted)\n
    fees Receipt = {check4.get()} (if 1 Submitted if 0 not Submitted)\nConfirmation Letter = {check5.get()} (if 1 Submitted if 0 not Submitted)\nTerms and Conditions = Accepted\n*****CONGRATULATIONS YOUR APPLICATION IS SUBMITTED SUCCESSFULLY*****''')


    frame1 = Frame(root, bg="#316479", width="1920", height=100).place(x=0, y=0)
    frame2 = Frame(root, bg="#587590", width="1920", height=950).place(x=0, y=95)
    # -------------------------------------------Inpt Variables-----------------------------------------------------
    fname = StringVar()
    Lname = StringVar()
    MName = StringVar()
    DOB = StringVar()
    PlaceofBirth = StringVar()
    Gender = IntVar()
    Disability = IntVar()
    DOA = StringVar()
    BirthCertificate = IntVar()
    Phone = StringVar()
    HomePhone = StringVar()
    Email = StringVar()
    HomeAdress = StringVar()
    currentschoolname = StringVar()
    currentgrade = StringVar()
    percentage = StringVar()
    SchoolAddress = StringVar()
    check = IntVar()
    check2 = IntVar()
    check3 = IntVar()
    check4 = IntVar()
    check5 = IntVar()
    check6 = IntVar()
    searchbox = StringVar()

    # ---------------------------------------------Lable Frames---------------------------------------------------
    label1 = Label(frame1, text="VIDYADHAM JR. COLLEGE OF SCIENCE SHIRUR", font="Roboto 40 bold", fg="White",
                   bg="#316479").place(x=300, y=15)
    label2 = Label(frame1, text=", 411044", font="Roboto 15 bold", fg="White", bg="#316479").place(x=1550, y=45)
    lf1 = LabelFrame(root, text="Registration", padx=20, pady=0, width=900, height=800, bg="#587590", fg="white")
    lf1.place(x=40, y=110)
    lf2 = LabelFrame(root, text="Student Data", width=880, height=600, bg="#587590", fg="white")
    lf2.place(x=1000, y=110)
    lf3 = LabelFrame(root, text="Search in Data", width=880, height=150, bg="#587590", fg="white")
    lf3.place(x=1000, y=750)

    # -------------------------------------------Lables-----------------------------------------------------
    lab3=Label(lf1, text="Id", bg="#587590", fg="white").place(x=150, y=0)
    var1 = StringVar()
    ent23 = Entry(lf1, textvariable=var1, font="arial 10  ", bg="#B1C7DC", width=8)
    ent23.place(x=180, y=0)
    Label(lf1, text="Personal Details", font="Roboto 10 ", bg="#587590", fg="white").place(x=30, y=0)
    label3 = Label(lf1, text="First Name", bg="#587590", fg="white")
    label3.place(x=30, y=30)
    label4 = Label(lf1, text="Middle Name", bg="#587590", fg="white")
    label4.place(x=330, y=30)
    label5 = Label(lf1, text="Last Name", bg="#587590", fg="white")
    label5.place(x=630, y=30)
    label6 = Label(lf1, text="Date of birth", bg="#587590", fg="white")
    label6.place(x=30, y=120)
    label7 = Label(lf1, text="Place of Birth", bg="#587590", fg="white")
    label7.place(x=330, y=120)
    label24 = Label(lf1, text="Date Of Admission", bg="#587590", fg="white")
    label24.place(x=30, y=220)
    label8 = Label(lf1, text="Gender", bg="#587590", fg="white")
    label8.place(x=630, y=120)
    label9 = Label(lf1, text="Physically Disabled", bg="#587590", fg="white")
    label9.place(x=330, y=220)
    label23 = Label(lf1, text="Birth Certificate Available", bg="#587590", fg="white")
    label23.place(x=630, y=220)
    label10 = Label(lf1, text="Phone no", bg="#587590", fg="white").place(x=30, y=340)
    label11 = Label(lf1, text="Home Phone", bg="#587590", fg="white").place(x=330, y=340)
    label12 = Label(lf1, text="Email", bg="#587590", fg="white").place(x=630, y=340)
    label13 = Label(lf1, text=" Complete Home Address", bg="#587590", fg="white").place(x=30, y=410)
    Label(lf1, text="Current School Details", font="Roboto 10 ", bg="#587590", fg="white").place(x=30, y=490)
    label17 = Label(lf1, text="School Name", bg="#587590", fg="white").place(x=30, y=520)
    label18 = Label(lf1, text="Grade", bg="#587590", fg="white").place(x=330, y=520)
    label20 = Label(lf1, text="Percentage", bg="#587590", fg="white").place(x=630, y=520)
    label19 = Label(lf1, text="Current School Address", bg="#587590", fg="white").place(x=30, y=600)
    label22 = Label(lf1, text="Documents Enclosed", bg="#587590", fg="white").place(x=630, y=600)
    label21 = Label(lf3, text="**Please Double Click on Record After Search to Edit or Download Data", bg="#587590",
                    fg="white").place(x=220, y=100)
    # -------------------------------------------calender-----------------------------------------------------

    entry_date =Entry(lf1,textvariable = DOB, font="arial 10 ", bg="#B1C7DC", width=30)
    entry_date.place(x=30, y=150)
    entry_date2 = Entry(lf1,textvariable = DOA, font="arial 10 ", bg="#B1C7DC", width=30)
    entry_date2.place(x=30, y=250)
    # -------------------------------------------Entry Boxes-----------------------------------------------------

    ent1 = Entry(lf1, textvariable=fname, font="arial 10 ", bg="#B1C7DC", width=30)
    ent1.place(x=30, y=60)
    ent2 = Entry(lf1, textvariable=MName, font="arial 10 ", bg="#B1C7DC", width=30)
    ent2.place(x=330, y=60)
    ent3 = Entry(lf1, textvariable=Lname, font="arial 10 ", bg="#B1C7DC", width=30)
    ent3.place(x=630, y=60)
    ent4 = Entry(lf1,textvariable =PlaceofBirth , font="arial 10 ", width=30, bg="#B1C7DC")
    ent4.place(x=330, y=150)
    ent5 = Entry(lf1, textvariable=Phone, font="arial 10 ", bg="#B1C7DC", width=30)
    ent5.place(x=30, y=370)
    ent6 = Entry(lf1, textvariable=HomePhone, font="arial 10 ", bg="#B1C7DC", width=30)
    ent6.place(x=330, y=370)
    ent7 = Entry(lf1, textvariable=Email, font="arial 10 ", bg="#B1C7DC", width=30)
    ent7.place(x=630, y=370)
    ent8 = Entry(lf1, textvariable = HomeAdress,font="arial 10 ",  width=73, bg="#B1C7DC")
    ent8.place(x=30, y=450)
    ent9 = Entry(lf1,textvariable = currentschoolname, font="arial 10 ", width=30, bg="#B1C7DC")
    ent9.place(x=30, y=560)
    ent10 = Entry(lf1, textvariable=currentgrade, font="arial 10 ", bg="#B1C7DC", width=30)
    ent10.place(x=330, y=560)
    ent11 = Entry(lf1, textvariable=percentage, font="arial 10 ", bg="#B1C7DC", width=30)
    ent11.place(x=630, y=560)
    ent12 = Entry(lf1, textvariable = SchoolAddress,font="arial 10 ", width=73, bg="#B1C7DC")
    ent12.place(x=30, y=630)
    ent13 = Entry(lf3, textvariable=searchbox, font="arial 10 ", width=75, bg="#B1C7DC")
    ent13.place(x=160, y=20)

    # --------------------------------------List------------------------------------------
    box1 = Combobox(lf1,values=["Male","Sigma Male","Female","Cant Say"], font=('Helvetica', 10))
    box1.place(x = 630,y=150)
    box2 = Combobox(lf1,values=["Yes","No","What Do yo Think"])
    box2.place(x = 330,y=250)
    box3 = Combobox(lf1,values=["Yes","No","I dont know"])
    box3.place(x = 630,y=250)
    # --------------------------------------Check boxes------------------------------------------
    check12 = Checkbutton(lf1, text="Previous Grade Result", variable=check2, font=('Helvetica', 10), bg="#587590", fg="#052441")
    check12.place(x=630, y=630)
    check13 = Checkbutton(lf1, text="School LC", variable=check3, font=('Helvetica', 10), bg="#587590", fg="#052441")
    check13.place(x=630, y=650)
    check14 = Checkbutton(lf1, text="Fees Receipt", variable=check4, font=('Helvetica', 10), bg="#587590", fg="#052441")
    check14.place(x=630, y=670)
    check15 = Checkbutton(lf1, text="Confirmation Letter", variable=check5, font=('Helvetica', 10), bg="#587590",
                         fg="#052441")
    check15.place(x=630, y=690)
    check11 = Checkbutton(lf1, text="I Agree Terms & Conditions", variable=check, font=('Helvetica', 10), bg="#587590",
                         fg="#052441")
    check11.place(x=330, y=680)
    # -----------------------------------------Table-------------------------------------------------------
    table = ttk.Treeview(lf2, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22), show="headings", height=30)
    table.place(x=0, y=0)
    cols = ("nill","id","Fname","Mname","Lname","DOB","POB","Gender","DOA","PhyDis","BirthCert","PhoneNo","HomePhone","Email","CompAddress","SchoolName","Grade","Percentage","CurrentSchoolAddress","BC","SLC","FR","CL","TnC")
    for i in range(1,22):
        table.column(i, width=90, anchor="center")
        table.heading(i, text=f"{cols[i]}")

    command = ("select id,Fname,Mname,Lname,DOB,POB,Gender,DOA,PhyDis,BirthCert,PhoneNo,HomePhone,Email,CompAddress,SchoolName,Grade,Percentage,CurrentSchoolAddress,BC,SLC,FR,CL,TnC from details")
    cursor.execute(command)
    row1=cursor.fetchall()
    show(row1)
    table.bind('<Double-1>',GetData)

    # -----------------------------------------Buttons-------------------------------------------------------
    btn1 = Button(lf1, text="Update ", font=('Helvetica', 12), bg="#325779", fg="white", padx=10,command=Update).place(x=100, y=730)
    btn2 = Button(lf1, text="Add", font=('Helvetica', 12), bg="#134B7E", fg="white", padx=20, command=adddata).place(x=250,y=730)
    btn3 = Button(lf1, text="Delete", font=('Helvetica', 12), bg="#325779", fg="white", padx=10,command =Delete).place(x=400, y=730)
    btn4 = Button(lf3, text="Search", font=('Helvetica', 12), bg="#325779", fg="white", padx=15,command =search).place(x=310, y=60)
    btn5 = Button(lf3, text="Download", font=('Helvetica', 12), bg="#325779", fg="white", padx=10,command=Download).place(x=450, y=60)
    btn6 = Button(lf1, text="clear", font=('Helvetica', 12), bg="#325779", fg="white", padx=10, command=clear).place(x=550, y=730)
    btn7 = Button(lf1, text="Quite", font=('Helvetica', 12), bg="#325779", fg="white", padx=10, command=quit).place(x=700, y=730)
except Exception as e:
    messagebox.showerror("Error", f"Error{str(e)}", parent=root)
root.mainloop()
