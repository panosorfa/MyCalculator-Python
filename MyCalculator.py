from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import math
window = ThemedTk(theme='breeze')

window.title("calculator")
window.geometry('390x320')

result = ""
equation = StringVar()

def press(x) :
    global result
    result = result+str(x)
    equation.set(result)

def equalpress():
    try:
        global result
        total=str(eval(result))
        equation.set(total)
        result=""
    except:
        equation.set("error")
        result=""

def clear():
    global result
    result=""
    equation.set("")
def delete():
    global equation,result,txt1
    txt1.delete(len(txt1.get())-1)
    equation.set(equation.get()[:-1])
    result= (equation.get())
txt1 = Entry(window, width=10, fg='red', bg='white', font=('Times', 25), cursor="dot", relief='solid', text=equation)
txt1.place(x=100 , y=0)
button7 = ttk.Button(window, text='7', cursor="dot",command=lambda :press(7))
button7.place(x=0 , y=50)
button4 = ttk.Button(window, text='4', cursor="dot",command=lambda :press(4))
button4.place(x=0 , y=80)
button1 = ttk.Button(window, text='1', cursor="dot",command=lambda :press(1))
button1.place(x=0 , y=110)
buttonc = ttk.Button(window, text='C', cursor="dot",command=clear )
buttonc.place(x=0 , y=140)
button0 = ttk.Button(window, text='0', cursor="dot",command=lambda :press(0))
button0.place(x=95 , y=140)
button8 = ttk.Button(window, text='8', cursor="dot",command=lambda :press(8))
button8.place(x=95 , y=50)
button5 = ttk.Button(window, text='5', cursor="dot",command=lambda :press(5))
button5.place(x=95 , y=80)
button2 = ttk.Button(window, text='2', cursor="dot",command=lambda :press(2))
button2.place(x=95 , y=110)
button9 = ttk.Button(window, text='9', cursor="dot",command=lambda :press(9))
button9.place(x=190 , y=50)
button6 = ttk.Button(window, text='6', cursor="dot",command=lambda :press(6))
button6.place(x=190 , y=80)
button3 = ttk.Button(window, text='3', cursor="dot",command=lambda :press(3))
button3.place(x=190 , y=110)
button3 = ttk.Button(window, text=',', cursor="dot",command=lambda :press(","))
button3.place(x=190 , y=140)
button = ttk.Button(window, text='+', cursor="dot",command=lambda :press("+"))
button.place(x=285 , y=50)
button = ttk.Button(window, text='-', cursor="dot",command=lambda :press("-"))
button.place(x=285 , y=80)
button = ttk.Button(window, text='*', cursor="dot",command=lambda :press("*"))
button.place(x=285 , y=110)
button = ttk.Button(window, text='/', cursor="dot",command=lambda :press("/"))
button.place(x=285 , y=140)
button = ttk.Button(window, text='=', cursor="dot",width=51,command=equalpress)
button.place(x=0 , y=220)
button = ttk.Button(window, text='(', cursor="dot",command=lambda :press("("))
button.place(x=0 , y=180)
button = ttk.Button(window, text=')', cursor="dot",command=lambda :press(")"))
button.place(x=285 , y=180)
button = ttk.Button(window, text='^', cursor="dot",command=lambda :press("**"))
button.place(x=95 , y=180)
button9 = ttk.Button(window, text='√', cursor="dot",command=lambda :press("math.sqrt("))
button9.place(x=190 , y=180)
button10 = ttk.Button(window, text='Delete', cursor="dot",width=10,command=delete)
button10.place(x=285 , y=5)
def first():
    button = ttk.Button(window, text='close', cursor="dot",width=25, command=close )
    button.place(x=95 , y=260)

def close():
    window.destroy()

first()
window.mainloop()

