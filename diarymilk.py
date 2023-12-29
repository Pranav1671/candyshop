from tkinter import *
import webbrowser
win5=Tk()

win5.geometry('800x400')
'''
ph1=PhotoImage(file="white1.png")
lb1=Label(image=ph1)
lb1.place(x=0,y=0)

p=PhotoImage(file='diarymilk1.png')
bb2=Label(image=p)
bb2.place(x=60,y=20)
'''

def ok():
    win5.destroy()

def callback(url):
    webbrowser.open_new_tab(url)

#use pack() instead of place() to place label at the corner sides

lb3=Label(win5,text='MRP  : Rs. 40.00 /-',font=('copper',20,'bold'))
lb3.place(x=360,y=30)
lb4=Label(win5,text='Expiry Date  : JUN/23 ',font=('copper',20,'bold'))
lb4.place(x=360,y=70)
lb5=Label(win5,text='MFD  : OCT/22 ',font=('copper',20,'bold'))
lb5.place(x=360,y=110)
lb6=Label(win5,text='Inclusive of All Taxes ',font=('copper',20,'bold'))
lb6.place(x=360,y=150)
lb7=Label(win5,text='A Product By Cadbury',font=('copper',20,'bold'))
lb7.place(x=360,y=190)
lb8=Label(win5,text='For Further Details Click Below',font=('copper',20,'bold'))
lb8.place(x=360,y=230)

btt1=Button(win5,text='Visit Official WebPage',font=('courier',20))
btt1.place(x=360,y=270)
btt1.bind('<Button-1>',lambda e:callback('https://www.cadbury.co.uk/'))
btt2=Button(win5,text="OK",font=('courier',20,'bold'),width=49,bd=5,command=ok)
btt2.place(x=3,y=340)

win5.mainloop()


