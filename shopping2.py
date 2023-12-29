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
bgi=PhotoImage(file="207.png")
li=Label(win,image=bgi)
li.pack()
i=[0,0,0,0,0,0,0,0,0,0,0]
j=['Diarymilk','Fivestar','Perk','Milkybarclassic','Fabelle','Bournville','Mrbeast','Darkchocolate','Kitkatdark','Diarymilkbubbles','Whittakershazelnut']
k=[60,30,10,20,300,250,600,800,150,250,450]

plus=PhotoImage(file='plus.png')
minus=PhotoImage(file='minus.png')

def increment(a):
    if a=='i1':
        i[0]+=1
        et1.delete(0,'end')
        et1.insert(0,i[0])
    elif a=='i2':
        i[1]+=1
        et2.delete(0,'end')
        et2.insert(0,i[1])
    elif a=='i3':
        i[2]+=1
        et3.delete(0,'end')
        et3.insert(0,i[2])
    elif a=='i4':
        i[3]+=1
        et4.delete(0,'end')
        et4.insert(0,i[3])
    elif a=='i5':
        i[4]+=1
        et5.delete(0,'end')
        et5.insert(0,i[4])
    elif a=='i6':
        i[5]+=1
        et6.delete(0,'end')
        et6.insert(0,i[5])
    elif a=='i7':
        i[6]+=1
        et7.delete(0,'end')
        et7.insert(0,i[6])
    elif a=='i8':
        i[7]+=1
        et8.delete(0,'end')
        et8.insert(0,i[7])
    elif a=='i9':
        i[8]+=1
        et9.delete(0,'end')
        et9.insert(0,i[8])
    elif a=='i10':
        i[9]+=1
        et10.delete(0,'end')
        et10.insert(0,i[9])
    elif a=='i11':
        i[10]+=1
        et11.delete(0,'end')
        et11.insert(0,i[10])
    else:
        pass
    

def decrement(a):
    if a=='i1':
        if i[0]>=1:
            i[0]-=1
            et1.delete(0,'end')
            et1.insert(0,i[0])
    elif a=='i2':
        if i[1]>=1:
            i[1]-=1
            et2.delete(0,'end')
            et2.insert(0,i[1])
    elif a=='i3':
        if i[2]>=1:
            i[2]-=1
            et3.delete(0,'end')
            et3.insert(0,i[2])
    elif a=='i4':
        if i[3]>=1:
            i[3]-=1
            et4.delete(0,'end')
            et4.insert(0,i[3])
    elif a=='i5':
        if i[4]>=1:
            i[4]-=1
            et5.delete(0,'end')
            et5.insert(0,i[4])
    elif a=='i6':
        if i[5]>=1:
            i[5]-=1
            et6.delete(0,'end')
            et6.insert(0,i[5])
    elif a=='i7':
        if i[6]>=1:
            i[6]-=1
            et7.delete(0,'end')
            et7.insert(0,i[6])
    elif a=='i8':
        if i[7]>=1:
            i[7]-=1
            et8.delete(0,'end')
            et8.insert(0,i[7])
    elif a=='i9':
        if i[8]>=1:
            i[8]-=1
            et9.delete(0,'end')
            et9.insert(0,i[8])
    elif a=='i10':
        if i[9]>=1:
            i[9]-=1
            et10.delete(0,'end')
            et10.insert(0,i[9])
    elif a=='i11':
        if i[10]>=1:
            i[10]-=1
            et11.delete(0,'end')
            et11.insert(0,i[10])
    else:
        pass
    

def diarymilk():
    pass

def fivestar():
    pass

def perk():
    pass

def milkybarclassic():
    pass

def fabelle():
    pass

def bournville():
    pass

def mrbeast():
    pass

def darkchocolate():
    pass

def kitkatdark():
    pass

def diarymilkbubbles():
    pass

def whittakershazelnut():
    pass



