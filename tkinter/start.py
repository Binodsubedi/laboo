from tkinter import *
root = Tk()
'''
redbutton = Button(root, text = 'left', bg ='red')
redbutton.pack(side='left')
greenbutton =Button(root, text="hello-there", bg="green")
greenbutton.pack(side="right")
yellow =Button(root, text="there", bg="yellow")
yellow.pack(side="top")
blue =Button(root, text="theree", bg="blue")
blue.pack(side="bottom")


labo = Label(root, text="name", fg="blue",)
labo.grid(row=0, column=0)
name = Entry(root,bg="green")
name.grid(row=0, column=1)

submit = Button(root, text="submit", bg="blue")
submit.grid(row=1, column= 1)
'''
root.geometry("400x300")
#lab1 = Label(root, text="helloThere", fg="#00ff00")
#lab1.grid(row=0, column= 0)

#lab2 = Label(root, text="hello", fg="#00ff00")
#lab2.grid(row=2, column=1)
def gen():
    lab1 = Label(root, text="hello")
    lab1.pack()

btn1 = Button(root, text="clickMe", padx=20, pady=20, command=gen)
btn1.pack()













root.mainloop()
