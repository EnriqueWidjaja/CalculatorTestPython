from tkinter import *
import parser
from math import factorial

root = Tk()
root.title ('Calculator-Test')
root.resizable(0,0)

#buat display angka dan proses
display = Entry(root)
display.grid(row=1,columnspan=6,sticky="nesw")

#tombol 789
Button(root,text="7",command = lambda :get_variables(7)).grid(row=2,column=0, sticky="nesw")
Button(root,text=" 8 ",command = lambda :get_variables(8)).grid(row=2,column=1, sticky="nesw")
Button(root,text=" 9 ",command = lambda :get_variables(9)).grid(row=2,column=2, sticky="nesw")

#tombol 456
Button(root,text="4",command = lambda :get_variables(4)).grid(row=3,column=0, sticky="nesw")
Button(root,text=" 5 ",command = lambda :get_variables(5)).grid(row=3,column=1, sticky="nesw")
Button(root,text=" 6 ",command = lambda :get_variables(6)).grid(row=3,column=2, sticky="nesw")

#tombol 123
Button(root,text="1",command = lambda :get_variables(1)).grid(row=4,column=0, sticky="nesw")
Button(root,text=" 2 ",command = lambda :get_variables(2)).grid(row=4,column=1, sticky="nesw")
Button(root,text=" 3 ",command = lambda :get_variables(3)).grid(row=4,column=2, sticky="nesw")

#tombol 0.AC
Button(root,text=" 0 ",command = lambda :get_variables(0)).grid(row=5,column=0, sticky="nesw")
Button(root,text=" . ",command = lambda :get_variables(".")).grid(row=5, column=1, sticky="nesw")
Button(root,text="AC",command = lambda :clear_all()).grid(row=5,column=2, sticky="nesw")

#tombol operator +-*/
Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky="nesw")
Button(root,text=" - ",command= lambda :get_operation("-")).grid(row=3,column=3, sticky="nesw")
Button(root,text=" * ",command= lambda :get_operation("*")).grid(row=4,column=3, sticky="nesw")
Button(root,text=" / ",command= lambda :get_operation("/")).grid(row=5,column=3, sticky="nesw")

#tambahan tombol buat pi, persen, buka kurung, eksponen
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky="nesw")
Button(root,text=" % ",command= lambda :get_operation("%")).grid(row=3,column=4, sticky="nesw")
Button(root,text=" ( ",command= lambda :get_operation("(")).grid(row=4,column=4, sticky="nesw")
Button(root,text=" exp ",command= lambda :get_operation("**")).grid(row=5,column=4, sticky="nesw")

#tombol delete, faktorial, tutup kurung, pangkat 2, sama dengan
Button(root,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky="nesw")
Button(root,text=" x! ", command= lambda: fact()).grid(row=3,column=5, sticky="nesw")
Button(root,text=" ) ",command= lambda :get_operation(")")).grid(row=4,column=5, sticky="nesw")
Button(root,text=" ^2 ",command= lambda :get_operation("**2")).grid(row=5,column=5, sticky="nesw")
Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky="nesw")

i = 0

#buat dapet angka
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

#buat dapet operator
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

#buat apus semua
def clear_all():
    display.delete(0,END)

#buat delete
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#buat ngitung
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

#buat faktorial
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
root.mainloop()