#DIARYMILK
p1=PhotoImage(file="diarymilk.png")
bt1=Button(win,image=p1,command=diarymilk,borderwidth=8,bg='green')
bt1.place(x=70,y=60)
et1=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et1.insert(0,0)
et1.place(x=66,y=230)
incbtn1=Button(win,image=plus,command=lambda:increment('i1'))
incbtn1.place(x=205,y=236)
decbtn1=Button(win,image=minus,command=lambda:decrement('i1'))
decbtn1.place(x=70,y=236)

#5STAR
p2=PhotoImage(file="5star.png")
bt2=Button(win,image=p2,command=fivestar,borderwidth=8,bg='green')
bt2.place(x=280,y=60)
et2=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=14,justify=CENTER)
et2.insert(0,0)
et2.place(x=276,y=230)
incbtn2=Button(win,image=plus,command=lambda:increment('i2'))
incbtn2.place(x=460,y=236)
decbtn2=Button(win,image=minus,command=lambda:decrement('i2'))
decbtn2.place(x=280,y=236)

#PERK
p3=PhotoImage(file="perk.png")
bt3=Button(win,image=p3,command=perk,borderwidth=8,bg='green')
bt3.place(x=510,y=60)
et3=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=16,justify=CENTER)
et3.insert(0,0)
et3.place(x=506,y=230)
incbtn3=Button(win,image=plus,command=lambda:increment('i3'))
incbtn3.place(x=720,y=236)
decbtn3=Button(win,image=minus,command=lambda:decrement('i3'))
decbtn3.place(x=512,y=236)

#MILKYBARCLASSIC
p4=PhotoImage(file="milkybarclassic.png")
bt4=Button(win,image=p4,command=milkybarclassic,borderwidth=8,bg='green')
bt4.place(x=770,y=60)
et4=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=19,justify=CENTER)
et4.insert(0,0)
et4.place(x=770,y=230)
incbtn4=Button(win,image=plus,command=lambda:increment('i4'))
incbtn4.place(x=1030,y=236)
decbtn4=Button(win,image=minus,command=lambda:decrement('i4'))
decbtn4.place(x=776,y=236)

#FABELLE
p5=PhotoImage(file="fabelle.png")
bt5=Button(win,image=p5,command=fabelle,borderwidth=8,bg='green')
bt5.place(x=1120,y=60)
et5=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=12,justify=CENTER)
et5.insert(0,0)
et5.place(x=1108,y=230)
incbtn5=Button(win,image=plus,command=lambda:increment('i5'))
incbtn5.place(x=1262,y=236)
decbtn5=Button(win,image=minus,command=lambda:decrement('i5'))
decbtn5.place(x=1114,y=236)

#BOURNVILLE
p6=PhotoImage(file="bournville.png")
bt6=Button(win,image=p6,command=bournville,borderwidth=8,bg='green')
bt6.place(x=80,y=300)
et6=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et6.insert(0,0)
et6.place(x=66,y=510)
incbtn6=Button(win,image=plus,command=lambda:increment('i6'))
incbtn6.place(x=205,y=516)
decbtn6=Button(win,image=minus,command=lambda:decrement('i6'))
decbtn6.place(x=70,y=516)

#MRBEAST
p7=PhotoImage(file="mrbeast.png")
bt7=Button(win,image=p7,command=mrbeast,borderwidth=8,bg='green')
bt7.place(x=275,y=300)
et7=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et7.insert(0,0)
et7.place(x=266,y=510)
incbtn7=Button(win,image=plus,command=lambda:increment('i7'))
incbtn7.place(x=405,y=516)
decbtn7=Button(win,image=minus,command=lambda:decrement('i7'))
decbtn7.place(x=270,y=516)

#DARKCHOCOLATE
p8=PhotoImage(file="darkchocolate.png")
bt8=Button(win,image=p8,command=darkchocolate,borderwidth=8,bg='green')
bt8.place(x=475,y=300)
et8=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et8.insert(0,0)
et8.place(x=470,y=510)
incbtn8=Button(win,image=plus,command=lambda:increment('i8'))
incbtn8.place(x=610,y=516)
decbtn8=Button(win,image=minus,command=lambda:decrement('i8'))
decbtn8.place(x=476,y=516)

