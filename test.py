import tkinter
from tkinter import *
root = Tk()
zmienna = "*"
entry1=tkinter.Entry(root,textvariable = zmienna)
a = IntVar(root, 255)
a.set(200)
print(a.get())
def funkcja(tekst="chuj"):
    myDatabase = open('diet_app\Diet_app\TESTable', "a")
    tekst = entry1.get()
    myDatabase.write(tekst+"\n")
    myDatabase.close()
funkcja("putin")
funkcja("to")
funkcja()

butt1=tkinter.Button(root,text="wciśnij przycisk",command=funkcja)
entry1.pack()
butt1.pack()

root.mainloop()