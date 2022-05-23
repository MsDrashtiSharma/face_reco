from operator import delitem
from tkinter import*
from tkinter import ttk
from turtle import update
from xml.etree.ElementPath import prepare_predicate
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector
from mysqlx import UpdateStatement
from numpy import delete
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")

        #********************************text variable****************************************
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


         #1st image
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
            #2 image
        img1=Image.open(r"college_images\smart-attendance.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=570,height=200)

        title_lbl=Label(self.root,text="Attendance Management System",font=("ARIAL",20,"bold"),bg="blue",fg="black")
        title_lbl.place(x=0,y=200,width=1380,height=40)

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=5,y=245,width=1353,height=485)
        

          #Left_frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="pink",relief=RIDGE,text="Student Attendane  Details",font=("Times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=465)

        #img_left
        img_left=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\dev.jpg")
        img_left=img_left.resize((640,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=150)


        #left_inside_frame
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=153,width=640,height=275)


      #  label and entry


        #attendancet_id
        attendance_id_label=Label(left_inside_frame,text="Attendance:Id",font=("Times new roman",12,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
          
        #Roll
        
        rollLabel=Label(left_inside_frame,text="Roll",font=("Times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("Times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        
        NameLabel=Label(left_inside_frame,text="Name",font=("Times new roman",12,"bold"),bg="white")
        NameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("Times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        
        depLabel=Label(left_inside_frame,text="Department",font=("Times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=4,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("Times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

          #time
        
        timeLabel=Label(left_inside_frame,text="Time",font=("Times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("Times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Date
        
        dateLabel=Label(left_inside_frame,text="Date",font=("Times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=4,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("Times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance
        attenLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("Times new roman" ,12,"bold"))
        attenLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("Times new roman", 12,"bold"),state="read only")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        
              
      #button frmae
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=80,y=200,width=475,height=45)

        save_btn=Button(btn_frame,text="Import csv",width=15,command=self.importCsv,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=5)

        update_btn=Button(btn_frame,text="Export Csv",width=15,command=self.exportCsv,font=("Times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5)

       # delete_btn=Button(btn_frame,text="Update",width=15,font=("Times new roman",12,"bold"),bg="blue",fg="white")
        #delete_btn.grid(row=0,column=2,padx=5,pady=5)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("Times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=2,padx=5,pady=5)

        #Right_frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="pink",relief=RIDGE,text="Attendance Details",font=("Times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=465)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=640,height=430)


      #scroll bar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #fetch data 
    

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
          self.AttendanceReportTable.insert("",END,values=i)  

#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
            mydata.append(i)
          self.fetchData(mydata)  

#export csv
    
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"succesfully")
      except Exception as es:
             messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)      

    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content["values"]
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])
      
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")


    
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()