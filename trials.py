'''from tkinter import *

def main():
    win = Tk()
    win.geometry("480x480");
    win.title("Title");

    def login_redirect():
        win.destroy()
        login_page()

    login = Button(win, text="login", command=login_redirect)
    login.place(x=40,y=40)

    win.mainloop()

def login_page():
    win = Tk()
    win.geometry("480x480");
    win.title("Covid 19 Admin Panel")

main()'''







'''# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file = "D:\Project SE\Vgslogo.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
				height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

# Add Text
canvas1.create_text( 200, 250, text = "Welcome")

# Create Buttons
button1 = Button( root, text = "Exit")
button3 = Button( root, text = "Start")
button2 = Button( root, text = "Reset")

# Display Buttons
button1_canvas = canvas1.create_window( 100, 10,
									anchor = "nw",
									window = button1)

button2_canvas = canvas1.create_window( 100, 40,
									anchor = "nw",
									window = button2)

button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
									window = button3)

# Execute tkinter
root.mainloop()'''

# Program to make a simple
# login screen


from tkinter import*
from tkinter import messagebox


ac = Tk()
ac.title("Add Candidate")

ac.minsize(width=500, height=200)
ac.maxsize(width=1580, height=1080)


Candidates=[]
Name = StringVar()


def add_candidateButton():
	print(Name.get())
	Candidates.append(Name.get())
	messagebox.showinfo("Congratulations", "Candidate added Successfully")
	print(Candidates)


nameentry = Entry(ac, textvariable=Name, font=("Calibri", 18))
nameentry.place(x=120, y=70)

acbutton = Button(ac, text=" Add ", font=("Calibri", 14), command=add_candidateButton)
acbutton.place(x=380, y=65)

ac.mainloop()


