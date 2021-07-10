from tkinter import *
root = Tk()

root.geometry('400x200')

e1 = Entry(root)
e1.pack()
def clickme():
    valvo = 'hello ' + e1.get()
    lab1 = Label(root, text=valvo)
    lab1.pack()
    btn = Button(root, text=valvo, command=clickme)

btn = Button(root, text='click-me',command=clickme)
btn.pack()








root.mainloop()