from tkinter import*
from tkinter import messagebox

admin = Tk()
admin.title("Election system")

admin.minsize(width=800, height=800)
admin.maxsize(width=1580, height=1080)

vgslogo = PhotoImage(file = "D:\Project SE\VGS.png")
l1 = Label(admin, image= vgslogo)
l1.pack()




#Add Candidate Window
Candidates=[]
def acwindow():
    ac=Tk()
    ac.title("Add Candidate")

    ac.minsize(width=500, height=200)
    ac.maxsize(width=1580, height=1080)

    Labelname=Label(ac, text="Name:", font=("Calibri", 18))
    Labelname.place(x=30, y=70)

    Name=StringVar()
    def add_candidateButton():
        print(Name.get())
        Candidates.append(Name.get())
        messagebox.showinfo("Congratulations", "Candidate added Successfully")
        print(Candidates)
        ac.destroy()


    nameentry=Entry(ac, textvariable=Name, font=("Calibri", 18))
    nameentry.place(x=120, y=70)


    acbutton=Button(ac, text=" Add ", font=("Calibri", 14), command=add_candidateButton)
    acbutton.place(x=380, y=65)


    def Exitbutton1():
        ac.destroy()


    backbutton1=Button(ac, text="Back", font=("Times", 14), command=Exitbutton1)
    backbutton1.place(x=230, y=130)


    ac.mainloop()

b1=Button(admin, text="Add Candidate", font=("Calibri", 18), command=acwindow)
b1.pack()





#Show Candidates Window
def scwindow():
    sc=Tk()
    sc.title("List of Candidates")

    sc.minsize(width=500, height=200)
    sc.maxsize(width=1580, height=1080)



    Name=Candidates[0]
    print(Candidates)






    def Exitbutton2():
        sc.destroy()

    backbutton2=Button(sc, text="Back", font=("Times", 14), command=Exitbutton2)
    backbutton2.pack()


    sc.mainloop()





b2=Button(admin, text="Show Candidates", font=("Calibri", 18), command=scwindow)
b2.pack()



















admin.mainloop()

