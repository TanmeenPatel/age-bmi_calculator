import datetime
import tkinter as tk

window=tk.Tk()
window.geometry("600x600")
window.title(" Age and BMI Calculator ")

name = tk.Label(text = "Name")
name.grid(column = 0, row = 1)
#---------------------------------------
year = tk.Label(text = "Year")
year.grid(column = 0, row = 2)
#---------------------------------------
month = tk.Label(text = "Month")
month.grid(column = 0, row = 3)
#---------------------------------------
date = tk.Label(text = "Day")
date.grid(column = 0, row = 4)
#---------------------------------------
height = tk.Label(text = "Height")
height.grid(column = 0, row = 5)
#---------------------------------------
weight = tk.Label(text = "Weight")
weight.grid(column = 0, row = 6)


nameEntry = tk.Entry()
nameEntry.grid(column = 1, row = 1)
#---------------------------------------
yearEntry = tk.Entry()
yearEntry.grid(column = 1, row = 2)
#---------------------------------------
monthEntry = tk.Entry()
monthEntry.grid(column = 1,row = 3)
#---------------------------------------
dateEntry = tk.Entry()
dateEntry.grid(column = 1, row = 4)
#---------------------------------------
heightEntry = tk.Entry()
heightEntry.grid(column = 1, row = 5)
#---------------------------------------
weightEntry = tk.Entry()
weightEntry.grid(column = 1, row = 6)

def getBMI():
    name = nameEntry.get()
    height = float(heightEntry.get())
    weight = float(weightEntry.get())
    bmi_long = weight/(height**2)*10000
    bmi_short = round(bmi_long,2)
    textarea = tk.Text(master = window, height = 5, width = 40)
    textarea.grid(column = 1, row = 10)
    ANSWER = "Hey {name}, your Body Mass Index value is {bmi}".format(name=name, bmi=bmi_short)
    textarea.insert(tk.END, ANSWER)

def getAge():
    name=nameEntry.get()
    person = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=window,height=5,width=40)
    textArea.grid(column = 1, row = 10)
    answer = " Hey {person}, you are {age} years old!".format(person=name, age=person.age())
    textArea.insert(tk.END, answer)

button = tk.Button(window, text="Calculate Age", command = getAge, bg="pink").grid(column = 1, row = 7)
button = tk.Button(window, text="Calculate BMI", command = getBMI, bg="#bbb2e9").grid(column = 1, row = 8)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

'''image=Image.open('app_image.jpeg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)'''
window.mainloop()
