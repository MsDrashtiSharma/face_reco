
from cgitb import text
import imp
from msvcrt import LK_NBLCK
from time import strftime, time
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import title

from PIL import Image,ImageTk
from help import HELP
from student import Student
import os
from train import Train
from face_recogni import Face_Recognition
from attend import Attendance
from developer import Developer
from help import HELP

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")
       
        #1st image
        img=Image.open(r"college_images\facialrecognition.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #2 image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        #3 image
        img2=Image.open(r"college_images\facialrecognition.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        #background image
        img3=Image.open(r"college_images\images.jfif")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("ARIAL",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
    
        
        #student button
        
        img4=Image.open(r"college_images\smart-attendance.jpg")
        img4=img4.resize((200,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1_l=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1_l.place(x=200,y=100,width=200,height=150)

        b1_l=Button(bg_img,text="Student_details",command=self.student_details,cursor="hand2",font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=250,width=200,height=40)

        #face detect
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((200,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1_l=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1_l.place(x=500,y=100,width=200,height=150)

        b1_l=Button(bg_img,text="Face Detect",cursor="hand2",command=self.face_data,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=500,y=250,width=200,height=40)

        # Attendance face detect
        img6=Image.open(r"college_images\report.jpg")
        img6=img6.resize((200,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1_l=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1_l.place(x=800,y=100,width=200,height=150)

        b1_l=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=800,y=250,width=200,height=40)
        
        #help desk

        img7=Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((200,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1_l=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1_l.place(x=1100,y=100,width=200,height=150)

        b1_l=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=1100,y=250,width=200,height=40)
        
        #train
        
        
        img8=Image.open(r"C:\Users\drash\OneDrive\Desktop\facial_system\college_images\Train.jpg")
        img8=img8.resize((200,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1_l=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1_l.place(x=200,y=380,width=200,height=150)

        b1_l=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=530,width=200,height=40)
  
        
        #photos face button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((200,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1_l=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1_l.place(x=500,y=380,width=200,height=150)

        b1_l=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=500,y=530,width=200,height=40)

         #developer
        img10=Image.open(r"college_images\developer.jpg")
        img10=img10.resize((200,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1_l=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.develop_data)
        b1_l.place(x=800,y=380,width=200,height=150)

        b1_l=Button(bg_img,text="Developer",cursor="hand2",command=self.develop_data,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=800,y=530,width=200,height=40)
        #exit
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((200,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1_l=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1_l.place(x=1100,y=380,width=200,height=150)

        b1_l=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=1100,y=530,width=200,height=40)
        

    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are u sure u want to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return    





    #Function details
    
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

       
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)    

    
    def develop_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=HELP(self.new_window) 

      
       
   
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()