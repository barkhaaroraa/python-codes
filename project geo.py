
#import pandas as pd 

import tkinter as tk
import * from tk
def pharmacyy():
  window = tk.ABC()
  window.geometry("400x400")
  def code():
      import geocoder
      import geopy.distance
      g = geocoder.ip("me")
      a=g.latlng
      phar1=(28.6433, 77.2125)
      phar2=(28.6245, 77.2190)
      phar3=(28.6530, 77.2162)
      dis1=geopy.distance.geodesic(a,phar1).km
      dis2=geopy.distance.geodesic(a,phar2).km
      dis3=geopy.distance.geodesic(a,phar3).km
      return dis1,dis2,dis3
      
  def codeplot():
      lst=[]
      distances=code()
      for i in distances:
          lst.append(i)
      return lst
  def codedisplay():
      showup = codeplot()
      text = tk.Text(master=window, height=10, width=30)
      text.grid(column=0, row=5)
      text.insert(tk.END, showup)

  label_head = tk.Label(text=" LOCATE YOUR NEARBY PHARMACY ", font=("The New Roman", 25))
  label_head.grid()

  label_enter = tk.Label(text=" Locating the distance between you and the pharmacy ")
  label_enter.grid(column=0, row=1)

  button_submit = tk.Button(text="Generate", bg="green", command=codedisplay)
  button_submit.grid(column=0, row=11)


def buttons():
    root=tk.Tk()
    l=tk.Label(root,text="CLICK ON THE SYMPTOMS YOU ARE EXPERIENCING:",fg="saddle brown", bg="khaki")
    l.config(font=("Times",20,"bold roman"))
    l.pack()
    root.geometry("500x500")
    root.config(background="khaki")
    tk.Button(root, text='Fever/Chills',bg='sandy brown',fg='saddle brown',activebackground='white',height = 4, width=10, font=1, command=lambda: select("Fever/Chills")).place(x=50, y=50)
    tk.Button(root, text='Cough',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10, font=1,command=lambda: select('Cough')).place(x=200,y=50)
    tk.Button(root, text='Fatigue',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10,font=1,command=lambda: select('Fatigue')).place(x=350,y=50)
    tk.Button(root, text='Difficulty Breathing',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4, width=20,font=1,command=lambda: select('Difficulty breathing')).place(x=500,y=50)
    tk.Button(root, text='Muscle/Body aches',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=20,font=1,command=lambda: select('Muscle/Body aches')).place(x=50,y=200)
    tk.Button(root, text='Headache',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10,font=1,command=lambda: select('Headache')).place(x=305,y=200)
    tk.Button(root, text='Loss of Taste/Smell',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=20,font=1,command=lambda: select('Loss of Taste/Smell')).place(x=450,y=200)
    tk.Button(root, text='Sore Throat',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10,font=1,command=lambda: select('Sore Throat')).place(x=50,y=350)
    tk.Button(root, text='Congestion/Runny Nose',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=20,font=1,command=lambda: select('Congestion/Runny Nose')).place(x=200,y=350)
    tk.Button(root, text='Nausea',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10,font=1,command=lambda: select('Nausea')).place(x=460,y=350)
    tk.Button(root, text='Diarrhea',bg='sandy brown',fg='saddle brown',activebackground='white', height = 4,width=10,font=1,command=lambda: select('Diarrhea')).place(x=610,y=350)
    tk.Button(root,text="Submit",bg='red',activebackground='white', height = 2,width=10,font=1,command=root.destroy).place(x=330,y=500)
    root.mainloop()

