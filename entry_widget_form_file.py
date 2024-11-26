from tkinter import *
root = Tk()
root.geometry("600x500")
def click():
    a = nameVal.get()
    b = phoneVal.get()
    c = genderVal.get()
    d = payVal.get()
    e = foodserviceVal.get()
    with open('new.txt','w') as file:
        file.write(f'name: {a}, \n phone number: {b}, \n gender: {c},\n  payment: {d}, \n food service:{e}')
    print('it works')

#heading
Label(root, text = "welcome to the game", font = 'comicsansms 13 bold', padx = 100, pady = 15).grid(row = 0, column = 3)
#text for the form
name = Label(root, text = "Name").grid(row = 1, column = 1)
phone = Label(root, text = "Phone").grid(row = 2, column = 1)
gender = Label(root, text = "gender").grid(row = 3, column = 1)
pay= Label(root, text = "Payment Mode").grid(row = 4, column = 1)

#tkinter variables for storing entries
nameVal = StringVar()
phoneVal = StringVar()
genderVal = StringVar()
payVal = StringVar()
foodserviceVal = IntVar()
#entry for the form
nameentry = Entry(root, textvariable =nameVal )
phoneentry = Entry(root, textvariable = phoneVal)
genderentry = Entry(root, textvariable = genderVal)
payentry = Entry(root, textvariable = payVal)


nameentry.grid(row = 1 ,column = 3)
phoneentry.grid(row = 2 ,column = 3)
genderentry.grid(row = 3,column = 3)
payentry.grid(row =4 ,column = 3)

#checkbox
foodservice = Checkbutton(text= 'want to play the game', variable = foodserviceVal).grid(column = 2)

Button(root, text = 'Submit', command = click).grid( column = 2)
root.mainloop()