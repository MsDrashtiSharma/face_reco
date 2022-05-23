from tkinter import*
from tkinter import ttk
from turtle import update

from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector
from mysqlx import UpdateStatement
from numpy import delete
import cv2



class HELP:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="HELP DESK",font=("ARIAL",34,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=55)

        img_top=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1370,680),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1370,height=680)


        dev_label=Label(f_lbl,text="Email : drashtibhardwaj2002@gmail.com",font=("Times new roman",20,"bold"),bg="black",fg="white")
        dev_label.place(x=450,y=200)

if __name__=="__main__":
    root=Tk()
    obj=HELP(root)
    root.mainloop()      