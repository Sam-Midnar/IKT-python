from tkinter import *
ablak1 = Tk()
gyoker = 'H:\\Python IKT\\'
ablak1.geometry('600x600')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file='D:\IKT python projects\IKT-python\light.png')
ablak1.iconphoto(True, icon)
ablak1.config(background="black")
elsokep = PhotoImage(file=  gyoker+'siraly.png')
cimke = Label(ablak1,
             text="Üdvüzlet",
             fg='#553388',
             bg="#c3cee0",
             font=("Arial", 45, "bold"),
             bd=10,
             relief=RAISED,
             padx=45,
             pady=30,
             image=elsokep,
             compound='right'
            ).pack()

ablak1.mainloop()