# this is a clock created by using pythons
from  tkinter import *
import datetime 

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    ap = time.strftime('%p')
    date = time.strftime ("%d")
    day = time.strftime ('%a')
    year = time.strftime ('%y')
    month = time.strftime ('%m')

    lab_hour.config(text=hr)
    lab_minute.config(text = mi)
    lab_second.config (text = sec)
    lab_ap.config(text = ap)
    lab_date.config (text = date)
    lab_day.config (text = day)
    lab_year.config (text = year)
    lab_month.config (text = month)
    lab_hr.after(200,date_time)#this function will automatically change the graphics of the hour window 
    



clock = Tk()
clock.title ("FRIDAY THE CLOCK")
clock.geometry("1000x500")
clock.config(bg="black")

lab_hour=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_hour.place(x=40,y=40,height=110,width=100)

lab_hr=Label(clock,text="hour",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_hr.place(x=20,y=150,height=50,width=140)


lab_minute=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_minute.place(x=300,y=40,height=110,width=100)

lab_min=Label(clock,text="minute",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_min.place(x=280,y=150,height=50,width=140)


lab_second=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_second.place(x=600,y=40,height=110,width=100)

lab_sec=Label(clock,text="second",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_sec.place(x=580,y=150,height=50,width=140)


lab_ap=Label(clock,text="am/pm",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_ap.place(x=860,y=40,height=110,width=100)

lab_am=Label(clock,text="am/pm",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_am.place(x=860,y=150,height=50,width=100)


lab_year=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_year.place(x=40,y=200,height=110,width=100)

lab_yea=Label(clock,text="year",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_yea.place(x=40,y=300,height=50,width=100)


lab_month=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_month.place(x=300,y=200,height=110,width=100)

lab_mont=Label(clock,text="month",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_mont.place(x=300,y=300,height=50,width=100)


lab_date=Label(clock,text="00",font = ("time new roman",60,"bold"),bg="black",fg="white")
lab_date.place(x=600,y=200,height=110,width=100)

lab_dat=Label(clock,text="date",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_dat.place(x=600,y=300,height=50,width=100)


lab_day=Label(clock,text="00",font = ("time new roman",20,"bold"),bg="black",fg="white")
lab_day.place(x=860,y=200,height=110,width=100)

lab_da=Label(clock,text="day",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_da.place(x=860,y=300,height=50,width=100)

lab_title=Label(clock,text="friday tells time",font = ("time new roman",20,"bold"),bg="black",fg="aqua")
lab_title.place(x=400,y=400,height=50,width=250)

date_time()
clock.mainloop()