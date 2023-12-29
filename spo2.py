from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
win=Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.configure(height=h,width=w)

mycon=mysql.connector.connect(host='localhost',user='root',password='pass',database='choco')
mycursor=mycon.cursor()

mycursor.execute('drop table if exists cart')
mycursor.execute('create table cart(product varchar(20),qty integer(3),cost integer(10))')

win.title("ShoppingProject")
bgi=PhotoImage(file="back2.png")
li=Label(win,image=bgi)
li.pack()

class products:
    i=[0,0,0,0,0,0,0,0,0,0,0]
    j=['Diarymilk','Fivestar','Perk','Milkybarclassic','Fabelle','Bournville','Mrbeast','Darkchocolate','Kitkatdark','Diarymilkbubbles','Whittakershazelnut']
    k=[40,20,10,15,1500,150,3499,140,50,200,899]
obj1=products()

plus=PhotoImage(file='plus.png')
minus=PhotoImage(file='minus.png')

class quantity:
    def increment(self,a):
        if a=='i1':
            obj1.i[0]+=1
            et1.config(text=obj1.i[0])
        elif a=='i2':
            obj1.i[1]+=1
            et2.config(text=obj1.i[1])
        elif a=='i3':
            obj1.i[2]+=1
            et3.config(text=obj1.i[2])
        elif a=='i4':
            obj1.i[3]+=1
            et4.config(text=obj1.i[3])
        elif a=='i5':
            obj1.i[4]+=1
            et5.config(text=obj1.i[4])
        elif a=='i6':
            obj1.i[5]+=1
            et6.config(text=obj1.i[5])
        elif a=='i7':
            obj1.i[6]+=1
            et7.config(text=obj1.i[6])
        elif a=='i8':
            obj1.i[7]+=1
            et8.config(text=obj1.i[7])
        elif a=='i9':
            obj1.i[8]+=1
            et9.config(text=obj1.i[8])
        elif a=='i10':
            obj1.i[9]+=1
            et10.config(text=obj1.i[9])
        elif a=='i11':
            obj1.i[10]+=1
            et11.config(text=obj1.i[10])
        else:
            pass
    
    def decrement(self,a):
        if a=='i1':
            if obj1.i[0]>=1:
                obj1.i[0]-=1
                et1.config(text=obj1.i[0])
        elif a=='i2':
            if obj1.i[1]>=1:
                obj1.i[1]-=1
                et2.config(text=obj1.i[1])
        elif a=='i3':
            if obj1.i[2]>=1:
                obj1.i[2]-=1
                et3.config(text=obj1.i[2])
        elif a=='i4':
            if obj1.i[3]>=1:
                obj1.i[3]-=1
                et4.config(text=obj1.i[3])
        elif a=='i5':
            if obj1.i[4]>=1:
                obj1.i[4]-=1
                et5.config(text=obj1.i[4])
        elif a=='i6':
            if obj1.i[5]>=1:
                obj1.i[5]-=1
                et6.config(text=obj1.i[5])
        elif a=='i7':
            if obj1.i[6]>=1:
                obj1.i[6]-=1
                et7.config(text=obj1.i[6])
        elif a=='i8':
            if obj1.i[7]>=1:
                obj1.i[7]-=1
                et8.config(text=obj1.i[7])
        elif a=='i9':
            if obj1.i[8]>=1:
                obj1.i[8]-=1
                et9.config(text=obj1.i[8])
        elif a=='i10':
            if obj1.i[9]>=1:
                obj1.i[9]-=1
                et10.config(text=obj1.i[9])
        elif a=='i11':
            if obj1.i[10]>=1:
                obj1.i[10]-=1
                et11.config(text=obj1.i[10])
        else:
            pass
obj2=quantity()

def diarymilk():
    import diarymilk

def fivestar():
    import fivestar

def perk():
    import perk

def milkybarclassic():
    import milkybarclassic

def fabelle():
    import fabelle

def bournville():
    import bournville

def mrbeast():
    import mrbeast

def darkchocolate():
    import darkchocolate

def kitkatdark():
    import kitkatdark

def diarymilkbubbles():
    import diarymilkbubbles

def whittakershazelnut():
    import whittakershazelnut



