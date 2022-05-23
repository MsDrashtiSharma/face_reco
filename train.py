from msilib.schema import File
from tkinter import*
from tkinter import ttk
from turtle import update

from PIL import Image,ImageTk
from tkinter import messagebox 
import mysql.connector
from mysqlx import UpdateStatement
from numpy import delete
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl=Label(self.root,text="TRAINED DATA SET",font=("ARIAL",34,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1400,height=36)

        img_top=Image.open(r"college_images\train1.png")
        img_top=img_top.resize((1370,300),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=37,width=1370,height=300)
        

        #button
        b1_l=Button(self.root,text="Trained Data",command=self.train_classifier,cursor="hand2",font=("ARIAL",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=0,y=340,width=1370,height=60)

        img_bottom=Image.open(r"college_images\train1.png")
        img_bottom=img_bottom.resize((1370,300),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=405,width=1370,height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[] 
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image 
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets compeleted!!")      


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()