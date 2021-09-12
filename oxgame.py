from tkinter import *
t=Tk()
t.resizable(0,0)
t.title("OXgame")
w=300
h=300
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))

c=1
def show(b):
    global c
    c+=1
    if(c%2==0):
        if(b["text"]==""):
           b["text"]="0"
    else:
        if(b["text"]==""):
           b["text"]="x" 
    if(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b1["text"]=="x" and b2["text"]=="x" and b3["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b4["text"]=="x" and b5["text"]=="x" and b6["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b7["text"]=="x" and b8["text"]=="x" and b9["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b1["text"]=="x" and b4["text"]=="x" and b7["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b2["text"]=="x" and b5["text"]=="x" and b8["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b3["text"]=="x" and b6["text"]=="x" and b9["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b1["text"]=="x" and b5["text"]=="x" and b9["text"]=="x"):
        print("player 2 is winner")
        startdemo()  
    elif(b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0"):
        print("player 1 is winner")
        startdemo()  
    elif(b3["text"]=="x" and b5["text"]=="x" and b7["text"]=="x"):
        print("player 2 is winner")
        startdemo()    
            
b1=Button(font=("",25),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b1))
b1.place(x=0,y=0,width=100,height=100)
b2=Button(font=("",25),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b2))
b2.place(x=100,y=0,width=100,height=100)
b3=Button(font=("",25),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b3))
b3.place(x=200,y=0,width=100,height=100)
b4=Button(font=("",25),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b4))
b4.place(x=0,y=100,width=100,height=100)
b5=Button(font=("",25),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b5))
b5.place(x=100,y=100,width=100,height=100)
b6=Button(font=("",25),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b6))
b6.place(x=200,y=100,width=100,height=100)
b7=Button(font=("",25),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b7))
b7.place(x=0,y=200,width=100,height=100)
b8=Button(font=("",25),bg="lightblue",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b8))
b8.place(x=100,y=200,width=100,height=100)
b9=Button(font=("",25),bg="lightyellow",fg="black",activebackground="lavender",activeforeground="black",command=lambda:show(b9))
b9.place(x=200,y=200,width=100,height=100)

def startdemo():
    b1["text"]=""
    b2["text"]=""
    b3["text"]=""
    b4["text"]=""
    b5["text"]=""
    b6["text"]=""
    b7["text"]=""
    b8["text"]=""
    b9["text"]=""

t.mainloop()