#KITKATDARK
p9=PhotoImage(file="kitkatdark.png")
bt9=Button(win,image=p9,command=kitkatdark,borderwidth=8,bg='green')
bt9.place(x=675,y=300)
et9=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et9.insert(0,0)
et9.place(x=669,y=510)
incbtn9=Button(win,image=plus,command=lambda:increment('i9'))
incbtn9.place(x=809,y=516)
decbtn9=Button(win,image=minus,command=lambda:decrement('i9'))
decbtn9.place(x=676,y=516)

#DIARYMILKBUBBLES
p10=PhotoImage(file="diarymilkbubbles.png")
bt10=Button(win,image=p10,command=diarymilkbubbles,borderwidth=8,bg='green')
bt10.place(x=885,y=300)
et10=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et10.insert(0,0)
et10.place(x=872,y=510)
incbtn10=Button(win,image=plus,command=lambda:increment('i10'))
incbtn10.place(x=1012,y=516)
decbtn10=Button(win,image=minus,command=lambda:decrement('i10'))
decbtn10.place(x=878,y=516)

#WHITTAKERSHAZELNUT
p11=PhotoImage(file="whittakershazelnut.png")
bt11=Button(win,image=p11,command=whittakershazelnut,borderwidth=8,bg='green')
bt11.place(x=1100,y=300)
et11=Entry(win,font=('arialbalck',20,),highlightthickness=6, highlightbackground="red",width=11,justify=CENTER)
et11.insert(0,0)
et11.place(x=1085,y=510)
incbtn11=Button(win,image=plus,command=lambda:increment('i11'))
incbtn11.place(x=1225,y=516)
decbtn11=Button(win,image=minus,command=lambda:decrement('i11'))
decbtn11.place(x=1090,y=516)


def billing():
    win.destroy()
    import shopping3

def clear():
    i[0]=0
    i[1]=0
    i[2]=0
    i[3]=0
    i[4]=0
    i[5]=0
    i[6]=0
    i[7]=0
    i[8]=0
    i[9]=0
    i[10]=0
    et1.delete(0,'end')
    et1.insert(0,i[0])
    et2.delete(0,'end')
    et2.insert(0,i[1])
    et3.delete(0,'end')
    et3.insert(0,i[2])
    et4.delete(0,'end')
    et4.insert(0,i[3])
    et5.delete(0,'end')
    et5.insert(0,i[4])
    et6.delete(0,'end')
    et6.insert(0,i[5])
    et7.delete(0,'end')
    et7.insert(0,i[6])
    et8.delete(0,'end')
    et8.insert(0,i[7])
    et9.delete(0,'end')
    et9.insert(0,i[8])
    et10.delete(0,'end')
    et10.insert(0,i[9])
    et11.delete(0,'end')
    et11.insert(0,i[10])

v=[]

def cart():
    try:
        if int(et1.get())>0 or int(et2.get())>0 or int(et3.get())>0 or int(et4.get())>0 or int(et5.get())>0 or int(et6.get())>0 or int(et7.get())>0 or int(et8.get())>0 or int(et9.get())>0 or int(et10.get())>0 or int(et11.get())>0:
            g='select product from cart'
            mycursor.execute(g)
            bj=mycursor.fetchall()
            for l in bj:
                v.append(l[0])
            for h in range(11):
                if j[h] in v:
                    qry='update cart set qty=qty+%s where product=%s'
                    dat=[i[h],j[h]]
                    mycursor.execute(qry,dat)
                elif i[h]>0:
                    qry='insert into cart values(%s,%s,%s)'
                    dat=[j[h],i[h],k[h]*i[h]]
                    mycursor.execute(qry,dat)
            mycon.commit()
            messagebox.showinfo("Info",'Succesfully Added to Your Cart')
            clear()
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
