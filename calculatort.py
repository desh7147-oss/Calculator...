#remaining tasks:
"""1. handling the corner cases like division with 0
   2. applying the two stack two calculate the result
   3. adding a new sliding window for more operations
   4. applying the logics for square-root(with BINARY SEARCH)
   5. DRY THE CODE
   6. saving the expression on the screen so that the user can revisit it
   7. add some styling to our calculator
"""
from tkinter import *
root=Tk()
#putting entry box for the calculation window
enter=Entry(root,width=30,borderwidth=5)
enter.grid(row=0,columnspan=3)#padx=10,pady=10)
global stringing

#functions for using buttons
def do(number):
    current=enter.get()
    do_clear()
    enter.insert(0,str(current) + str(number))
    stringing = enter.get()
    

#fuction for clearing the entry box
def do_clear():
    enter.delete(0,END)

#function for additon 
def do_add():
    num1=enter.get()
    global num
    num=float(num1)
    do_clear()
    global operation
    operation="+"
    #stringing  += operation

    #enter.insert(0,str(stringing))
    #do_clear()
    

#function for subtraction
def do_sub():
    num1=enter.get()
    global num
    num=float(num1)
    do_clear()
    global operation
    operation="-"

#function  for multiplication
def do_multiply():
    num1=enter.get()
    global num
    num=float(num1)
    do_clear()
    global operation
    operation="*"

#function for division

def do_div():
    num1=enter.get()
    global num
    num=float(num1)
    do_clear()
    global operation
    operation="/"

#function for remainder
def do_remainder():
    num1=enter.get()
    global num
    num=float(num1)
    do_clear()
    global operation
    operation="%"

#function for square root(using binary search)

#function for square

#function for logarithm

#fuction for sin(x)

#function for cos(x)

#function for tan(x)

#function for point
def do_decimal():
    pass


#function for o/p the result
def equals():
    num2=enter.get()
    do_clear()
    if(operation=="+"):
        enter.insert(0,num + int(num2))
    elif(operation=="-"):
        result=num-float(num2)
        enter.insert(0,result)
    elif(operation=="*"):
        enter.insert(0,num* float(num2))
    
    elif(operation=="/"):
        enter.insert(0,num / float(num2))


    elif(operation=="%"):
        enter.insert(0,num % float(num2))
    



#buttons for the digits 0 to 9
button_1=Button(root,text="1",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(1))
button_2=Button(root,text="2",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(2))
button_3=Button(root,text="3",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(3))
button_4=Button(root,text="4",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(4))
button_5=Button(root,text="5",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(5))
button_6=Button(root,text="6",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(6))
button_7=Button(root,text="7",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(7))
button_8=Button(root,text="8",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(8))
button_9=Button(root,text="9",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(9))
button_0=Button(root,text="0",fg="black",bg="grey",padx=43,pady=15,borderwidth=5,command=lambda: do(0))

#setting up the buttons onto the window
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_3.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_1.grid(row = 3, column = 2)

button_0.grid(row=4,column=0)

#buttons for opearations

button_add = Button(root, text = "+", padx = 43, pady = 47,borderwidth = 5,bg = "grey",fg = "black", command = do_add)
button_equals = Button(root, text="=", padx = 44, pady = 18, borderwidth = 5,bg = "grey", fg = "black", command = equals)
button_sub = Button(root, text = "-", padx = 45, pady = 18, borderwidth = 5, bg = "grey", fg = "black", command = do_sub)
button_clear = Button(root, text = "clear", padx = 32, pady = 18, borderwidth = 5, bg="grey", fg="black", command = do_clear)
button_multiply = Button(root, text = "*", padx = 43, pady=18, borderwidth = 5,bg = "grey", fg="black", command = do_multiply)
button_division = Button(root, text = "/" , padx = 45, pady=18, borderwidth = 5,bg = "grey", fg="black", command = do_div)
button_remainder = Button(root, text= "remainder", padx = 14, pady = 18, borderwidth = 5, bg = "grey", fg=  "black",command = do_remainder)
button_point = Button(root, text = ".", fg = "black", bg = "grey",padx = 43,pady = 16,borderwidth = 5,command = do_decimal)
button_percentage  = Button(root, text = "%", fg = "black", bg = "grey", padx = 43, pady = 16, borderwidth=  5,command = do_decimal)

button_add.grid ( row = 4, column = 2, rowspan = 2)
button_equals.grid ( row = 6,column = 2, columnspan = 2)
button_sub.grid ( row = 5, column = 1)
button_clear.grid ( row = 5, column = 0)
button_multiply.grid ( row = 6, column = 1)
button_division.grid ( row = 4, column = 1)
button_remainder.grid ( row = 6, column = 0 )
button_point.grid ( row = 7, column = 0)
button_percentage.grid ( row = 7, column = 1)



root.mainloop()
