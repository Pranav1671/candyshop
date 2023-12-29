from tkinter import *
from tkinter import ttk
win=Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.configure(height=h,width=w)

win.title("ShoppingProject")
bgi=PhotoImage(file="pbr1.png")
li=Label(win,image=bgi)
li.pack()

deli=20
svar=StringVar()
lbl=Label(win,textvariable=svar,font=('impact',30,'italic'),bg='red',fg='black',height=1,width=50)

def shif():
    shif.msg=shif.msg[1:]+shif.msg[0]
    svar.set(shif.msg)
    win.after(deli,shif)

shif.msg='                                                                                                                                                                                              Welcome To LW Candy Shop'
shif()
lbl.place(x=180,y=60)

def product():
    win.destroy()
    import spo2

deli1=40
svar1=StringVar()
lbl=Label(win,textvariable=svar1,font=('impact',30,'italic'),bg='red',fg='black',height=1,width=30)

def shif1():
    shif1.msg=shif1.msg[1:]+shif1.msg[0]
    svar1.set(shif1.msg)
    win.after(deli1,shif1)

shif1.msg='                                                                                                                                       Click Below To Start Shopping'
shif1()
lbl.place(x=390,y=210)


nxt=Button(win,text='Product Section',font=('arialblack',15,'bold'),command=product)
nxt.place(x=600,y=300)


win.mainloop()