def progress():
    global set
    ws=tk.abc()
    ws.geometry('500x500')
    set = ttk.Treeview(ws)
    set.pack()
    set['columns']= ('date', 'name','spo2','fever','heartrate')
    set.column("#0", width=0, stretch=NO)
    set.column("date",anchor=CENTER, width=80)
    set.column("name",anchor=CENTER, width=80)
    set.column("spo2",anchor=CENTER, width=75)
    set.column("fever",anchor=CENTER, width=85)
    set.column("heartrate",anchor=CENTER, width=80)
    set.heading("#0",text="",anchor=CENTER)
    set.heading("date",text="DATE",anchor=CENTER)
    set.heading("name",text="NAME",anchor=CENTER)
    set.heading("spo2",text="SPO2",anchor=CENTER)
    set.heading("fever",text="TEMPERATURE(F)",anchor=CENTER)
    set.heading("heartrate",text="HEART RATE",anchor=CENTER)
    data = [
        ["20/01/22","ISHITA","95","96.4","72"],
        ["21/01/22","ISHITA","97","96.4","75"]
        ]
    global count
    count=0
    for record in data:
        set.insert(parent='',index='end',iid = count,text='',values=(record[0],record[1],record[2],record[3],record[4]))
        count += 1
    Input_frame = Frame(ws)
    Input_frame.pack()
    date = Label(Input_frame,text="DATE")
    date.grid(row=0,column=0)
    name= Label(Input_frame,text="NAME")
    name.grid(row=0,column=1)
    spo2 = Label(Input_frame,text="SPO2")
    spo2.grid(row=0,column=2)
    fever = Label(Input_frame,text="TEMPERATURE")
    fever.grid(row=0,column=3)
    heartrate = Label(Input_frame,text="HEART RATE")
    heartrate.grid(row=0,column=4)
    date_entry = Entry(Input_frame)
    date_entry.grid(row=1,column=0)
    name_entry = Entry(Input_frame)
    name_entry.grid(row=1,column=1)
    spo2_entry = Entry(Input_frame)
    spo2_entry.grid(row=1,column=2)
    fever_entry = Entry(Input_frame)
    fever_entry.grid(row=1,column=3)
    heartrate_entry = Entry(Input_frame)
    heartrate_entry.grid(row=1,column=4)
    def input_record():
        global count
        set.insert(parent='',index='end',iid = count,text='',values=(date_entry.get(),name_entry.get(),spo2_entry.get(),fever_entry.get(),heartrate_entry.get()))
        count += 1
        date_entry.delete(0,END)
        name_entry.delete(0,END)
        spo2_entry.delete(0,END)
        fever_entry.delete(0,END)
        heartrate_entry.delete(0,END)
    Input_button = Button(ws,text = "Input data",command= input_record)
    Input_button.pack()
    ws.mainloop() 

def user():
    master=tk.Tk()
    master.geometry("300x300")
    l1=Label(master,text='Name',font=(14))
    l2=Label(master,text='Age',font=(14))
    l3=Label(master,text='Vaccinationstatus',font=(14))
    l1.grid(row=0,column=0,padx=5,pady=5)
    l2.grid(row=1,column=0,padx=5,pady=5)
    l3.grid(row=2,column=0,padx=5,pady=5)
    Name=StringVar()
    Age=StringVar()
    VaccinationStatus=StringVar()
    t1=Entry(master,textvariable=Name,font=(16))
    t2=Entry(master,textvariable=Age,font=(16))
    t3=Entry(master,textvariable=VaccinationStatus,font=(16))
    t1.grid(row=0,column=1)
    t2.grid(row=1,column=1)
    t3.grid(row=2,column=1)
    print(t1,type)
    def enter():
        master.destroy()
    A1=Button(master,command=enter,text='Login',font=(14))
    A1.grid(row=3,column=1,sticky=W)
    def cancel():
        status=messagebox.askyesno(message='Do you want to close the window?')
        if status==True:
            master.destroy()
        master.mainloop()
    A2=Button(master,command=cancel,text='Cancel',font=(14))
    A2.grid(row=3,column=1,sticky=E)
    Myname=Name.get()
    MYAge=Age.get()
    Vaccination=VaccinationStatus.get()
    Name.set("")
    Age.set("")
    VaccinationStatus.set("")
user()
f=tk.Tk()
l=tk.Label(f,text="SELECT A CHOICE TO PROCEED WITH",fg="white", bg="black")
l.config(font=("Times",27,"bold roman"))
l.pack()
f.geometry("500x500")
myFont = font.Font(family='Times', size=20, weight='bold')
f.config(background="black")
button2=tk.Button(f, text='SELF DIAGNOSIS',bg='khaki',activebackground='white', height=5, width=15, command=buttons)
button2['font']=myFont
button3=tk.Button(f, text='DAILY CHART',bg='lightblue',activebackground='white', height=5, width=15, command=progress)
button3['font']=myFont
button4=tk.Button(f, text='NEARBY PHARMACY',bg='light green',activebackground='white', height=5, width=18, command=pharmacyy)
button4['font']=myFont
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
f.mainloop()

