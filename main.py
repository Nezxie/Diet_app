from tkinter import *
from tkinter import ttk
import random


#class def

class Meal:
    def __init__(self, name = "",ingredients = [],kcal = 0,howToMake = "",tags = [0,0,0,0,0]): #later add makro B/T/W etc
        self.name = name
        self.ingredients=ingredients
        self.kcal=kcal
        self.howToMake = howToMake
        self.tags = {"isVegan":tags[0],
                    "isWege":tags[1],
                    "isSweet":tags[2],
                    "isSpicy":tags[3],
                    "isHot":tags[4]}

 
    

#variables
myDatabase = open('diet_app\Diet_app\FoodTable', "r",encoding="utf-8")
root = Tk()
listOfMeals = []
listOfMealsRaw=myDatabase.readlines()

for item in listOfMealsRaw:
    tmp=item.split(":")
    tmpName=tmp[0]
    tmpIngr=tmp[1].split(",")
    tmpkcal=tmp[2]
    tmpHTM=tmp[3]         #HowToMake
    tmpTags=tmp[4].split(",")
    listOfMeals.append(Meal(tmpName,tmpIngr,tmpkcal,tmpHTM))


#functions

def randomMeal(listOfMeals):
    tmp = outputMealName["text"]
    outputIngredients["text"] = ""
    while 1:        #not optimal cause i change before i check if ok
        randMeal=random.choice(listOfMeals)
        outputMealName["text"] = randMeal.name #        random.choice(listOfMeals).name  #OMG it works wow i feel smart xD
        outputKcal["text"] = randMeal.kcal + " kcal"
        outputHTM["text"] = "Przygotowanie: " + randMeal.howToMake
        if outputMealName["text"] != tmp: break
    outputIngredients["text"] += "Składniki: " + "\n"    
    for item in randMeal.ingredients:
        outputIngredients["text"] += item + "\n"
    


#GUI
#center the app window (on the screen)
windowWidth = 600
windowHeight = 400
mainColor = "#80b380"
secColor = "white"
fontColor = "black"

#   get the screen dimension
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

#    find the center point
centerX = int(screenWidth/2 - windowWidth / 2)
centerY = int(screenHeight/2 - windowHeight / 2)


root.title("Generator posiłków")
#im sorry this is so complicated it was done with f'{text}' but i dont remember how to use it
root.geometry(str(windowWidth)+"x"+str(windowHeight)+"+"+str(centerX)+"+"+str(centerY)) #widthxheight base window "600x400+x+y"

#   icon
root.iconbitmap(r'diet_app\Diet_app\lemon.ico')  #r converts this to raw string so python does not read this as Unicode (cause of \U xD)



#GUI features
#font needs tuple ("style",size,bold/nobold,italic/roman)
root.configure(background=secColor)
leftMargin = Frame(root, bg=mainColor,height = windowHeight,width = windowWidth/6)
rightMargin = Frame(root, bg=mainColor,height = windowHeight,width = windowWidth/6)
buttonGenerate = Button(root,text = "Co zjeść? \U0001F957",padx=20, pady=10,font = 'Courier 15',bg = secColor, command = lambda: randomMeal(listOfMeals))
outputMealName = Label(root,text = "", fg = fontColor,font= ("Courier", 16),bg = secColor) #nice font "Fixedsys"
outputIngredients = Label(root,text = "", fg = fontColor,font= ("Courier", 12),bg = secColor)
outputKcal = Label(root,text = "", fg = fontColor,font= ("Courier", 10),bg = secColor)
outputHTM = Label(root,text = "", fg = fontColor,font= ("Courier", 10),bg = secColor)


leftMargin.pack(side=LEFT)
rightMargin.pack(side=RIGHT)
buttonGenerate.pack(padx=10, pady=5)
outputMealName.pack(padx=10,pady=10)
outputIngredients.pack(padx=10,pady=10)
outputKcal.pack(padx=10,pady=10)
outputHTM.pack(padx=10,pady=10)

''' FOR NOW
buttonGenerate.grid(row = 0, column = 0)
outputMealName.grid(row=1,column=0)
outputIngredients.grid(row=1,column=0)
outputKcal.grid(row=1,column=0)
outputHTM.grid(row=1,column=0)
'''


#main loop

root.mainloop()
