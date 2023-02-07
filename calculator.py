import tkinter

root = tkinter.Tk()

mainFrame = tkinter.Frame(root)
mainFrame.pack(padx=10, pady=10)

# ------------- Display ------------- #

display = tkinter.Entry(mainFrame)
display.grid(row=1, column=1, pady=(0, 10), columnspan='4')
display.config(background='#aaa', fg='#000', justify='right')


# ------------- Row 1 ------------- #

btn7 = tkinter.Button(mainFrame, text='7', width='3')
btn7.grid(row=2, column=1, padx=2, pady=2)
btn8 = tkinter.Button(mainFrame, text='8', width='3')
btn8.grid(row=2, column=2, padx=2, pady=2)
btn9 = tkinter.Button(mainFrame, text='9', width='3')
btn9.grid(row=2, column=3, padx=2, pady=2)
btnDiv = tkinter.Button(mainFrame, text='/', width='3')
btnDiv.grid(row=2, column=4, padx=2, pady=2)


# ------------- Row 2 ------------- #

btn4 = tkinter.Button(mainFrame, text='4', width='3')
btn4.grid(row=3, column=1)
btn5 = tkinter.Button(mainFrame, text='5', width='3')
btn5.grid(row=3, column=2)
btn6 = tkinter.Button(mainFrame, text='6', width='3')
btn6.grid(row=3, column=3)
btnMult = tkinter.Button(mainFrame, text='*', width='3')
btnMult.grid(row=3, column=4)


# ------------- Row 3 ------------- #

btn1 = tkinter.Button(mainFrame, text='1', width='3')
btn1.grid(row=4, column=1)
btn2 = tkinter.Button(mainFrame, text='2', width='3')
btn2.grid(row=4, column=2)
btn3 = tkinter.Button(mainFrame, text='3', width='3')
btn3.grid(row=4, column=3)
btnRest = tkinter.Button(mainFrame, text='-', width='3')
btnRest.grid(row=4, column=4)


# ------------- Row 4 ------------- #

btnPoint = tkinter.Button(mainFrame, text='.', width='3')
btnPoint.grid(row=5, column=1)
btn0 = tkinter.Button(mainFrame, text='0', width='3')
btn0.grid(row=5, column=2)
btnEq = tkinter.Button(mainFrame, text='=', width='3')
btnEq.grid(row=5, column=3)
btnAdd = tkinter.Button(mainFrame, text='+', width='3')
btnAdd.grid(row=5, column=4)


root.mainloop()