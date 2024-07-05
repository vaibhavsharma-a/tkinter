from tkinter import *

root = Tk()

e = Entry(root,width=50,bg="light blue",fg="black",borderwidth=10)
e.pack()
e.insert(0,"Enter a name: ")

def theclick():
  onclick =  Label(root,text=f"Hello {e.get()}")
  onclick.pack()
#creating lable
# mylabel = Label(root, text="i love cricket")
# anotherlabel = Label(root, text="virat is the goat")
mybutton = Button(root,text="Enter a name",padx=10,pady=10,command=theclick,bg="pink",fg="red")
#putting it on the screen
# mylabel.grid(row=0,column=0)
# anotherlabel.grid(row=1,column=1)
mybutton.pack()

root.mainloop()
