from tkinter import *
from time import sleep
root = Tk()
##################Betting##########
def betH1():
    global totalMoney,H1bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H1bets=H1bets+1
        lb1.config(text=("£" + str(H1bets)))
    else:
        w1.config(text=("No more bets"))
def betH2():
    global totalMoney,H2bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H2bets=H2bets+1
        lb2.config(text=("£" + str(H2bets)))
    else:
        w1.config(text=("No more bets"))
def betH3():
    global totalMoney,H3bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H3bets=H3bets+1
        lb3.config(text=("£" + str(H3bets)))
    else:
        w1.config(text=("No more bets"))
def betH4():
    global totalMoney,H4bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H4bets=H4bets+1
        lb4.config(text=("£" + str(H4bets)))
    else:
        w1.config(text=("No more bets"))
def betH5():
    global totalMoney,H5bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H5bets=H5bets+1
        lb5.config(text=("£" + str(H5bets)))
    else:
        w1.config(text=("No more bets"))
def betH6():
    global totalMoney,H6bets
    if totalMoney>0:
        totalMoney=totalMoney-1
        lb.config(text=("£" + str(totalMoney)))
        H6bets=H6bets+1
        lb6.config(text=("£" + str(H6bets)))
    else:
        w1.config(text=("No more bets"))
##################Betting##########

def resetBets():
    global H1bets,H2bets,H3bets,H4bets,H5bets,H6bets
    H1bets=0
    lb1.config(text=("£" + str(H1bets)))
    H2bets=0
    lb2.config(text=("£" + str(H2bets)))
    H3bets=0
    lb3.config(text=("£" + str(H3bets)))
    H4bets=0
    lb4.config(text=("£" + str(H4bets)))
    H5bets=0
    lb5.config(text=("£" + str(H5bets)))
    H6bets=0
    lb6.config(text=("£" + str(H6bets)))

def repayMoney(w):
    global totalMoney,H1bets,H2bets,H3bets,H4bets,H5bets,H6bets
    if w == 1:
        totalMoney = totalMoney+(H1bets*2)
        resetBets()
        resetAllHorses()
    elif w==2:
        totalMoney=totalMoney+(H2bets*2)
        resetBets()
        resetAllHorses()
    elif w==3:
        totalMoney=totalMoney+(H3bets*2)
        resetBets()
        resetAllHorses()
    elif w==4:
        totalMoney=totalMoney+(H4bets*2)
        resetBets()
        resetAllHorses()
    elif w==5:
        totalMoney=totalMoney+(H5bets*2)
        resetBets()
        resetAllHorses()
    elif w==6:
        totalMoney=totalMoney+(H6bets*2)
        resetBets()
        resetAllHorses()
    lb.config(text=("£" + str(totalMoney)))
    
##################Betting##########
    
##################Reset Horses Position##########

def resetAllHorses():
    canvas1.coords(firstHorse,x, y+(laneWidth*0))
    canvas1.coords(secondHorse,x, y+(laneWidth*1))
    canvas1.coords(thirdHorse,x, y+(laneWidth*2))
    canvas1.coords(fourthHorse,x, y+(laneWidth*3))
    canvas1.coords(fithHorse,x, y+(laneWidth*4))
    canvas1.coords(sixthHorse,x, y+(laneWidth*5))
    
##################Reset Horses Position##########
def gameNotStarted():
    generic=True

def enableOrDisableButtons(x):
    if x == "disable":
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
    elif x=="enable":
        b1.config(state=NORMAL)
        b2.config(state=NORMAL)
        b3.config(state=NORMAL)
        b4.config(state=NORMAL)
        b5.config(state=NORMAL)
        b6.config(state=NORMAL)
        
def startGame():
    global gameStarted,h1X,h2X,h3X,h4X,h5X,h6X
    h1X=0
    h2X=0
    h3X=0
    h4X=0
    h5X=0
    h6X=0
    enableOrDisableButtons("disable")
    gameStarted=True
    sleep(0.1)
    w1.config(text=("Race in progress"))
    

def eachButtonPress():
    global gameStarted,h1X,h2X,h3X,h4X,h5X,h6X
    ####print (h1X,h2X,h3X,h4X,h5X,h6X)
    if gameStarted==True:
        w1.config(text=("Race in progress"))
        
    if h1X>1120:
        gameStarted=False
        w1.config(text=("Horse 1 Wins"))
        h1X=0
        repayMoney(1)
        enableOrDisableButtons("enable")
    if h2X>1120:
        gameStarted=False
        w1.config(text=("Horse 2 Wins"))
        h2X=0
        repayMoney(2)
        enableOrDisableButtons("enable")
    if h3X>1120:
        gameStarted=False
        w1.config(text=("Horse 3 Wins"))
        h3X=0
        repayMoney(3)
        enableOrDisableButtons("enable")
    if h4X>1120:
        gameStarted=False
        w1.config(text=("Horse 4 Wins"))
        h4X=0
        repayMoney(4)
        enableOrDisableButtons("enable")
    if h5X>1120:
        gameStarted=False
        w1.config(text=("Horse 5 Wins"))
        h5X=0
        repayMoney(5)
        enableOrDisableButtons("enable")
    if h6X>1120:
        gameStarted=False
        w1.config(text=("Horse 6 Wins"))
        h6X=0
        repayMoney(6)
        enableOrDisableButtons("enable")
    
