from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Attendance Management System")

Tops = Frame(root,bg="lightcyan3",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

"""f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
"""

f2 = Frame(root , width = 400,height=700, bd= 0)
f2.pack()
"""frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
frame1.pack()"""
#frame1.pack_propagate(False)


f3 = Frame(root, width = 500, height= 200, relief=SUNKEN)
f3.pack()

logo="NIIT UNIVERSITY"
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="******CAPSTONE PROJECT******",fg="black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=logo,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

"""txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)


"""
def reset():
        q.set("")
        w.set("")
        e.set("")

def live():
    root4 = Tk()
    root4.geometry("800x350+0+0")
    root4.title("Attendance Management System")

    Tops4 = Frame(root4,bg="lightcyan3",width = 1600,height=50,relief=SUNKEN)
    Tops4.pack(side=TOP)

    f14 = Frame(root4 , highlightbackground="green", highlightcolor="green", highlightthickness=1, width = 400,height=700, bd= 0)
    f14.pack(side=LEFT)
    f24 = Frame(root4,width = 900,height=700,relief=SUNKEN)
    f24.pack(side=RIGHT)

    f34 = Frame(root4, width = 500, height= 200, relief=SUNKEN)
    f34.pack()

    q = StringVar()
    w = StringVar()
    e = StringVar()

    lblinfo = Label(f14, font=( 'aria' ,30, 'bold' ),text="Register User",fg="black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)

    lblreference = Label(f14, font=( 'aria' ,16, 'bold' ),text="Enter Name",fg="steel blue",bd=10,anchor='w')
    lblreference.grid(row=1,column=0)
    txtreference = Entry(f14,font=('ariel' ,16,'bold'), textvariable=q , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtreference.grid(row=1,column=1)

    lblfries = Label(f14, font=( 'aria' ,16, 'bold' ),text="   Enter Enr No.",fg="steel blue",bd=10,anchor='w')
    lblfries.grid(row=2,column=0)
    txtfries = Entry(f14,font=('ariel' ,16,'bold'), textvariable=w , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtfries.grid(row=2,column=1)

    lblLargefries = Label(f14, font=( 'aria' ,16, 'bold' ),text="   Enter Section",fg="steel blue",bd=10,anchor='w')
    lblLargefries.grid(row=3,column=0)
    txtLargefries = Entry(f14,font=('ariel' ,16,'bold'), textvariable=e , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtLargefries.grid(row=3,column=1)

    btnprice=Button(f14,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Submit", bg="powder blue")
    btnprice.grid(row=6, column=0)
    btnprice=Button(f14,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Reset", bg="powder blue", command = reset)
    btnprice.grid(row=6, column=1)
    btnprice=Button(f24,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Live Detection", bg="powder blue", anchor = 's')
    btnprice.grid(row=6, column=0)

    root4.mainloop()

    

def registeruser():
    root3 = Tk()
    """root.geometry("1600x700+0+0")"""
    root3.title("Attendance Management System")

    Tops3 = Frame(root3,bg="lightcyan3",width = 1600,height=50,relief=SUNKEN)
    Tops3.pack(side=TOP)


    q = StringVar()
    w = StringVar()
    e = StringVar()

    lblreference = Label(Tops3, font=( 'aria' ,16, 'bold' ),text="Enter Name",fg="steel blue",bd=10,anchor='w')
    lblreference.grid(row=0,column=0)
    txtreference = Entry(Tops3,font=('ariel' ,16,'bold'), textvariable=q , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtreference.grid(row=0,column=1)

    lblfries = Label(Tops3, font=( 'aria' ,16, 'bold' ),text="   Enter Enr No.",fg="steel blue",bd=10,anchor='w')
    lblfries.grid(row=1,column=0)
    txtfries = Entry(Tops3,font=('ariel' ,16,'bold'), textvariable=w , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtfries.grid(row=1,column=1)

    lblLargefries = Label(Tops3, font=( 'aria' ,16, 'bold' ),text="   Enter Section",fg="steel blue",bd=10,anchor='w')
    lblLargefries.grid(row=2,column=0)
    txtLargefries = Entry(Tops3,font=('ariel' ,16,'bold'), textvariable=e , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
    txtLargefries.grid(row=2,column=1)

    btnTotal=Button(Tops3,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="SUBMIT", bg="powder blue")
    btnTotal.grid(row=7, column=1)


    root.mainloop()


def attendance():
    

    root2 = Tk()
    root2.geometry("1600x700+0+0")
    root2.title("Attendance Management System")

    Tops2 = Frame(root2,bg="lightcyan3",width = 1600,height=50,relief=SUNKEN)
    Tops2.pack(side=TOP)

    logo2 = "NIIT UNIVERSITY"
    lblinfo = Label(Tops2, font=( 'aria' ,30, 'bold' ),text="***ATTENDANCE SYSTEM***",fg="black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops2, font=( 'aria' ,20, ),text=logo2,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)
    f22 = Frame(root2 , width = 400,height=700, bd= 0)
    f22.pack()

    f32 = Frame(root2, width = 500, height= 200, relief=SUNKEN)
    f32.pack()


    btn7=Button(f22,padx=130,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="REGISTER USER",bg="powder blue", command= registeruser )
    btn7.grid(row=4,column=0, padx=10, pady=20)

    btn8=Button(f22,padx=103,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="MARK ATTENDANCE",bg="powder blue", command=lambda: btnclick(8) )
    btn8.grid(row=5,column=0, padx=10, pady=20)

    btn7=Button(f22,padx=103,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="SHOW ATTENDANCE",bg="powder blue", command=lambda: btnclick(7) )
    btn7.grid(row=6,column=0, padx=10, pady=20)

    Tops2.mainloop()



#*********************************
def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""




def qexit():
    root.destroy()

"""def reset():
    q.set("")
    w.set("")
    e.set("")
    r.set("")
    t.set("")
    y.set("")
    u.set("")
    i.set("")
    o.set("")
    p.set("")
    a.set("")
    s.set("")"""

#************************************
btn7=Button(f2,padx=172,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="Attendance",bg="powder blue", command = attendance )
btn7.grid(row=1,column=0, padx=10, pady=20)

btn8=Button(f2,padx=123,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="Emotion Detection",bg="powder blue", command=lambda: btnclick(8) )
btn8.grid(row=2,column=0, padx=10, pady=20)

btn7=Button(f2,padx=100,pady=12,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="Live Face Recognition",bg="powder blue", command= live )
btn7.grid(row=3,column=0, padx=10, pady=20)

#---------------------------------------------------------------------------------------


q = StringVar()
w = StringVar()
e = StringVar()
"""
r = StringVar()
t = StringVar()
y = StringVar()
u = StringVar()
i = StringVar()
o = StringVar()
p = StringVar()
a = StringVar()
s = StringVar()"""


"""lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Enter Name",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=q , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="   Enter Enr No.",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=w , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="   Enter Section",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=e , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)
"""

#--------------------------------------------------------------------------------------


#-----------------------------------------buttons------------------------------------------
"""lblTotal = Label(f1,text="------------------------------------------------------------------------------------------------",fg="black")
lblTotal.grid(row=6,columnspan=3)"""
"""
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)
"""
"""btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=1)
"""
"""btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=2)
"""
def show():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Total Attendance")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SUBJECTS", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ATTENDANCE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________", fg="black", anchor=W)
    lblinfo.grid(row=1, column=0)
    
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________", fg="black", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Data Str.", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CPP", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Physics", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Algorithms", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chemistry", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    

    roo.mainloop()

"""btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Show", bg="powder blue",command=show)
btnprice.grid(row=7, column=0)
"""
root.mainloop()

