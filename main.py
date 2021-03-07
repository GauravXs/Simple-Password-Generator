#RANDOM PASSWORD GENERATOR
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import time
from pwgenfunc import RandPass
import tkinter.messagebox
def name():
    myname=Label(text='Developed By:- GAURAV SINGH',fg='black',font=('sans serif',15,'bold')).place(x=50,y=205)
    return
def pwGenerator(size = 8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    lbl_strength.configure(foreground="white", background=pw_color, text=pw_strength,font=('sans serif', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()
def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Password Generator","Do You Want To Exit")
    if iExit > 0:
        gui.destroy()
        return
gui = Tk()
about=Button(text='i',fg='black',font=('Ravie',15,'bold'),command=name)
about.place(x=0,y=200)
exit=Button(text='Exit',fg='black',font=('sans serif',10, 'bold'),command=iExit)
exit.place(x=564,y=211)
gui.title("Password Generator")
width = 600
height = 262
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))
PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8)
Top = Frame(gui, width=width)
Top.pack(side=TOP)
Form = Frame(gui, width=width)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)
lbl_title = Label(Top, width=width, font=('sans serif', 12, 'bold'), text="Select: Size >> Click: Generate Now", bd=1, relief=SOLID)
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('sans serif', 18), text="Password", bd=10)
lbl_password.grid(row=0, pady=10)
lbl_strength = Label(Form, font=('sans serif', 10, 'bold'), foreground="white", background="#6d0001", text="Weak", bd=10, height=1, width=10)
lbl_strength.grid(row=0, column=3, pady=10, padx=10)
lbl_pw_size = Label(Form, font=('sans serif', 18), text="Size", bd=10)
lbl_pw_size.grid(row=1, pady=10)
lbl_instructions = Label(Bot, width=width, font=('sans serif', 12, 'bold'), text="Result will be on clipboard.", bd=1, relief=SOLID)
lbl_instructions.pack(fill=X)
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=230,width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, font=(18))
pw_size.grid(row=1, column=1, columnspan=2)
btn_generate = Button(Form, text="Generate Now", width=20,font=('bold'),command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=2, column=1, columnspan=2)
gui.mainloop()
