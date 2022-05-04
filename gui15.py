from tkinter import *
tk=Tk()
tk.title("tk")


personaldetailsFrame=LabelFrame(tk,text='Personal Details')
personaldetailsFrame.grid(row=0,padx=10)

address=LabelFrame(tk,text='Address')
address.grid(row=1,pady=10)

Button(tk,text="Submit").grid(row=2,padx=(150,0))

Label(personaldetailsFrame,text="First Name").grid(row=0)
Entry(personaldetailsFrame).grid(row=0,column=1)

Label(personaldetailsFrame,text="Last Name").grid(row=1)
Entry(personaldetailsFrame).grid(row=1,column=1)

Label(address,text="Street").grid(row=0)
Entry(address).grid(row=0,column=1)

Label(address,text="City").grid(row=1)
Entry(address).grid(row=1,column=1)

Label(address,text="Zip Code").grid(row=2)
Entry(address,width=10).grid(row=2,column=1,padx=(0,60))

tk.mainloop()