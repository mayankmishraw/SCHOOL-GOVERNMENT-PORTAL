from tkinter import *
from PIL import Image,ImageTk
def func():
    pass
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
img=Image.open("JAO.jpg")
img=img.resize((1370,800))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=700)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
Label(root,text="USERNAME",bg="white",fg="blue",font="courier 30 bold",relief=RAISED).place(x=420,y=270)
Label(root,text="PASSWORD",bg="white",fg="blue",font="courier 30 bold",relief=RAISED).place(x=420,y=360)
Button(root,text="<<BACK",command=func,font="comicsansms 10 bold").place(x=5,y=650)
strr=StringVar()
strr2=StringVar()
e1=Entry(root,textvariable=strr,font="courier 30 bold",fg="red")
e1.place(x=640,y=273)
e1.focus_force()
e2=Entry(root,textvariable=strr2,font="courier 30 bold")
e2.place(x=640,y=360)
e2.focus_force()
Button(root,text="LOGIN",command=func,font="default 15 bold").place(x=590,y=473)
Button(root,text="SIGN UP",command=func,font="default 15 bold").place(x=720,y=473)
root.mainloop()