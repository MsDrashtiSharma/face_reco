
from tkinter import*
from tkinter import ttk
from turtle import update

from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector
from mysqlx import UpdateStatement
from numpy import delete
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")
        
        #********************variable*******************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()  
        self.var_std_name=StringVar()             
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
      #1st image
        img=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\stu.png")
        img=img.resize((500,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=100)
        #2 image
        img1=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\stu.png")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=100)
        #3 image
        img2=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\stu.png")
        img2=img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)

         #background image
        img3=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\images.jfif")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1500,height=710)

        title_lbl=Label(bg_img,text="Student Management system",font=("ARIAL",20,"bold"),bg="black",fg="pink")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=30,width=1330,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=585)

        img_left=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((640,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=100)

        #current__cousre
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Cousre Information",font=("Times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=110,width=640,height=110)
        #department
        dep_label=Label(Current_course_frame,text="Department",font=("Times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("Times new roman",12,"bold"),state="read only")
        dep_combo["value"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #course
        course_label=Label(Current_course_frame,text="Course",font=("Times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("Times new roman",12,"bold"),state="read only",width=20)
        course_combo["value"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #year
        year_label=Label(Current_course_frame,text="Year",font=("Times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("Times new roman",12,"bold"),state="read only",width=20)
        year_combo["value"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(Current_course_frame,text="Semester",font=("Times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("Times new roman",12,"bold"),state="read only",width=20)
        semester_combo["value"]=("Select Semester","Semester1","Semester2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class_student__cousre
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Times new roman",12,"bold"))
        class_student_frame.place(x=5,y=230,width=640,height=330)
        
        #student_id
        student_id_label=Label(class_student_frame,text="Student:Id",font=("Times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         
         #student_name
        studenName_label=Label(class_student_frame,text="Student:Name",font=("Times new roman",12,"bold"),bg="white")
        studenName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studenName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Times new roman",12,"bold"))
        studenName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #class division
        class_div_label=Label(class_student_frame,text="Class:Division",font=("Times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Times new roman",12,"bold"),state="read only",width=18)
        div_combo["value"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       
        
        #Roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("Times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)  

        #gender
        gender_label=Label(class_student_frame,text="Gender",font=("Times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times new roman",12,"bold"),state="read only",width=18)
        gender_combo["value"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("Times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)  

        #email
        email_label=Label(class_student_frame,text="Email:",font=("Times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)  

        #phone
        phone_label=Label(class_student_frame,text="Phone No:",font=("Times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)  

        #address
        address_label=Label(class_student_frame,text="Address:",font=("Times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)  

        #teacher
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("Times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)  

        
        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=6,column=1)

        #button frmae
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=210,width=625,height=45)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("Times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("Times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=5)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=260,width=625,height=45)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=60,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=1,padx=20,pady=5)

        #update_photo_btn=Button(btn_frame1,text="Update Photo",width=32,font=("Times new roman",12,"bold"),bg="black",fg="white")
        #update_photo_btn.grid(row=0,column=2,padx=5,pady=5)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=640,height=585)
        
        img_right=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\gettyimages-1022573162.jpg")
        img_right=img_right.resize((640,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=640,height=100)

        #searching system
       # search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("Times new roman",12,"bold"))
        #search_frame.place(x=5,y=110,width=625,height=70)
        
        #search_label=Label(search_frame,text="Search By:",font=("Times new roman",15,"bold"),bg="blue",fg="white")
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search_combo=ttk.Combobox(search_frame,font=("Times new roman",12,"bold"),state="read only",width=15)
        #search_combo["value"]=("Select","Roll No","Phone No")
        #search_combo.current(0)
        #search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search_entry=ttk.Entry(search_frame,width=15,font=("Times new roman",12,"bold"))
        #search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)  
       
        #search_btn=Button(search_frame,text="Search",width=9,font=("Times new roman",12,"bold"),bg="black",fg="white")
        #search_btn.grid(row=0,column=3,padx=5,pady=5)

        #showAll_btn=Button(search_frame,text="ShowAll",width=9,font=("Times new roman",12,"bold"),bg="black",fg="white")
        #showAll_btn.grid(row=0,column=4,padx=5,pady=5)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=102,width=625,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
       
        self.student_table.heading("name",text="Name")  
        self.student_table.heading("id",text="id")     
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        
        self.student_table.column("name",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
    #function declartion
    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Feilds are require",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="drashti@123",database="face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(  self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    
                                                                                                                    self.var_std_name.get(), 
                                                                                                                    self.var_std_id.get(),                                                                                                                                                                                                                                       
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                    
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Student detils has been added Succesfully",parent=self.root)                                                                                                
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    #fetch data
    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="drashti@123",database="face_recog")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

        #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])        
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Feilds are require",parent=self.root)    
        else:
            try:
                Update=messagebox.askyesno("Update","do you want to update this student details",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="drashti@123",database="face_recog")
                     my_cursor=conn.cursor() 
                     my_cursor.execute("update student set Depa=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                     self.var_std_id.get()
                                                                                                                                                                                                                 ))                                                                                                                                                                
                else:
                    if not Update:
                     return
                messagebox.showinfo("Success","Student detail dsuccesfully updated",parent=self.root)      
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete data
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do u want to delete this student",parent=self.root)  
                if delete>0: 
                     conn=mysql.connector.connect(host="localhost",username="root",password="drashti@123",database="face_recog")
                     my_cursor=conn.cursor() 
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                    # my_cursor.execute("delete from student  where Student_id=%s",(self.var_std_id.get())) 
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
     
     #reset
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Male")        
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")


     #GENERATE DATA SET OR TAKE PHOTO
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Feilds are require",parent=self.root)    
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="drashti@123",database="face_recog")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                     id+=1
                my_cursor.execute("update student set Depa=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                     self.var_std_id.get()==id+1
                                                                                                                                                                                                                 ))                                                                                                                                                                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #load predefined data on face frontal from open cv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                    faces=face_classifier.detectMultiScale(gray,1.3,5)   
        
        
                     #scaling factoor=1.3
                     # minimum negibour=5
              
                    for(x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return  face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==10:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data set completed succesfully",parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)              

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()    