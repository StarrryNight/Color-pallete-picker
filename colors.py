import colorsys
from chromato import convert

leftX = 8
rightX = 98
leftY=95
rightY=20

xArray=[0]*9
xArray[0], xArray[8]= leftX, rightX
yArray=[0]*9
yArray[0], yArray[8]= leftY, rightY

power1 = 2
power2=2

def setPow1(i):
    global power1
    power1 = i/100
   

def setPow2(i):
    global power2
    power2 = i/100



def generateX(anchor):
    #Calculate equal increments from left to right
    leftXIncrements = (xArray[anchor]-xArray[0])/anchor
    for i in range(1,anchor):
        xArray[i]=round(xArray[i-1]+leftXIncrements)
    rightXIncrements = (xArray[8]-xArray[anchor])/(8-anchor)
    for i in range(anchor+1,8):
       xArray[i]=round(xArray[i-1]+rightXIncrements)
        #
   # leftXIncrements = (xArray[0]-xArray[anchor])/(calculateIncrements(anchor,0,power1))
  #  for i in range(1,anchor):
  #      xArray[i]= round(xArray[i-1]-leftXIncrements*int(pow(power1,i-1)))
  #  rightXIncrements = (xArray[anchor]-xArray[8])/(calculateIncrements(8,anchor, power1))
  #  for i in range(anchor+1,8):
  #      xArray[i]= round(xArray[i-1]-rightXIncrements*int(pow(power1,i-5)))


def calculateIncrements(x,y,power):
    z=x-y
    b=0
 
    for i in range(1,z+1):
        b+=int(pow(power,i-1))
  
    return b
def generateY(anchor):
    #calculate exponential increments from left to right. This is going from larger value to smaller value hence operations are reversed
    leftYIncrements = (yArray[0]-yArray[anchor])/(calculateIncrements(anchor,0, power2))
    for i in range(1,anchor):
        yArray[i]= round(yArray[i-1]-leftYIncrements*int(pow(power2,i-1)))
    rightYIncrements = (yArray[anchor]-yArray[8])/(calculateIncrements(8,anchor, power2))
    for i in range(anchor+1,8):
        yArray[i]= round(yArray[i-1]-rightYIncrements*int(pow(power2,3-(i-5))))

def makeGradient(rgbs,anchor):
    hsv= colorsys.rgb_to_hsv(rgbs[0]/255,rgbs[1]/255,rgbs[2]/255)
    h=round(hsv[0]*360)
    s=round(hsv[1]*100)
    v=round(hsv[2]*100)
    
    xArray[anchor], yArray[anchor] = s,v
    generateX(anchor)
    generateY(anchor)
    return generateHex(h)

def generateHex(h):
    hexCode=[]
    print(xArray)
    print(yArray)
    for i in range (9):
        rgbs=colorsys.hsv_to_rgb(h/360, xArray[i]/100, yArray[i]/100)
       
        hexs = '#%02x%02x%02x'%(round(rgbs[0]*255),round(rgbs[1]*255),round(rgbs[2]*255))
        hexCode.append(hexs)
        
    return hexCode

