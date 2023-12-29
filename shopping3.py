import tkinter
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
win=tkinter.Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.configure(height=h,width=w)

mycon=mysql.connector.connect(host='localhost',user='root',password='pass',database='choco')
mycursor=mycon.cursor()
'''
mycursor.execute('drop table if exists cart')
mycursor.execute('create table cart(product varchar(20),qty integer(3),cost integer(10))')
'''
win.title("ShoppingProject")
bgi=tkinter.PhotoImage(file="207.png")
li=tkinter.Label(win,image=bgi)
li.pack()

s=ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',font=('copper',15))
s.configure('Treeview.Heading',background='green3',foreground='black')
s.configure('Treeview',rowheight=28)

tree=ttk.Treeview(win, column=("c1", "c2","c3"), show='headings', height=11,selectmode='browse')
tree['columns']=('ProductName','Quantity','Cost')
tree.column('#0',width=0,stretch='NO')
tree.column('#1',anchor='center')
tree.column('#2',anchor='center')
tree.column('#3',anchor='center')

tree.heading('#0',text='')
tree.heading('#1',text='ProductName')
tree.heading('#2',text='Quantity')
tree.heading('#3',text='Cost')

fo='select * from cart'
mycursor.execute(fo)
go=mycursor.fetchall()

tot=[0,0]

for c in go:
    tot[0]+=c[1]
    tot[1]+=c[2]
    tree.insert('','end',values=(c[0],c[1],c[2]))
tree.pack()

def totlabel():
    mycursor.execute('select sum(qty),sum(cost) from cart')
    go=mycursor.fetchall()
    for c in go:
        tot[0]=c[0]
        tot[1]=c[1]
    lbl2.config(text=tot[0])
    lbl3.config(text=tot[1])

lbl1=Label(win,text='Total',font=('courier',15,'bold'),width=15)
lbl1.place(x=380,y=400)
lbl2=Label(win,text=tot[0],font=('courier',15,'bold'),width=16)
lbl2.place(x=580,y=400)
lbl3=Label(win,text=tot[1],font=('courier',15,'bold'),width=16)
lbl3.place(x=786,y=400)

tree.selection_clear()

plus=PhotoImage(file='plus.png')
minus=PhotoImage(file='minus.png')

j=['Diarymilk','Fivestar','Perk','Milkybarclassic','Fabelle','Bournville','Mrbeast','Darkchocolate','Kitkatdark','Diarymilkbubbles','Whittakershazelnut']
k=[40,20,10,15,1500,150,3499,140,50,200,899]



def rem():
    x=tree.selection()
    q=[0,1,0]
    d=[0,0]
    newwin=Toplevel(win)
    newwin.geometry('250x160+560+300')
    lbr=Label(newwin,text='Enter New Quantity',font=(20)).place(x=58,y=10)
    entr=Entry(newwin,width=10,font=('courier',20),justify=CENTER)
    entr.insert(0,1)
    entr.place(x=45,y=40)
    def troy():
        if q[1]>0:
            qry='update cart set qty=%s,cost=%s where product=%s'
            s=j.index(d[0])
            q[2]=k[s]*q[1]
            dat=[q[1],q[2],d[0]]
            mycursor.execute(qry,dat)
            for n in j:
                if n==d[0]:
                    o=j.index(n)
                    break
            tree.item(x,text='',values=(d[0],q[1],k[o]*q[1]))
            mycon.commit()
            newwin.destroy()
        elif q[1]==0:
            for b in x:
                pass
            qry='delete from cart where product=%s'
            dat=[d[0]]
            mycursor.execute(qry,dat)
            tree.delete(b)
            if len(tree.get_children())==0:
                lbl2.config(text=0)
                lbl3.config(text=0)
            newwin.destroy()
            mycon.commit()
        totlabel()
    def increment(a):
        if a=='i1':
            if int(entr.get())<q[0]:
                q[1]+=1
                entr.delete(0,'end')
                entr.insert(0,q[1])
    def decrement(a):
        if a=='i1':
            if int(entr.get())>0:
                q[1]-=1
                entr.delete(0,'end')
                entr.insert(0,q[1])

    b=tree.item(x)
    c=b.get('values')
    d[0]=c[0]
    q[0]=c[1]
    
    incbtn=Button(newwin,image=plus,command=lambda:increment('i1'))
    incbtn.place(x=173,y=40)
    decbtn=Button(newwin,image=minus,command=lambda:decrement('i1'))
    decbtn.place(x=45,y=40)
    okb=Button(newwin,text='Ok',font=(20),width=8,command=troy)
    okb.place(x=85,y=110)
    mycon.commit()

def selec(y):
    try:
        tree.selection_remove(y)
    except:
        a=tree.get_children()
        tree.selection_remove(a)

a=tree.get_children()

ico1=PhotoImage(file='tick.png')
ic1=ico1.subsample(1,1)
ico2=PhotoImage(file='exit.png')
ic2=ico2.subsample(1,1)

def clear_all():
   for item in tree.get_children():
      tree.delete(item)

def purchase():
    messagebox.showinfo('Info','Purchase Complete')
    clear_all()
    lbl2.config(text=0)
    lbl3.config(text=0)

    
def gpay():
    pass

br=PhotoImage(file='purchase.png')
bt4=Button(win,image=br,command=purchase)
bt4.place(x=810,y=436)
br1=PhotoImage(file='gpay.png')
bt5=Button(win,image=br1,command=gpay)
bt5.place(x=575,y=445)



bt3=Button(win,text='Deselect All',font=('courier',15,'bold'),image=ic1,compound=LEFT,command=lambda : selec(a),width=200)
bt3.place(x=575,y=570)
bt2=Button(win,text='Want to Remove Products Select And Click Here',font=('courier',15,'bold'),width=50,command=rem)
bt2.place(x=378,y=510)

def ex():
    messagebox.showinfo('Info','Thank You Visit Again')
    win.destroy()
    

bt1=Button(win,text='Exit',font=('helvetica',18,'bold'),image=ic2,compound=LEFT,command=ex,width=210)
bt1.place(x=570,y=630)

tree.place(x=380,y=50)

win.mainloop()

    
