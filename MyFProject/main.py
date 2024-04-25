from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy
import random
import time
window = Tk()
icon1 = PhotoImage(file="image\lock.png")
window.iconphoto(True, icon1)
window.title('Login')
window.geometry('925x500')
window.resizable(False, False)
img = PhotoImage(file="image\image2.png")
window.configure(bg='#fff')
Label(window, image=img, bg='white').place(x=50, y=65)
frame = Frame(window, width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading = Label(frame, text='Sign in', fg='#07f572', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
def action():
    frame3.tkraise()
def visualiser():
    global c
    global filename
    a1 = float(week1.get())
    a2 = float(week2.get())
    a3 = float(week3.get())
    a4 = float(week4.get())
    c = random.randint(1,1000)
    filename = f"image/mypng{c}.png"
    liste_x = numpy.array([1,2,3,4])
    liste_y = numpy.array([a1,a2,a3,a4])

    plt.figure(figsize=(4, 3))
    plt.plot(liste_x,liste_y)
    plt.title('Développement de poids')
    plt.xlabel("Semaine")
    plt.ylabel("Pound")
    plt.savefig(filename)
    about_button = Button(frame2, text='Graphe', font=('Arial', 17, 'bold'), border=0, bd=4, command=graph)
    about_button.place(x=210, y=26)
def myinfo():
    global image5
    global image6
    global image7
    image5 = PhotoImage(file="image\\noraml.png")
    image6 = PhotoImage(file="image\weekfinaly.png")
    image7 = PhotoImage(file="image\overweight.png")
    if weight.get()=="" or height.get()=="" or week1.get()=="" or week2.get()=="" or week3.get()=="" or week4.get()=="":
        messagebox.showinfo(message="Please complete all the form",title="Empty data")
    else:
        about_button = Button(frame2, text='MyInfo', font=('Arial', 17, 'bold'), border=0, bd=4, command=accct)
        about_button.place(x=110, y=26)
    P = int(weight.get())
    H = int(height.get())
    sex = x.get()
    ag = int(age.get())
    bmi = float((P/(H*10**(-2))**2).__format__(".2f"))
    if sex=="male":
        tdee = float((88.362+(13.397*P)+(4.799*H)-(5.677*ag)).__format__(".2f"))
    else:
        tdee = float((447.593 + (9.247*P)+(3.098*H) - (4.330*ag)).__format__(".2f"))
    Label(frame4,text="Your BMI  = ", fg='blue', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=100,y=30)
    Label(frame4,text=bmi, fg='green', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=240,y=30)
    Label(frame4,text="Your TDEE  = ", fg='blue', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=100,y=70)
    Label(frame4,text=tdee, fg='green', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=240,y=70)
    if bmi < 18.5:
        Label(frame4, image=image6, bg="#e6ccff").place(x=390, y=30)
        Label(frame4, text="You are underweight        ", bg='#e6ccff', font=('Arial', 13, 'bold'), fg='green').place(
            x=380, y=230)
    elif bmi >= 18.5 and bmi < 25:
        Label(frame4,image=image5,bg="#e6ccff").place(x=390,y=30)
        Label(frame4,text="You have a normal weight",bg='#e6ccff', font=('Arial', 13, 'bold'),fg='green').place(x=380,y=230)
    else:
        Label(frame4, image=image7, bg="#e6ccff").place(x=390, y=30)
        Label(frame4,text="You have an over weight        ",bg='#e6ccff', font=('Arial', 13, 'bold'),fg='green').place(x=380,y=230)
    Button(frame4,text="Visualisation de poid",bg='#e6ccff',font=('Arial', 13, 'bold'),command=visualiser).place(x=150,y=110)


def accct():
    frame4.tkraise()
    frame4.place(x=0, y=110)
def graph():
    frame6.tkraise()
    frame6.place(x=0, y=110)
    global imag7
    imag7 = PhotoImage(file=filename)
    Label(frame6,image=imag7,bg="#e6ccff").place(x=130,y=5)
def account():
    global frame3
    global frame4
    global frame6
    global frame2
    global image2
    global image3
    global frame5
    global image4
    global x
    global weight,height,week1,week2,week3,week4
    global age
    sub = Toplevel()
    image2 = PhotoImage(file="image\\trees.png")
    image3 = PhotoImage(file="image\\trees.png")
    image4 = PhotoImage(file="image\\new.png")
    sub.title('Welcome to fit tracker app')
    sub.geometry('700x500')
    sub.config(bg='#e6ccff')
    sub.resizable(False, False)
    icon = PhotoImage(file="image\sport.png")
    window.iconphoto(True, icon)
    frame5 = Frame(sub, width=700,height=4,bg='green')
    frame2 = Frame(sub, width=350, height=102, bg='#e6ccff')
    Label(sub, image=image2, bg='#e6ccff').place(x=550, y=0)
    Label(sub, image=image3, bg='#e6ccff').place(x=15, y=0)
    frame3 = Frame(sub, width=750, height=500, bg='#e6ccff')
    frame4 = Frame(sub, width=750, height=500, bg='#e6ccff')
    frame6 = Frame(sub, width=750, height=500, bg='#e6ccff')
    home_button = Button(frame2, text='Home', font=('Arial', 17, 'bold'), border=0, bd=4, command=action)
    frame2.place(x=170, y=0)
    frame5.place(x=0,y=104)
    home_button.place(x=10, y=26)
    frame3.place(x=0, y=110)
    Label(frame3,text="Please complete the form : ",font=('Arial', 12, 'bold'),bg='#e6ccff',fg='red').place(x=400,y=0)
    Label(frame3, text=" Your age : ", font=('Arial', 14, 'bold'),
          bg='#e6ccff',fg='black').place(x=10, y=20)
    age = Entry(frame3,font=('Arial',14,'bold'),width=5)
    age.place(x=140,y=20)
    Label(frame3,image=image4,bg='#e6ccff').place(x=410,y=30)
    Label(frame3,text="Your gender : ",fg='black',bg='#e6ccff',font=('Arial',14,'bold')).place(x=10,y=55)
    x = StringVar()
    Radiobutton(frame3,text='Male',variable=x,value='male',bg='#e6ccff',font=('Arial',14,'bold')).place(x=200,y=55)
    Radiobutton(frame3,text='Female',variable=x,value='Female',bg='#e6ccff',font=('Arial',14,'bold')).place(x=280,y=55)
    Label(frame3,text="Your Weight en KG: ",fg='black',bg='#e6ccff',font=('Arial',14,'bold')).place(x=10,y=95)
    weight = Entry(frame3,font=('Arial',14,'bold'),width=5)
    weight.place(x=260, y=95)
    Label(frame3, text="Your height en Cm: ", fg='black', bg='#e6ccff', font=('Arial', 14, 'bold')).place(x=10, y=135)
    height = Entry(frame3,font=('Arial',14,'bold'),width=5)
    height.place(x=260,y=135)
    Label(frame3, text="Your weight during the last month :", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=90, y=170)
    Label(frame3,text="week1 : ",fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120,y=200)
    week1=Entry(frame3,font=('Arial',13,'bold'),width=5)
    week1.place(x=190,y=200)
    Label(frame3, text="week2 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=240)
    week2 = Entry(frame3, font=('Arial', 13, 'bold'), width=5)
    week2.place(x=190, y=240)
    Label(frame3, text="week3 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=280)
    week3 = Entry(frame3, font=('Arial', 13, 'bold'), width=5)
    week3.place(x=190, y=280)
    Label(frame3, text="week4 : ", fg='black', bg='#e6ccff', font=('Arial', 13, 'bold')).place(x=120, y=320)
    week4 = Entry(frame3,font=('Arial', 13, 'bold'), width=5)
    week4.place(x=190, y=320)
    submit = Button(frame3,text='submit',bg='#e6ccff',bd='2',font=('Arial', 14, 'bold'),command=myinfo)
    submit.place(x=450,y=330)

def sign_in():
    if user.get() == 'omar' and code.get() == 'sabor':
        account()
    elif user.get() in ["Username", ''] or code.get() in ['Password', '']:
        messagebox.showinfo(title='erreu', message="Donner manquant")
    else:
        messagebox.showerror(title='incorrect info', message='mot de passe ou username incorrect')


def on_enter(a):
    user.delete(0, 'end')


def on_leave(a):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


def on_enterr(a):
    code.delete(0, 'end')
    code.config(show='*')


def on_leavee(a):
    name = code.get()
    if name == '':
        code.config(show='')
        code.insert(0, 'Password')


##################-----------------------------
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
##################-----------------------------
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enterr)
code.bind('<FocusOut>', on_leavee)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=180)
##################-----------------------------
Button(frame, width=39, pady=7, text='Sign in', bg='#07f572', fg='white', border=0, command=sign_in).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)
##################-----------------------------
window.mainloop()