#DIARYMILK
p1=PhotoImage(file="diarymilk.png")
bt1=Button(win,image=p1,command=diarymilk,borderwidth=8,bg='green')
bt1.place(x=70,y=20)
ett1=Label(win,text='₹'+str(obj1.k[0]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett1.place(x=70,y=193)
et1=Label(win,text=obj1.i[0],font=('arialbalck',20),width=10,justify=CENTER,bd=2)
et1.place(x=70,y=235)
incbtn1=Button(win,image=plus,command=lambda:obj2.increment('i1'))
incbtn1.place(x=200,y=236)
decbtn1=Button(win,image=minus,command=lambda:obj2.decrement('i1'))
decbtn1.place(x=70,y=236)

#5STAR
p2=PhotoImage(file="5star.png")
bt2=Button(win,image=p2,command=fivestar,borderwidth=8,bg='green')
bt2.place(x=280,y=48)
ett2=Label(win,text='₹'+str(obj1.k[1]),font=('arialbalck',20),width=13,justify=CENTER,bd=2)
ett2.place(x=280,y=193)
et2=Label(win,text=obj1.i[1],font=('arialbalck',20),width=13,justify=CENTER)
et2.place(x=280,y=235)
incbtn2=Button(win,image=plus,command=lambda:obj2.increment('i2'))
incbtn2.place(x=458,y=236)
decbtn2=Button(win,image=minus,command=lambda:obj2.decrement('i2'))
decbtn2.place(x=280,y=236)

#PERK
p3=PhotoImage(file="perk.png")
bt3=Button(win,image=p3,command=perk,borderwidth=8,bg='green')
bt3.place(x=510,y=38)
ett3=Label(win,text='₹'+str(obj1.k[2]),font=('arialbalck',20),width=15,justify=CENTER,bd=2)
ett3.place(x=510,y=193)
et3=Label(win,text=obj1.i[2],font=('arialbalck',20),width=15,justify=CENTER)
et3.place(x=510,y=235)
incbtn3=Button(win,image=plus,command=lambda:obj2.increment('i3'))
incbtn3.place(x=720,y=236)
decbtn3=Button(win,image=minus,command=lambda:obj2.decrement('i3'))
decbtn3.place(x=510,y=236)

#MILKYBARCLASSIC
p4=PhotoImage(file="milkybarclassic.png")
bt4=Button(win,image=p4,command=milkybarclassic,borderwidth=8,bg='green')
bt4.place(x=775,y=28)
ett4=Label(win,text='₹'+str(obj1.k[3]),font=('arialbalck',20),width=18,justify=CENTER,bd=2)
ett4.place(x=775,y=193)
et4=Label(win,text=obj1.i[3],font=('arialbalck',20),width=18,justify=CENTER)
et4.place(x=775,y=235)
incbtn4=Button(win,image=plus,command=lambda:obj2.increment('i4'))
incbtn4.place(x=1033,y=236)
decbtn4=Button(win,image=minus,command=lambda:obj2.decrement('i4'))
decbtn4.place(x=776,y=236)

#FABELLE
p5=PhotoImage(file="fabelle.png")
bt5=Button(win,image=p5,command=fabelle,borderwidth=8,bg='green')
bt5.place(x=1120,y=20)
ett5=Label(win,text='₹'+str(obj1.k[4]),font=('arialbalck',20),width=11,justify=CENTER,bd=2)
ett5.place(x=1113,y=193)
et5=Label(win,text=obj1.i[4],font=('arialbalck',20),width=11,justify=CENTER)
et5.place(x=1113,y=235)
incbtn5=Button(win,image=plus,command=lambda:obj2.increment('i5'))
incbtn5.place(x=1260,y=236)
decbtn5=Button(win,image=minus,command=lambda:obj2.decrement('i5'))
decbtn5.place(x=1114,y=236)

#BOURNVILLE
p6=PhotoImage(file="bournville.png")
bt6=Button(win,image=p6,command=bournville,borderwidth=8,bg='green')
bt6.place(x=80,y=300)
ett5=Label(win,text='₹'+str(obj1.k[5]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett5.place(x=70,y=503)
et6=Label(win,text=obj1.i[5],font=('arialbalck',20),width=10,justify=CENTER)
et6.place(x=70,y=545)
incbtn6=Button(win,image=plus,command=lambda:obj2.increment('i6'))
incbtn6.place(x=200,y=546)
decbtn6=Button(win,image=minus,command=lambda:obj2.decrement('i6'))
decbtn6.place(x=70,y=546)

#MRBEAST
p7=PhotoImage(file="mrbeast.png")
bt7=Button(win,image=p7,command=mrbeast,borderwidth=8,bg='green')
bt7.place(x=275,y=300)
ett7=Label(win,text='₹'+str(obj1.k[6]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett7.place(x=270,y=503)
et7=Label(win,text=obj1.i[6],font=('arialbalck',20),width=10,justify=CENTER)
et7.place(x=270,y=545)
incbtn7=Button(win,image=plus,command=lambda:obj2.increment('i7'))
incbtn7.place(x=400,y=546)
decbtn7=Button(win,image=minus,command=lambda:obj2.decrement('i7'))
decbtn7.place(x=270,y=546)

#DARKCHOCOLATE
p8=PhotoImage(file="darkchocolate.png")
bt8=Button(win,image=p8,command=darkchocolate,borderwidth=8,bg='green')
bt8.place(x=475,y=300)
ett8=Label(win,text='₹'+str(obj1.k[7]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett8.place(x=475,y=503)
et8=Label(win,text=obj1.i[8],font=('arialbalck',20),width=10,justify=CENTER)
et8.place(x=475,y=545)
incbtn8=Button(win,image=plus,command=lambda:obj2.increment('i8'))
incbtn8.place(x=605,y=546)
decbtn8=Button(win,image=minus,command=lambda:obj2.decrement('i8'))
decbtn8.place(x=476,y=546)

#KITKATDARK
p9=PhotoImage(file="kitkatdark.png")
bt9=Button(win,image=p9,command=kitkatdark,borderwidth=8,bg='green')
bt9.place(x=675,y=300)
ett9=Label(win,text='₹'+str(obj1.k[8]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett9.place(x=675,y=503)
et9=Label(win,text=obj1.i[9],font=('arialbalck',20,),width=10,justify=CENTER)
et9.place(x=675,y=545)
incbtn9=Button(win,image=plus,command=lambda:obj2.increment('i9'))
incbtn9.place(x=805,y=546)
decbtn9=Button(win,image=minus,command=lambda:obj2.decrement('i9'))
decbtn9.place(x=676,y=546)

#DIARYMILKBUBBLES
p10=PhotoImage(file="diarymilkbubbles.png")
bt10=Button(win,image=p10,command=diarymilkbubbles,borderwidth=8,bg='green')
bt10.place(x=885,y=300)
ett10=Label(win,text='₹'+str(obj1.k[9]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett10.place(x=878,y=503)
et10=Label(win,text=obj1.i[9],font=('arialbalck',20,),width=10,justify=CENTER)
et10.place(x=878,y=545)
incbtn10=Button(win,image=plus,command=lambda:obj2.increment('i10'))
incbtn10.place(x=1008,y=546)
decbtn10=Button(win,image=minus,command=lambda:obj2.decrement('i10'))
decbtn10.place(x=878,y=546)

#WHITTAKERSHAZELNUT
p11=PhotoImage(file="whittakershazelnut.png")
bt11=Button(win,image=p11,command=whittakershazelnut,borderwidth=8,bg='green')
bt11.place(x=1100,y=300)
ett11=Label(win,text='₹'+str(obj1.k[10]),font=('arialbalck',20),width=10,justify=CENTER,bd=2)
ett11.place(x=1090,y=503)
et11=Label(win,text=obj1.i[10],font=('arialbalck',20,),width=10,justify=CENTER)
et11.place(x=1090,y=545)
incbtn11=Button(win,image=plus,command=lambda:obj2.increment('i11'))
incbtn11.place(x=1220,y=546)
decbtn11=Button(win,image=minus,command=lambda:obj2.decrement('i11'))
decbtn11.place(x=1091,y=546)

def crt():
    mycursor.execute('select count(*) from cart')
    fg=mycursor.fetchall()
    return fg[0][0]
        
def billing():
    if crt()!=0:
        win.destroy()
        import shopping3
    else:
        messagebox.showinfo('Info','Please Add Something To Your Cart And Move To The Billing Section')

def clear():
    obj1.i[0]=0
    obj1.i[1]=0
    obj1.i[2]=0
    obj1.i[3]=0
    obj1.i[4]=0
    obj1.i[5]=0
    obj1.i[6]=0
    obj1.i[7]=0
    obj1.i[8]=0
    obj1.i[9]=0
    obj1.i[10]=0
    et1.config(text=obj1.i[0])
    et2.config(text=obj1.i[1])
    et3.config(text=obj1.i[2])
    et4.config(text=obj1.i[3])
    et5.config(text=obj1.i[4])
    et6.config(text=obj1.i[5])
    et7.config(text=obj1.i[6])
    et8.config(text=obj1.i[7])
    et9.config(text=obj1.i[8])
    et10.config(text=obj1.i[9])
    et11.config(text=obj1.i[10])

v=[]

def cart():
    try:
        if obj1.i[0]>0 or obj1.i[1]>0 or obj1.i[2]>0 or obj1.i[3]>0 or obj1.i[4]>0 or obj1.i[5]>0 or obj1.i[6]>0 or obj1.i[7]>0 or obj1.i[8]>0 or obj1.i[9]>0 or obj1.i[10]>0:
            g='select product from cart'
            mycursor.execute(g)
            bj=mycursor.fetchall()
            for l in bj:
                v.append(l[0])
            for h in range(11):
                if obj1.j[h] in v:
                    qry='update cart set qty=qty+%s where product=%s'
                    dat=[obj1.i[h],obj1.j[h]]
                    mycursor.execute(qry,dat)
                elif obj1.i[h]>0:
                    qry='insert into cart values(%s,%s,%s)'
                    dat=[obj1.j[h],obj1.i[h],obj1.k[h]*obj1.i[h]]
                    mycursor.execute(qry,dat)
            mycon.commit()
            messagebox.showinfo("Info",'Succesfully Added to Your Cart')
            clear()
        else:
            messagebox.showinfo('Info','Please Select Some Quantity')
    except ValueError:
        messagebox.showwarning('Info','Only Numbers Should Represent The Quantity')
        clear()

def viewcart():
    fo='select product,qty from cart'
    mycursor.execute(fo)
    go=mycursor.fetchall()
    newwin=Toplevel(win)
    newwin.geometry('800x400')
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview.Heading',font=('copper',15))
    s.configure('Treeview.Heading',background='green3',foreground='black')
    s.configure('Treeview',rowheight=25)
    Label(newwin,text='Your Cart Products').pack()
    tree=ttk.Treeview(newwin,column=('c1','c2'),show='headings',height=11)
    tree.column('#1',anchor=CENTER)
    tree.heading('#1',text='Product')
    tree.column('#2',anchor=CENTER)
    tree.heading('#2',text='Quantity')
    for c in go:
        tree.insert('','end',values=(c[0],c[1]))
    tree.pack()

ico1=PhotoImage(file='cart1.png')
ic1=ico1.subsample(1,1)
ico2=PhotoImage(file='addcart1.png')
ic2=ico2.subsample(1,1)
ico3=PhotoImage(file='delete1.png')
ic3=ico3.subsample(1,1)
ico4=PhotoImage(file='bill1.png')
ic4=ico4.subsample(1,1)

view=Button(win,text='View Cart',font=('arialblack',15,'bold'),image=ic1,compound=LEFT,command=viewcart,width=140)
view.place(x=300,y=620)

addto=Button(win,text='Add to Cart',font=('arialblack',15,'bold'),image=ic2,compound=LEFT,command=cart,width=170)
addto.place(x=480,y=620)

clbtn=Button(win,text='Clear',font=('arialblack',15,'bold'),image=ic3,compound=LEFT,command=clear,width=100)
clbtn.place(x=930,y=620)

nxt=Button(win,text='Billing Section',font=('arialblack',15,'bold'),image=ic4,compound=LEFT,command=billing,width=190)
nxt.place(x=700,y=620)

win.mainloop()
