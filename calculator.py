import tkinter as tk
from tkinter import *


window=tk.Tk()
window.resizable(False,False)
window.title("Calculator")
window.geometry("400x420")

result =""
update_value=""
def show(value):
    global result
  
    result= result + str(value)


    resultL.config(text=result)
 
def update_display(value):
   
    resultL.config(text=value)

def backspace():
    global result, update_value
    if result:
        result = result[:-1]
        update_value = result
        update_display(result)
   
def clear():
    global result
    result=""
    resultL.config(text=result)




def cal():
    global result 
    calculation=""
    if result !="":
        try:
        
            calculation=str(eval(result))
            result=calculation
            
        except:
            calculation="Error"
            result=""
    resultL.config(text=calculation)



resultL=Label(window,width=25,height=3,font=('Arial' ,30))
resultL.pack()
B1=Button(window,text="C",width=5,height=1,font=('Arial', 20),command=lambda:clear()).place(x=15,y=100)
B_mod=Button(window,text="%",width=5,height=1,font=('Arial', 20),command=lambda:show("%")).place(x=110,y=100)
BB=Button(window,text="\u232b",width=5,height=1,font=('Arial', 20),command=lambda:backspace()).place(x=310,y=100)
B_dot=Button(window,text=".",width=5,height=1,font=('Arial', 20),command=lambda:show(".")).place(x=210,y=100)


B2=Button(window,text="7",width=5,height=1,font=('Arial', 20),command=lambda:show("7")).place(x=15,y=160)
B3=Button(window,text="8",width=5,height=1,font=('Arial', 20),command=lambda:show("8")).place(x=110,y=160)
B4=Button(window,text="9",width=5,height=1,font=('Arial', 20),command=lambda:show("9")).place(x=210,y=160)
B_Miv=Button(window,text="x",width=5,height=1,font=('Arial', 20),command=lambda:show("*")).place(x=310,y=160)

B5=Button(window,text="4",width=5,height=1,font=('Arial', 20),command=lambda:show("4")).place(x=15,y=220)
B6=Button(window,text="5",width=5,height=1,font=('Arial', 20),command=lambda:show("5")).place(x=110,y=220)
B7=Button(window,text="6",width=5,height=1,font=('Arial', 20),command=lambda:show("6")).place(x=210,y=220)
B_Sub=Button(window,text="-",width=5,height=1,font=('Arial', 20),command=lambda:show("-")).place(x=310,y=220)


B8=Button(window,text="1",width=5,height=1,font=('Arial', 20),command=lambda:show("1")).place(x=15,y=280)
B9=Button(window,text="2",width=5,height=1,font=('Arial', 20),command=lambda:show("2")).place(x=110,y=280)
B10=Button(window,text="3",width=5,height=1,font=('Arial', 20),command=lambda:show("3")).place(x=210,y=280)
B_add=Button(window,text="+",width=5,height=1,font=('Arial', 20),command=lambda:show("+")).place(x=310,y=280)

B0=Button(window,text="0",width=11,height=1,font=('Arial', 20),command=lambda:show("0")).place(x=15,y=340)
B_div=Button(window,text="/",width=5,height=1,font=('Arial', 20),command=lambda:show("/")).place(x=310,y=340)
B_equ=Button(window,text="=",width=5,height=1,font=('Arial', 20),command=lambda:cal()).place(x=210,y=340)

window.mainloop()