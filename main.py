from tkinter import *
import colors
from tkinter import colorchooser
import randomFunctions

root = Tk()


root.state('zoomed')
main =Frame(root, height=100)

main.pack()

main.columnconfigure(0,weight=2)
main.columnconfigure((1,2,3,4,5,6,7,8,9),weight=1)
currentBrandColor =[(0),(0),(0)]
Brand = Label(main, text="brand")
brandInput = Entry(main)
displayBrand = Label(main, borderwidth=2)
displayBrand.grid(row=0,column=4)
anchor = 4


def choose_color(self,i):
    global anchor
    global currentBrandColor
    color_code = colorchooser.askcolor(title="Choose main brand color")
    currentBrandColor=color_code[0]
    self.config(bg=color_code[1])
    anchor=i
    
    

   
def setPower2(i):
    colors.setPow2(slider2.get())
    

lightnessValue = IntVar(value=0)
slider2 = Scale(main, from_=0, to=300, command=setPower2, variable=lightnessValue, width=10)
slider2.grid(row=0, column=6, sticky='w')

entry2 = Entry(main ,textvariable=lightnessValue, width=5)
entry2.grid(row=0,column=5)



brandColors=["#fff","#fff","#fff","#fff","#fff","#fff","#fff","#fff","#fff" ]
brandlabels =[]
hexCodes=[]
for i in range(len(brandColors)):
    
    globals()['b'+str(i)] = Button(main, bg='white', command=lambda i=i:choose_color(globals()['b'+str(i)],i))
    globals()['b'+str(i)].grid(row=1,column=i+1,sticky='nswe')
    brandlabels.append(globals()['b'+str(i)])

for i in range(len(brandColors)):
    
    globals()['h'+str(i)] = Label(main, bg='white')
    globals()['h'+str(i)].grid(row=2,column=i+1,sticky='nswe')
    hexCodes.append(globals()['h'+str(i)])

def generateBrand():

    hexes = colors.makeGradient(currentBrandColor,anchor)
    for i in range(len(brandColors)):
        brandColors[i]=hexes[i]
    for i in range(len(brandlabels)):
        brandlabels[i].config(bg=brandColors[i])
    for i in range(len(hexCodes)):
        hexCodes[i].config(text=hexes[i])

brandButton = Button(main, text="generate", command=generateBrand)
brandButton.grid(row=1,column=0)





generateBrand()
w,h = main.winfo_screenwidth(), main.winfo_screenheight()

main2=main
main2.pack()
root.geometry("%dx%d+0+0"%(w,h))
root.mainloop()