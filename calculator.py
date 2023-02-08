import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.resizable(False, False)
# root.geometry("400x700")
# root.config(background="#444")

mainFrame = tkinter.Frame(root)
mainFrame.pack(padx=5, pady=10)

displayNum=tkinter.StringVar() #Crea un String de caracteres
operator=""
result=0

# displayNum.set('0')

def showNum(num):
  global operator
  if operator != "":
    displayNum.set(num)
    operator=""
  else:
    displayNum.set(displayNum.get() + num)

def add(num):
  global operator
  global result

  result+=int(num)
  operator="+"

  displayNum.set(result)


# ------------- Display ------------- #

display = tkinter.Entry(mainFrame, textvariable=displayNum, width='36')
display.grid(row=1, column=1, pady=(0, 10), columnspan='4')
display.config(background='#aaa', fg='#000', justify='right')


# ------------- Row 1 ------------- #

btn7 = tkinter.Button(mainFrame, text='7', command=lambda:showNum('7'), width='6', height='2')
btn7.grid(row=2, column=1, padx=2, pady=2)
btn8 = tkinter.Button(mainFrame, text='8', command=lambda:showNum('8'), width='6', height='2')
btn8.grid(row=2, column=2, padx=2, pady=2)
btn9 = tkinter.Button(mainFrame, text='9', command=lambda:showNum('9'), width='6', height='2')
btn9.grid(row=2, column=3, padx=2, pady=2)
btnDiv = tkinter.Button(mainFrame, text='/', width='6', height='2')
btnDiv.grid(row=2, column=4, padx=2, pady=2)


# ------------- Row 2 ------------- #

btn4 = tkinter.Button(mainFrame, text='4', command=lambda:showNum('4'), width='6', height='2')
btn4.grid(row=3, column=1)
btn5 = tkinter.Button(mainFrame, text='5', command=lambda:showNum('5'), width='6', height='2')
btn5.grid(row=3, column=2)
btn6 = tkinter.Button(mainFrame, text='6', command=lambda:showNum('6'), width='6', height='2')
btn6.grid(row=3, column=3)
btnMult = tkinter.Button(mainFrame, text='*', width='6', height='2')
btnMult.grid(row=3, column=4)


# ------------- Row 3 ------------- #

btn1 = tkinter.Button(mainFrame, text='1', command=lambda:showNum('1'), width='6', height='2')
btn1.grid(row=4, column=1)
btn2 = tkinter.Button(mainFrame, text='2', command=lambda:showNum('2'), width='6', height='2')
btn2.grid(row=4, column=2)
btn3 = tkinter.Button(mainFrame, text='3', command=lambda:showNum('3'), width='6', height='2')
btn3.grid(row=4, column=3)
btnRest = tkinter.Button(mainFrame, text='-', width='6', height='2')
btnRest.grid(row=4, column=4)


# ------------- Row 4 ------------- #

btnPoint = tkinter.Button(mainFrame, text='.', width='6', height='2')
btnPoint.grid(row=5, column=1)
btn0 = tkinter.Button(mainFrame, text='0', command=lambda:showNum('0'), width='6', height='2')
btn0.grid(row=5, column=2)
btnEq = tkinter.Button(mainFrame, text='=', width='6', height='2')
btnEq.grid(row=5, column=3)
btnAdd = tkinter.Button(mainFrame, text='+', command=lambda:add(displayNum.get()), width='6', height='2')
btnAdd.grid(row=5, column=4)


root.mainloop()