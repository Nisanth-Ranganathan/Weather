from tkinter import*
import requests
import json


root=Tk()
root.title("Weather Forecast")
#creating Entry
e1=Entry(root,width=30,bd=4)
e1.grid(row=0,column=1,padx=4,pady=4)

label2 = Label(root)
label3 = Label(root)
label4 = Label(root)
label5 = Label(root)
label6 = Label(root)

def forecast():
    try:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=38df4619b32201310feb55bf680ee2bc&q="+e1.get())
        api = json.loads(api_request.content)

        v1 = var1.get()
        v2 = var2.get()
        v3 = var3.get()
        v4 = var4.get()
        v5 = var5.get()
        global label2
        global label3
        global label4
        global label5
        global label6

        b1["state"]=DISABLED

        if v1 == 1:
            Temperature = api["main"]["temp"]
            C = Temperature - 273.15
            label2 = Label(root, text="Temperature in (Celsius unit) = " + str(C))
            label2.grid(row=7, column=0,columnspan=2)


        if v2 == 1:
            Pressure = api["main"]["pressure"]
            label3 = Label(root, text="Pressure in (hpa unit) = " + str(Pressure))
            label3.grid(row=8, column=0,columnspan=2)

        if v3 == 1:
            Humidity = api["main"]["humidity"]
            label4 = Label(root, text="Humidity here is = " + str(Humidity))
            label4.grid(row=9, column=0,columnspan=2)

        if v4 == 1:
            Description = api["weather"][0]["description"]
            label5 = Label(root, text="Weather description in = " + Description)
            label5.grid(row=10, column=0,columnspan=2)
        if v5 == 1:
            Speed = api["wind"]["speed"]
            label6 = Label(root, text="Wind Speed is " + str(Speed) + str("m/s"))
            label6.grid(row=11, column=0,columnspan=2)

    except Exception as e:
        api = "Error"

def Delete():
    frame = LabelFrame(root)
    label2.grid_forget()
    label3.grid_forget()
    label4.grid_forget()
    label5.grid_forget()
    label6.grid_forget()
    b1["state"] = NORMAL

#Creating label
label1=Label(root,text="Enter the City",font=("Times new roman",10,"bold"))
label1.grid(row=0,column=0,padx=4,pady=4)

#declaring check button variable type

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()

#creating check button
cb=Checkbutton(root,text="Temp",variable=var1,onvalue=1,offvalue=0,anchor=W)
cb.grid(row=2,column=0,sticky=W)
cb1=Checkbutton(root,text="Pressure",variable=var2,onvalue=1,offvalue=0,anchor=W)
cb1.grid(row=3,column=0,sticky=W)
cb2=Checkbutton(root,text="Humidity",variable=var3,onvalue=1,offvalue=0,anchor=W)
cb2.grid(row=4,column=0,sticky=W)
cb3=Checkbutton(root,text="Description",variable=var4,onvalue=1,offvalue=0,anchor=W)
cb3.grid(row=5,column=0,sticky=W)
cb4=Checkbutton(root,text="Speed",variable=var5,onvalue=1,offvalue=0,anchor=W)
cb4.grid(row=6,column=0,sticky=W)

#creating button

b1=Button(root,text="Generate",width=10,command=forecast)
b1.grid(row=1,column=0,padx=6,pady=6)

Delete_button=Button(root,text="Delete",width=10,command=Delete)
Delete_button.grid(row=1,column=1,padx=0,pady=6)


root.mainloop()