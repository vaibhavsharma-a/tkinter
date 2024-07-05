from tkinter import *

root = Tk()
root.title("simple calculator")

# adding functioning to the buttons

def button_click(number):
  curr = display.get()
  display.delete(0,END)
  display.insert(0, str(curr) + str(number))
  
def button_clear():
  display.delete(0,END)

def button_add():
  first_number = display.get()
  global fir_num 
  global maths
  maths = "addition"
  fir_num = int(first_number)
  display.delete(0,END)




def button_multi():
  first_number = display.get()
  global fir_num
  global maths
  maths = "multiply"
  fir_num = int(first_number)
  display.delete(0,END)
  

def button_divi():
  first_number = display.get()
  global fir_num
  global maths
  maths = "division"
  fir_num = int(first_number)
  display.delete(0,END)

def button_subtr():
  first_number = display.get()
  global fir_num
  global maths
  maths = "subtration"
  fir_num = int(first_number)
  display.delete(0,END)

def button_eql():
  second_num = display.get()
  display.delete(0,END)

  if maths == "addition":
    display.insert(0,fir_num + int(second_num))
  
  elif maths == "subtration":
    display.insert(0,fir_num - int(second_num))
  
  elif maths == "multiply":
    display.insert(0,fir_num * int(second_num))

  else:
    display.insert(0,fir_num / int(second_num))




display = Entry(root,width=40,borderwidth=4)

display.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#creating button
button1 = Button(root,text="1",padx=40,pady=20,command=lambda : button_click(1))
button2 = Button(root,text="2",padx=40,pady=20,command=lambda : button_click(2))
button3 = Button(root,text="3",padx=40,pady=20,command=lambda : button_click(3))
button4 = Button(root,text="4",padx=40,pady=20,command=lambda : button_click(4))
button5 = Button(root,text="5",padx=40,pady=20,command=lambda : button_click(5))
button6 = Button(root,text="6",padx=40,pady=20,command=lambda : button_click(6))
button7 = Button(root,text="7",padx=40,pady=20,command=lambda : button_click(7))
button8 = Button(root,text="8",padx=40,pady=20,command=lambda : button_click(8))
button9 = Button(root,text="9",padx=40,pady=20,command=lambda : button_click(9))
button0 = Button(root,text="0",padx=40,pady=20,command=lambda : button_click(0))
buttonadd = Button(root,text="+",padx=39,pady=20,command=button_add)
buttonsubt = Button(root,text="-",padx=43,pady=20,command=button_subtr)
buttondiv = Button(root,text="/",padx=43,pady=20,command=button_divi)
buttonmult = Button(root,text="*",padx=43,pady=20,command=button_multi)
button_eql = Button(root,text="=",padx=91,pady=20,command=button_eql)
button_clear = Button(root,text="clear",padx=79,pady=20,command=button_clear)

# display.grid()

#puttin button

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)

button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

buttonadd.grid(row=5,column=0)
button_eql.grid(row=5,column=1,columnspan=2)

buttonsubt.grid(row=6,column=0)
buttonmult.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)


root.mainloop()