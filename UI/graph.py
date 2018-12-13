from tkinter import*
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.geometry("750x600+0+0")
root.title("Attendance Management System")

Tops = Frame(root,bg="lightcyan3",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

"""f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
"""

f2 = Frame(root , width = 400,height=700, bd= 0)
f2.pack(side = LEFT)
f3 = Frame(root , width = 400,height=700, bd= 0)
f3.pack(side = RIGHT)
"""frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
frame1.pack()"""
#frame1.pack_propagate(False)


"""f3 = Frame(root, width = 500, height= 200, relief=SUNKEN)
f3.pack(side = LEFT)"""
l = []
l2 = []
datelist = []
# open file
with open("nlog.csv", newline = "") as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      #print(col)
      c = 0
      no = 0
      condition = 1
      for row in col:
         # i've added some styling
         #print(row)
         if(no == 1):
            l.append(row)
            

         if(no == 2):
            datelist.append(row)

         if(no == 0):
            condition = 0
         
            
         """if(condition == 1):"""
         label = Label(f2, width = 10, height = 2, \
                              text = row, relief = SUNKEN)
         label.grid(row = r, column = c)
         c += 1
         no += 1
         
      r += 1
   for i in l:
      
      l3 = []
      l3.append(i)
      
      l3.append(l.count(i))
      l2.append(l3)
   
   x = set(tuple(i) for i in l2)
   #print(x)
   x2 = list(x)
#   print(x2)
   y = set(datelist)
#   print(y)
   totalclasses = (len(y) - 1)
#   print(totalclasses)
   names = []
   names = set(l)
   #print(names)
   nameslist = list(names)
   #print(nameslist)

labe2 = Label(f3 , font=( 'aria' ,30, 'bold' ),   \
                               text = "Total ")
labe2.grid(row = 0, column = 0) 
labe2 = Label(f3, font=( 'aria' ,30, 'bold' ), text = "Attendance ")
labe2.grid(row = 0, column = 1)
labe2 = Label(f3, font=( 'aria' ,15 ), text = "  Name  ")
labe2.grid(row = 1, column = 0)
labe2 = Label(f3, font=( 'aria' ,15 ), text = "  Total  ")
labe2.grid(row = 1, column = 1)
labe2 = Label(f3, font=( 'aria' ,15 ), text = "---------------")
labe2.grid(row = 2, column = 0)
labe2 = Label(f3, font=( 'aria' ,15 ), text = "---------------")
labe2.grid(row = 2, column = 1)
r2 = 3
c2 = 0
#print(x2)
totalatt = []




for i in x2:

   

   if(i[0] != "Name"):
      labe2 = Label(f3, font=( 'aria' ,15 ), text = i[0])
      labe2.grid(row = r2, column = 0)
      labe2 = Label(f3, font=( 'aria' ,15 ), text = str(i[1]) + "/" + str(totalclasses) )
      labe2.grid(row = r2, column = 1)
      r2 += 1
      x3 = (i[1]/totalclasses)*100
      totalatt.append(x3)



nameslist.remove("Name")
nameslist2 = tuple(nameslist)
#print(nameslist2)
objects = ()
objects = (i for i in nameslist2)
#print(objects)

y_pos = np.arange(len(nameslist2))
performance = [i for i in totalatt]
#print(performance)

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')
 
plt.show()
#print(totalatt)
root.mainloop()