def resetValues():
    global h1X,h2X,h3X,h4X,h5X,h6X,gameStarted,totalMoney,H1bets,H2bets,H3bets,H4bets,H5bets,H6bets, winner
    h1X=0
    h2X=0
    h3X=0
    h4X=0
    h5X=0
    h6X=0
    H1bets=0
    H2bets=0
    H3bets=0
    H4bets=0
    H5bets=0
    H6bets=0
    gameStarted=False
    totalMoney=10
    winner=False
def horse1move(event):
    global h1X, winner
    if gameStarted==True:
        canvas1.move(firstHorse, 20, 0)
        h1X = h1X+20
        #print(canvas1.coords(firstHorse))
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse2move(event):
    global h2X
    if gameStarted==True:
        canvas1.move(secondHorse, 20, 0)
        h2X = h2X+20
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse3move(event):
    global h3X
    if gameStarted==True:
        canvas1.move(thirdHorse, 20, 0)
        h3X = h3X+20
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse4move(event):
    global h4X
    if gameStarted==True:
        canvas1.move(fourthHorse, 20, 0)
        h4X = h4X+20
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse5move(event):
    global h5X
    if gameStarted==True:
        canvas1.move(fithHorse, 20, 0)
        h5X = h5X+20
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse6move(event):
    global h6X
    if gameStarted==True:
        canvas1.move(sixthHorse, 20, 0)
        h6X = h6X+20
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
####
image1 = r".\Horses\Horse1.gif"
photo1 = PhotoImage(file=image1)
image2 = r".\Horses\Horse2.gif"
photo2 = PhotoImage(file=image2)
image3 = r".\Horses\Horse3.gif"
photo3 = PhotoImage(file=image3)
image4 = r".\Horses\Horse4.gif"
photo4 = PhotoImage(file=image4)
image5 = r".\Horses\Horse5.gif"
photo5 = PhotoImage(file=image5)
image6 = r".\Horses\Horse6.gif"
photo6 = PhotoImage(file=image6)
####

####BACKGROUND######
bimage1 = r".\background.gif"
bphoto1 = PhotoImage(file=bimage1)
bwidth1 = bphoto1.width()
bheight1 = bphoto1.height()
bx=(bwidth1)/2
by=(bheight1)/2
####BACKGROUND######

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas1 = Canvas(width=bwidth1,height=bheight1)#Canvas(width=screen_width, height=screen_height)
canvas1.grid(row = 1, column = 1, rowspan=12,columnspan=10)

horseHeight = photo1.height()
horseWidth = photo1.width()

x = horseHeight/2
y = horseWidth/2
#To add 1/6 of the background height
laneWidth=0
laneWidth=(bheight1/6)

backgound = canvas1.create_image(bx, by, image=bphoto1)

firstHorse = canvas1.create_image(x, y+(laneWidth*0), image=photo1)
secondHorse = canvas1.create_image(x, (y+(laneWidth*1)), image=photo2)
thirdHorse = canvas1.create_image(x, (y+(laneWidth*2)), image=photo3)
fourthHorse = canvas1.create_image(x, (y+(laneWidth*3)), image=photo4)
fithHorse = canvas1.create_image(x, (y+(laneWidth*4)), image=photo5)
sixthHorse = canvas1.create_image(x, (y+(laneWidth*5)), image=photo6)

root.bind('1', horse1move)
root.bind('2', horse2move)
root.bind('3', horse3move)
root.bind('8', horse4move)
root.bind('9', horse5move)
root.bind('0', horse6move)
resetValues()

fontforbets="Sans 20"
b1=Button(text="Bet Win (Key1)",command=betH1)
b1.grid(row = 1, column = 0)
lb1 = Label(root, text="£" + str(H1bets),font = fontforbets)
lb1.grid(row=2,column=0)
b2=Button(text="Bet Win (Key2)",command=betH2)
b2.grid(row = 3, column = 0)
lb2 = Label(root, text="£" +str(H2bets),font = fontforbets)
lb2.grid(row=4,column=0)
b3=Button(text="Bet Win (Key3)",command=betH3)
b3.grid(row = 5, column = 0)
lb3 = Label(root, text="£" +str(H3bets),font = fontforbets)
lb3.grid(row=6,column=0)
b4=Button(text="Bet Win (Key8)",command=betH4)
b4.grid(row = 7, column = 0)
lb4 = Label(root, text="£" +str(H4bets),font = fontforbets)
lb4.grid(row=8,column=0)
b5=Button(text="Bet Win (Key9)",command=betH5)
b5.grid(row = 9, column = 0)
lb5 = Label(root, text="£" +str(H5bets),font = fontforbets)
lb5.grid(row=10,column=0)
b6=Button(text="Bet Win (Key0)",command=betH6)
b6.grid(row = 11, column = 0)
lb6 = Label(root, text="£" +str(H6bets),font = fontforbets)
lb6.grid(row=12,column=0)

play= Button(text=("Play Game!"),font = "Helvetica 15 bold italic",command=startGame)
play.grid(row=0,column=0)

w1 = Label(root, text="Please place bets",font = "Helvetica 30 bold italic")
w1.grid(row=0,column=1)
#w1.config(text=("Newtext"))
w2 = Label(root, text="Your Balance:",font = "Calibri 25 bold")
w2.grid(row=0,column=2)

lb = Label(root,text= ("£" + str(totalMoney)),font = "Calibri 20")
lb.grid(row=0,column=3)

root.mainloop() 
