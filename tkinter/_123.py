from tkinter import *
root = Tk()

root.title('hello world')

root.iconbitmap('C:/Users/dell/Downloads/Calculator.ico')

e = Entry(root, width=40, borderwidth= 4)
e.grid(row=0, column=0, columnspan =3, padx=6, pady=2)

#equalTimes = 0

def clicko(number):


    num = e.get()
    e.delete(0, END)
    e.insert(0, num + number)
    
def clear_fun():

    e.delete(0, END)

def add_fun():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Add'
    f_num = int(first_num)
    e.delete(0, END)

def sub_fun():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Sub'
    f_num = int(first_num)
    e.delete(0, END)

def mul_fun():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Mul'
    f_num = int(first_num)
    e.delete(0, END)

def div_fun():
    first_num = e.get()
    global f_num
    global operation
    operation = 'Div'
    f_num = int(first_num)
    e.delete(0, END)






def equal_fun():

    #global equalTimes
    #equalTimes += 1


    second_num = e.get()
    e.delete(0, END)

    if operation=='Add':
            e.insert(0, f_num + int(second_num))

    elif operation=='Sub':
        e.insert(0, f_num - int(second_num))

    elif operation=='Mul':
        e.insert(0, f_num * int(second_num))

    else:
        e.insert(0, f_num / int(second_num))


    #elif f_num == False:

     #   e.insert(0, 'Insert some value first')




# defining the buttons
#Numbers
btn_1 = Button(root, text='1', padx=40, pady=20, command =lambda: clicko('1'))
btn_2 = Button(root, text='2', padx=40, pady=20, command =lambda: clicko('2'))
btn_3 = Button(root, text='3', padx=40, pady=20, command =lambda: clicko('3'))
btn_4 = Button(root, text='4', padx=40, pady=20, command =lambda: clicko('4'))
btn_5 = Button(root, text='5', padx=40, pady=20, command =lambda: clicko('5'))
btn_6 = Button(root, text='6', padx=40, pady=20, command =lambda: clicko('6'))
btn_7 = Button(root, text='7', padx=40, pady=20, command =lambda: clicko('7'))
btn_8 = Button(root, text='8', padx=40, pady=20, command =lambda: clicko('8'))
btn_9 = Button(root, text='9', padx=40, pady=20, command =lambda: clicko('9'))
btn_0 = Button(root, text='0', padx=40, pady=20, command =lambda: clicko('0'))
btn_plus = Button(root, text='+', padx=39, pady=20, command=add_fun)
btn_minus = Button(root, text='-', padx=41, pady=20, command=sub_fun)

btn_mul = Button(root, text='*', padx=40, pady=20, command=mul_fun)
btn_div = Button(root, text='/', padx=40, pady=20, command=div_fun)
btn_clr = Button(root, text='C', padx=39, pady=20, command=clear_fun)

btn_equal = Button(root, text='=', padx=134, pady=20, command=equal_fun)


#shoving in
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)
btn_plus.grid(row=4, column=1)
btn_minus.grid(row=4, column=2)

btn_mul.grid(row=5, column=0)
btn_div.grid(row=5, column=1)
btn_clr.grid(row=5, column=2)

btn_equal.grid(row=6, column=0, columnspan=3)






root.mainloop()