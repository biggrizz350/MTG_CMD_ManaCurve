from tkinter import *
import math

class Window(Frame):
    def _init_(self, master = None):
        Frame._init_(self, master)
        self.master = master

    
def col_round(x):
    frac = x - math.floor(x)
    if frac < 0.5: return math.floor(x)
    return math.ceil(x)

#initialize tkinter
root = Tk()
app = Window(root)
root.config(bg="black")

#size of window
root.geometry("580x225")

#window title
root.wm_title("MTG CMD Mana Curve calculator")

#left frame
left_frame = Frame(root, width=200, height= 400, bg='grey')
left_frame.grid(row=0, column = 1, padx=10, pady=5)

#middle frame
middle_frame = Frame(root, width=200, height = 400, bg='grey')
middle_frame.grid(row=0, column = 2, padx= 10, pady=5)

#right frame
right_frame = Frame(root, width=200, height = 400, bg='grey')
right_frame.grid(row=0, column = 3, padx = 10, pady= 5)

#frame labels
Label(left_frame, text="Total Mana Symbols", relief=RAISED).grid(row=0,column=1, padx=5,pady=5)
Label(middle_frame, text="Total Land Count", relief=RAISED).grid(row=0, column=2, padx=5, pady=5)
Label(right_frame, text="Mana Reccomendations", relief=RAISED).grid(row=0, column=3, padx=5, pady=5)


#text fields
textW = Entry(left_frame)
textW.grid(row=1,column=1,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(left_frame, text="White: ").grid(row = 1, column=0, padx=5, pady=5)
textU = Entry(left_frame)
textU.grid(row=2,column=1,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(left_frame, text="Blue: ").grid(row = 2, column=0, padx=5, pady=5)
textB = Entry(left_frame)
textB.grid(row=3,column=1,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(left_frame, text="Black: ").grid(row = 3, column=0, padx=5, pady=5)
textR = Entry(left_frame)
textR.grid(row=4,column=1,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(left_frame, text="Red: ").grid(row = 4, column=0, padx=5, pady=5)
textG = Entry(left_frame)
textG.grid(row=5,column=1,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(left_frame, text="Green: ").grid(row = 5, column=0, padx=5, pady=5)

#Planned land total and calculate button
textL = Entry(middle_frame)
textL.grid(row=1, column=2, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

#Results for each amount of land suggested
textWR = Entry(right_frame)
textWR.grid(row=1,column=3,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(right_frame, text="White: ").grid(row = 1, column=2, padx=5, pady=5)
textUR = Entry(right_frame)
textUR.grid(row=2,column=3,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(right_frame, text="Blue: ").grid(row = 2, column=2, padx=5, pady=5)
textBR = Entry(right_frame)
textBR.grid(row=3,column=3,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(right_frame, text="Black: ").grid(row = 3, column=2, padx=5, pady=5)
textRR = Entry(right_frame)
textRR.grid(row=4,column=3,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(right_frame, text="Red: ").grid(row = 4, column=2, padx=5, pady=5)
textGR = Entry(right_frame)
textGR.grid(row=5,column=3,padx=5,pady=5, sticky='w'+'e'+'n'+'s')
Label(right_frame, text="Green: ").grid(row = 5, column=2, padx=5, pady=5)

def calculate():
    lands = int(textL.get())
    totalSymbols= int(textW.get()) + int(textU.get()) + int(textB.get()) + int(textR.get()) + int(textG.get())
    textWR.insert(0, col_round((int(textW.get())/totalSymbols)* lands))
    textUR.insert(0, col_round((int(textU.get())/totalSymbols)* lands))
    textBR.insert(0, col_round((int(textB.get())/totalSymbols)* lands))
    textRR.insert(0, col_round((int(textR.get())/totalSymbols)* lands))
    textGR.insert(0, col_round((int(textG.get())/totalSymbols)* lands))
    totalSybmols = 0;

def clear():
    textW.delete(0,END)
    textU.delete(0,END)
    textB.delete(0,END)
    textR.delete(0,END)
    textG.delete(0,END)
    textWR.delete(0,END)
    textUR.delete(0,END)
    textBR.delete(0,END)
    textRR.delete(0,END)
    textGR.delete(0,END)
    textL.delete(0,END)
    

#button for calculate and clear
btn = Button(middle_frame, text="Calculate", command=lambda:calculate())
btn.grid(row=2, column=2, padx=5,pady=5, sticky='w'+'e'+'n'+'s')

btn2 = Button(middle_frame, text="Clear", command=lambda:clear())
btn2.grid(row=3, column=2, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

#-----------------------

#show window
root.mainloop()
