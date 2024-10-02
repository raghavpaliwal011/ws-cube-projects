# making a translater using python
from tkinter import *
from tkinter import ttk # -- this function will import combobox
from googletrans import Translator,LANGUAGES
# combobox = window like app

def change(text="hello",src="english",dest="sanskrit"):
    text1 = text
    src1 = src
    dest1=dest
    trans = Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    mesg=sor_txt.get(1.0,END)
    textget = change(text = mesg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert (END,textget)

root = Tk()
root.title("Friday translates") # this function sets the title of the combobox as its name suggests
root.geometry("500x700")
root.config(bg="black")

lab_txt=Label(root,text="source text",font=("Time New Roman",20,"bold"),bg="black",fg="white")
lab_txt.place(x=500,y=40,height=100,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Friday translates",font=("Time New Roman",20,"bold"),bg="black",fg = "white")
lab_txt.place(x=500,y=20,height=40,width=300)

sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=120,height=100,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value = list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

button_change = Button(frame,text="translate",relief=RAISED,command=data)
button_change.place(x = 120,y=300,height=40,width=100)

comb_dest = ttk.Combobox(frame,value = list_text)
comb_dest.place(x=230,y=300,height=40,width=100)
comb_dest.set("english")

lab_txt=Label(root,text="destination",font=("Time New Roman",20,"bold"),bg="black",fg = "white")
lab_txt.place(x=500,y=360,height=20,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

comb_dest.set("hindi")
root.mainloop()