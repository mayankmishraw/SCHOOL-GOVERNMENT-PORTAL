from tkinter import *
from PIL import Image,ImageTk
def func():
    print("hey")
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
img=Image.open("j.jpg")
img=img.resize((1570,800))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=800)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
Button(root,text="<<BACK",command=func,font="comicsansms 10 bold").place(x=5,y=650)
Button(root,text="SAVE",command=func,font="default 15 bold").place(x=600,y=650)
Label(root,text="SCHOOL DETAIL FORM",font="default 25 bold",fg="red").place(x=510,y=33)
svar=StringVar()
pvar=StringVar()
scidvar=StringVar()
scaddvar=StringVar()
statevar=StringVar()
distvar=StringVar()
blockvar=StringVar()
mailvar=StringVar()
typevar=StringVar()
yearvar=StringVar()
grovar= StringVar()
midvar = StringVar()
teapvar = StringVar()
teatvar = StringVar()
toipvar = StringVar()
toitvar = StringVar()

a=Entry(root,textvariable=svar,font="courier 10 bold")
a.place(x=500,y=100)
a.focus_force()
i=Entry(root,textvariable=pvar,font="courier 10 bold")
i.place(x=500,y=160)
b=Entry(root,textvariable=scidvar,font="courier 10 bold")
b.place(x=500,y=220)
j=Entry(root,textvariable=teapvar,font="courier 10 bold")
j.place(x=850,y=220)
k=Entry(root,textvariable=teatvar,font="courier 10 bold")
k.place(x=1180,y=220)
c=Entry(root,textvariable=scaddvar,font="courier 10 bold")
c.place(x=500,y=280)
d=Entry(root,textvariable=mailvar,font="courier 10 bold")
d.place(x=500,y=340)
e=Entry(root,textvariable=typevar,font="courier 10 bold")
e.place(x=500,y=400)
f=Entry(root,textvariable=yearvar,font="courier 10 bold")
f.place(x=500,y=460)
l=Entry(root,textvariable=toipvar,font="courier 10 bold")
l.place(x=850,y=460)
m=Entry(root,textvariable=toitvar,font="courier 10 bold")
m.place(x=1180,y=460)

#this is different
a1=Label(root,text="AREA OF SCHOOL",font="courier 20 bold")
a1.place(x=100,y=100)
a1=Label(root,text="NUMBER OF STUDENTS",font="courier 20 bold")
a1.place(x=100,y=160)
a1=Label(root,text="NUMBER OF TEACHER",font="courier 20 bold")
a1.place(x=100,y=220)
a1=Label(root,text ="OTHER STAFF",font="courier 20 bold")
a1.place(x=100,y=280)
a1=Label(root,text="NUMBER OF LABS",font="courier 20 bold")
a1.place(x=100,y=340)
a1=Label(root,text="WATER PURIFIER",font="courier 20 bold")
a1.place(x=100,y=400)
a1=Label(root,text="TOILET",font="courier 20 bold")
a1.place(x=100,y=460)
a1=Label(root,text="GROUND",font="courier 20 bold")
a1.place(x=100,y=520)
a1=Label(root,text="MID- DAY MEAL",font="courier 20 bold")
a1.place(x=100,y=580)
a1=Label(root,text="PERMANENT ",font="courier 15 bold")
a1.place(x=1040,y=220)
a1=Label(root,text="TEMPORARY",font="courier 15 bold")
a1.place(x=700,y=220)
a1=Label(root,text="GILRS  ",font="courier 15 bold")
a1.place(x=1040,y=460)
a1=Label(root,text="BOYS",font="courier 15 bold")
a1.place(x=700,y=460)
varr=IntVar()
radio=Radiobutton(root,text="YES",variable=varr,value=1,font="comicsamsms 15")
radio.place(x=500,y=520)
radio=Radiobutton(root,text="NO",variable=varr,value=2,font="comicsamsms 15")
radio.place(x=590,y=520)
varr2=IntVar()
radio1=Radiobutton(root,text="YES",variable=varr2,value=1,font="comicsamsms 15")
radio1.place(x=500,y=590)
radio1=Radiobutton(root,text="NO",variable=varr2,value=2,font="comicsamsms 15")
radio1.place(x=590,y=590)
root.mainloop()