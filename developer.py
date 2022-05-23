from tkinter import*
from tkinter import ttk
from turtle import update

from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector
from mysqlx import UpdateStatement
from numpy import delete
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="DEVELOPER",font=("ARIAL",34,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=55)

        img_top=Image.open(r"college_images\bg1.jpg")
        img_top=img_top.resize((1370,680),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1370,height=680)

            #frame
            
        main_frame=Frame(f_lbl,bd=2,bg="white",relief=RIDGE)
        main_frame.place(x=1050,y=100,width=300,height=100)


        dev_label=Label(main_frame,text="I'm Drashti Sharma",font=("Times new roman",20,"bold"),bg="white")
        dev_label.place(x=5,y=5)

        deve_label=Label(main_frame,text="  a PROgrammar",font=("Times new roman",20,"bold"),bg="white")
        deve_label.place(x=5,y=40)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()    