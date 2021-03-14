from tkinter import *
from time import sleep
import random
from random import randint

root = Tk()
###################Click For Info######
def updateMouseType(event):
    global menuOpen,gameStarted
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    #print(x)
    #print(y)
    if (menuOpen==False) and (gameStarted==False):
        if x > 160 :
            if x < 250:
                if y > 90:
                    if y < 770:
                        root.config(cursor="hand2")
                    else:
                        root.config(cursor="arrow")
                else:
                    root.config(cursor="arrow")
            else:
                root.config(cursor="arrow")
        else:
            root.config(cursor="arrow")
            
    elif menuOpen==True:
        if x > 166 :
            if x < 196:
                if y > 110:
                    if y < 140:
                        root.config(cursor="hand2")
                    else:
                        root.config(cursor="arrow")
                else:
                    root.config(cursor="arrow")
            else:
                root.config(cursor="arrow")
        else:
            root.config(cursor="arrow")
######################################################################

################################Movement #############
def trackWeatherToNumber():
    global trackCondition
    if trackCondition== "Sunny and Dry":
        return 0
    else:
        return 1

def movementAlgorithem(horseNumber):
    runningTotal=0
    global H1StatisticsFull,H2StatisticsFull,H3StatisticsFull,H4StatisticsFull,H5StatisticsFull,H6StatisticsFull
    global arrayOfWeatherNumbers, trackCondition
    if horseNumber==1:
        age=H1StatisticsFull[0]
        odds=H1StatisticsFull[2]
        wins=H1StatisticsFull[3]
        weatherInNumbers=H1StatisticsFull[5]
        favourite=(favouriteHorse())
    elif horseNumber==2:
        age=H2StatisticsFull[0]
        odds=H2StatisticsFull[2]
        wins=H2StatisticsFull[3]
        weatherInNumbers=H2StatisticsFull[5]
        favourite=(favouriteHorse())
    elif horseNumber==3:
        age=H3StatisticsFull[0]
        odds=H3StatisticsFull[2]
        wins=H3StatisticsFull[3]
        weatherInNumbers=H3StatisticsFull[5]
        favourite=(favouriteHorse())
    elif horseNumber==4:
        age=H4StatisticsFull[0]
        odds=H4StatisticsFull[2]
        wins=H4StatisticsFull[3]
        weatherInNumbers=H4StatisticsFull[5]
        favourite=(favouriteHorse())
    elif horseNumber==5:
        age=H5StatisticsFull[0]
        odds=H5StatisticsFull[2]
        wins=H5StatisticsFull[3]
        weatherInNumbers=H5StatisticsFull[5]
        favourite=(favouriteHorse())
    elif horseNumber==6:
        age=H6StatisticsFull[0]
        odds=H6StatisticsFull[2]
        wins=H6StatisticsFull[3]
        weatherInNumbers=H6StatisticsFull[5]
        favourite=(favouriteHorse())

    if horseNumber == favourite:
        runningTotal=runningTotal+0.20
    else:
        runningTotal=runningTotal+0.15
    
    if age == 4:
        runningTotal=runningTotal+0.60
    elif age == 5:
        runningTotal=runningTotal+0.70
    elif age == 6:
        runningTotal=runningTotal+0.80
    elif age == 7:
        runningTotal=runningTotal+1
    elif age == 8:
        runningTotal=runningTotal+1
    elif age == 9:
        runningTotal=runningTotal+0.80
    elif age == 10:
        runningTotal=runningTotal+0.70
    elif age == 11:
        runningTotal=runningTotal+0.65
    elif age == 12:
        runningTotal=runningTotal+0.60
    elif age == 13:
        runningTotal=runningTotal+0.55
    elif age == 14:
        runningTotal=runningTotal+0.50
    elif age == 15:
        runningTotal=runningTotal+0.45
    elif age == 16:
        runningTotal=runningTotal+0.40
    else:
        runningTotal=runningTotal+0.35

    if odds == 2:
        runningTotal=runningTotal+0.50
    if odds == 3:
        runningTotal=runningTotal+0.45
    if odds == 4:
        runningTotal=runningTotal+0.40
    if odds == 5:
        runningTotal=runningTotal+0.35
    if odds == 6:
        runningTotal=runningTotal+0.30
    if odds == 7:
        runningTotal=runningTotal+0.25
    if odds == 8:
        runningTotal=runningTotal+0.20
    if odds == 9:
        runningTotal=runningTotal+0.15
    if odds == 10:
        runningTotal=runningTotal+0.10
    x=4
    sunnyWins=0
    wetWins=0
    while x>-1:
        if (wins[x]==1) and (weatherInNumbers[x]==1):
            wetWins=wetWins+1
        elif (wins[x]==1) and (weatherInNumbers[x]==0):
            sunnyWins=sunnyWins+1            
        x=x-1

    if (wetWins>sunnyWins) and (int(trackWeatherToNumber()))==1:
        runningTotal=runningTotal+1
    elif (sunnyWins>wetWins) and (int(trackWeatherToNumber()))==0:
        runningTotal=runningTotal+1

    #print("Wins array:" + str(wins))
    #print("Weather array (numbers):" + str(weatherInNumbers))
    #print("Number of wins in wet conditions:" + str(wetWins))
    #print("Number of wins in sunny conditions:" + str(sunnyWins))
    #print("\n")
    #print (str(horseNumber) + " : " + str(runningTotal))
    return (runningTotal)
    
################################Movement #############

def previousWins():
    previousRaceStats = [randint(0,1),randint(0,1),randint(0,1),randint(0,1),randint(0,1)]
    return previousRaceStats

def previousWeather():
    global arrayOfWeatherNumbers
    x=5
    previousRaceStats=[]
    arrayOfWeatherNumbers=[]
    while x>0:
        randomNumber=randint(0,1)
        arrayOfWeather=["Sunny and Dry", "Wet and Muddy"]
        previousRaceStats.append(arrayOfWeather[randomNumber])
        arrayOfWeatherNumbers.append(randomNumber)
        x=x-1
    return previousRaceStats

def previousWeatherInNumbers():
    global arrayOfWeatherNumbers
    return arrayOfWeatherNumbers

def favouriteHorse():
    global oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6
    arrayOfOdds=[oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6]
    
    if int(min(arrayOfOdds)) == oddsH1:
        return 1
    elif int(min(arrayOfOdds)) == oddsH2:
        return 2
    elif int(min(arrayOfOdds)) == oddsH3:
        return 3
    elif int(min(arrayOfOdds)) == oddsH4:
        return 4
    elif int(min(arrayOfOdds)) == oddsH5:
        return 5
    elif int(min(arrayOfOdds)) == oddsH6:
        return 6

def randomTrainer():    
    namesFile = open('./environment/people/punPeople.txt').read().splitlines()
    randomName = random.choice(namesFile)
    return randomName

def generateIndividualHorseStats(): 
    global H1StatisticsFull,H2StatisticsFull,H3StatisticsFull,H4StatisticsFull,H5StatisticsFull,H6StatisticsFull
    global oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6
    H1StatisticsFull=[randint(3,20),randomTrainer(),oddsH1,previousWins(),previousWeather(),previousWeatherInNumbers()]
    H2StatisticsFull=[randint(3,20),randomTrainer(),oddsH2,previousWins(),previousWeather(),previousWeatherInNumbers()]
    H3StatisticsFull=[randint(3,20),randomTrainer(),oddsH3,previousWins(),previousWeather(),previousWeatherInNumbers()]
    H4StatisticsFull=[randint(3,20),randomTrainer(),oddsH4,previousWins(),previousWeather(),previousWeatherInNumbers()]
    H5StatisticsFull=[randint(3,20),randomTrainer(),oddsH5,previousWins(),previousWeather(),previousWeatherInNumbers()]
    H6StatisticsFull=[randint(3,20),randomTrainer(),oddsH6,previousWins(),previousWeather(),previousWeatherInNumbers()]
    
def writeStatisticsToScreen(horseNumber):
    global menuOpen,trackCondition
    root.config(cursor="arrow")
    if horseNumber ==1:
        horseArray0=H1StatisticsFull[0]
        horseArray1=H1StatisticsFull[1]
        horseArray2=H1StatisticsFull[2]
        wonRaces=H1StatisticsFull[3]
        weatherType=H1StatisticsFull[4]
    elif horseNumber==2:
        horseArray0=H2StatisticsFull[0]
        horseArray1=H2StatisticsFull[1]
        horseArray2=H2StatisticsFull[2]
        wonRaces=H2StatisticsFull[3]
        weatherType=H2StatisticsFull[4]
    elif horseNumber==3:
        horseArray0=H3StatisticsFull[0]
        horseArray1=H3StatisticsFull[1]
        horseArray2=H3StatisticsFull[2]
        wonRaces=H3StatisticsFull[3]
        weatherType=H3StatisticsFull[4]
    elif horseNumber==4:
        horseArray0=H4StatisticsFull[0]
        horseArray1=H4StatisticsFull[1]
        horseArray2=H4StatisticsFull[2]
        wonRaces=H4StatisticsFull[3]
        weatherType=H4StatisticsFull[4]
    elif horseNumber==5:
        horseArray0=H5StatisticsFull[0]
        horseArray1=H5StatisticsFull[1]
        horseArray2=H5StatisticsFull[2]
        wonRaces=H5StatisticsFull[3]
        weatherType=H5StatisticsFull[4]
    elif horseNumber==6:
        horseArray0=H6StatisticsFull[0]
        horseArray1=H6StatisticsFull[1]
        horseArray2=H6StatisticsFull[2]
        wonRaces=H6StatisticsFull[3]
        weatherType=H6StatisticsFull[4]
        
    agePath = (r"./environment/genericNumbers/" + str(horseArray0) + ".gif")
    ageImage = PhotoImage(file=agePath)
    ageItem = canvas1.create_image(300, 395, image=ageImage)#340 # dif = 55
    ageImage.image = ageImage

    oddsGenericPath = (r"./environment/items/toOne.gif")
    oddsGenericImage = PhotoImage(file=oddsGenericPath)
    ageItem = canvas1.create_image(300, 468, image=oddsGenericImage)
    oddsGenericImage.image = oddsGenericImage

    horseOddsPath = (r"./environment/genericNumbers/" + str(horseArray2) + ".gif")
    horseOddsImage = PhotoImage(file=horseOddsPath)
    horseOddsItem = canvas1.create_image(240, 468, image=horseOddsImage)
    horseOddsImage.image = horseOddsImage
    
    nameOfOwner = canvas1.create_text(350, 610)
    canvas1.itemconfig(nameOfOwner, text=horseArray1,font = "Baskerville 35")

####
    xBase=535
    xDiff=100
    horseWeather1 = canvas1.create_text(xBase+(xDiff*0), 300)
    horseWeather2 = canvas1.create_text(xBase+(xDiff*1), 300)
    horseWeather3 = canvas1.create_text(xBase+(xDiff*2), 300)
    horseWeather4 = canvas1.create_text(xBase+(xDiff*3), 300)
    horseWeather5 = canvas1.create_text(xBase+(xDiff*4), 300)
    
    array=[]
    x=4
    while x>-1:
        if weatherType[x] == "Sunny and Dry":
            array.append("Sunny")
        elif weatherType[x] == "Wet and Muddy":
            array.append("Wet")
        x=x-1
  
    canvas1.itemconfig(horseWeather1, text=array[0],font = "Baskerville 20")
    canvas1.itemconfig(horseWeather2, text=array[1],font = "Baskerville 20")
    canvas1.itemconfig(horseWeather3, text=array[2],font = "Baskerville 20")
    canvas1.itemconfig(horseWeather4, text=array[3],font = "Baskerville 20")
    canvas1.itemconfig(horseWeather5, text=array[4],font = "Baskerville 20")

    yBase=345
    horseWin1 = canvas1.create_text(xBase+(xDiff*0), yBase)
    horseWin2 = canvas1.create_text(xBase+(xDiff*1), yBase)
    horseWin3 = canvas1.create_text(xBase+(xDiff*2), yBase)
    horseWin4 = canvas1.create_text(xBase+(xDiff*3), yBase)
    horseWin5 = canvas1.create_text(xBase+(xDiff*4), yBase)
    
    array2=[]
    
    y=4
    while y>-1:
        if wonRaces[y] == 1:
            array2.append("Win")
        elif wonRaces[y] == 0:                 
            array2.append("Lose")
        y=y-1
  
    canvas1.itemconfig(horseWin1, text=array2[0],font = "Baskerville 20")
    canvas1.itemconfig(horseWin2, text=array2[1],font = "Baskerville 20")
    canvas1.itemconfig(horseWin3, text=array2[2],font = "Baskerville 20")
    canvas1.itemconfig(horseWin4, text=array2[3],font = "Baskerville 20")
    canvas1.itemconfig(horseWin5, text=array2[4],font = "Baskerville 20")    

    if horseNumber==favouriteHorse():
        yesPath = (r"./environment/items/yes.gif")
        yesImage = PhotoImage(file=yesPath)
        yesItem = canvas1.create_image(280, 545, image=yesImage)
        yesImage.image = yesImage
    else:
        noPath = (r"./environment/items/no.gif")
        noImage = PhotoImage(file=noPath)
        noItem = canvas1.create_image(280, 545, image=noImage)
        noImage.image = noImage

    currentWeatherConditions = canvas1.create_text(680,520)
    canvas1.itemconfig(currentWeatherConditions, text=trackCondition,font = "Baskerville 50")

    menuOpen=True

def reOrderLevels(event):
    global menuOpen,finishLineItem
    root.config(cursor="arrow")
    canvas1.tag_raise(background)
    canvas1.tag_raise(finishLineItem)
    canvas1.tag_raise(laneOneOdds)
    canvas1.tag_raise(laneTwoOdds)
    canvas1.tag_raise(laneThreeOdds)
    canvas1.tag_raise(laneFourOdds)
    canvas1.tag_raise(laneFiveOdds)
    canvas1.tag_raise(laneSixOdds)
    canvas1.tag_raise(H1OddsPic)
    canvas1.tag_raise(H2OddsPic)
    canvas1.tag_raise(H3OddsPic)
    canvas1.tag_raise(H4OddsPic)
    canvas1.tag_raise(H5OddsPic)
    canvas1.tag_raise(H6OddsPic)
    canvas1.tag_raise(firstHorse)
    canvas1.tag_raise(secondHorse)
    canvas1.tag_raise(thirdHorse)
    canvas1.tag_raise(fourthHorse)
    canvas1.tag_raise(fithHorse)
    canvas1.tag_raise(sixthHorse)
    menuOpen=False
    trophiesOnTrack=False

def H1Clicked(event):
    global gameStarted
    if gameStarted==False:
        
        H1statisticsB = (r"./environment/horseBackgrounds/Horse1.gif")
        H1statistics = PhotoImage(file=H1statisticsB)
        height = H1statistics.height()
        width = H1statistics.width()
        
        H1statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H1statistics)
        H1statistics.image = H1statistics
        
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage

        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)

        writeStatisticsToScreen(1)

########################################################################################################################################################################

def H2Clicked(event):
    global gameStarted
    if gameStarted==False:        
        H2statisticsB = (r"./environment/horseBackgrounds/Horse2.gif")
        H2statistics = PhotoImage(file=H2statisticsB)
        height = H2statistics.height()
        width = H2statistics.width()        
        H2statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H2statistics)
        H2statistics.image = H2statistics        
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage
        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)
        writeStatisticsToScreen(2)

def H3Clicked(event):
    global gameStarted
    if gameStarted==False:        
        H3statisticsB = (r"./environment/horseBackgrounds/Horse3.gif")
        H3statistics = PhotoImage(file=H3statisticsB)
        height = H3statistics.height()
        width = H3statistics.width()        
        H3statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H3statistics)
        H3statistics.image = H3statistics        
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage
        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)
        writeStatisticsToScreen(3)

def H4Clicked(event):
    global gameStarted
    if gameStarted==False:        
        H4statisticsB = (r"./environment/horseBackgrounds/Horse4.gif")
        H4statistics = PhotoImage(file=H4statisticsB)
        height = H4statistics.height()
        width = H4statistics.width()        
        H4statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H4statistics)
        H4statistics.image = H4statistics        
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage
        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)
        writeStatisticsToScreen(4)

def H5Clicked(event):
    global gameStarted
    if gameStarted==False:        
        H5statisticsB = (r"./environment/horseBackgrounds/Horse5.gif")
        H5statistics = PhotoImage(file=H5statisticsB)
        height = H5statistics.height()
        width = H5statistics.width()       
        H5statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H5statistics)
        H5statistics.image = H5statistics       
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage
        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)
        writeStatisticsToScreen(5)

def H6Clicked(event):
    global gameStarted
    if gameStarted==False:        
        H6statisticsB = (r"./environment/horseBackgrounds/Horse6.gif")
        H6statistics = PhotoImage(file=H6statisticsB)
        height = H6statistics.height()
        width = H6statistics.width()        
        H6statisticsBackgroundItem = canvas1.create_image((width/2)-8, height/2, image=H6statistics)
        H6statistics.image = H6statistics        
        genericCloseButton = (r"./environment/items/close.gif")
        genericCloseButtonImage = PhotoImage(file=genericCloseButton)
        genericCloseButtonItem = canvas1.create_image((width/100)*4, (height/100)*6, image=genericCloseButtonImage)
        genericCloseButtonImage.image = genericCloseButtonImage
        canvas1.tag_bind(genericCloseButtonItem, '<ButtonPress-1>', reOrderLevels)
        writeStatisticsToScreen(6)  

###################Click For Info######
    
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
        ######Pleyer 2########
def pbetH1():
    global ptotalMoney,pH1bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH1bets=pH1bets+1
        plb1.config(text=("£" + str(pH1bets)))
    else:
        w1.config(text=("No more bets"))
def pbetH2():
    global ptotalMoney,pH2bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH2bets=pH2bets+1
        plb2.config(text=("£" + str(pH2bets)))
    else:
        w1.config(text=("No more bets"))
def pbetH3():
    global ptotalMoney,pH3bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH3bets=pH3bets+1
        plb3.config(text=("£" + str(pH3bets)))
    else:
        w1.config(text=("No more bets"))
def pbetH4():
    global ptotalMoney,pH4bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH4bets=pH4bets+1
        plb4.config(text=("£" + str(pH4bets)))
    else:
        w1.config(text=("No more bets"))
def pbetH5():
    global ptotalMoney,pH5bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH5bets=pH5bets+1
        plb5.config(text=("£" + str(pH5bets)))
    else:
        w1.config(text=("No more bets"))
def pbetH6():
    global ptotalMoney,pH6bets
    if ptotalMoney>0:
        ptotalMoney=ptotalMoney-1
        plb.config(text=("£" + str(ptotalMoney)))
        pH6bets=pH6bets+1
        plb6.config(text=("£" + str(pH6bets)))
    else:
        w1.config(text=("No more bets"))

################################################

def resetBets():
    global H1bets,H2bets,H3bets,H4bets,H5bets,H6bets,pH1bets,pH2bets,pH3bets,pH4bets,pH5bets,pH6bets
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
    
    pH1bets=0
    plb1.config(text=("£" + str(pH1bets)))
    pH2bets=0
    plb2.config(text=("£" + str(pH2bets)))
    pH3bets=0
    plb3.config(text=("£" + str(pH3bets)))
    pH4bets=0
    plb4.config(text=("£" + str(pH4bets)))
    pH5bets=0
    plb5.config(text=("£" + str(pH5bets)))
    pH6bets=0
    plb6.config(text=("£" + str(pH6bets)))

def repayMoney(w,s):
    global ptotalMoney,totalMoney,H1bets,H2bets,H3bets,H4bets,H5bets,H6bets,pH1bets,pH2bets,pH3bets,pH4bets,pH5bets,pH6bets
    global oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6
    if w == 1:
        totalMoney = totalMoney+(H1bets*(oddsH1))
        ptotalMoney = ptotalMoney+(pH1bets*(oddsH1)) 
    elif w==2:
        totalMoney=totalMoney+(H2bets*(oddsH2))
        ptotalMoney = ptotalMoney+(pH2bets*(oddsH2))
    elif w==3:
        totalMoney=totalMoney+(H3bets*(oddsH3))
        ptotalMoney = ptotalMoney+(pH3bets*(oddsH3))
    elif w==4:
        totalMoney=totalMoney+(H4bets*(oddsH4))
        ptotalMoney = ptotalMoney+(pH4bets*(oddsH4))
    elif w==5:
        totalMoney=totalMoney+(H5bets*(oddsH5))
        ptotalMoney = ptotalMoney+(pH5bets*(oddsH5))
    elif w==6:
        totalMoney=totalMoney+(H6bets*(oddsH6))
        ptotalMoney = ptotalMoney+(pH6bets*(oddsH6))
        
    if s== 1:
        totalMoney = totalMoney+(H1bets)
        ptotalMoney = ptotalMoney+(pH1bets) 
    elif s==2:
        totalMoney=totalMoney+(H2bets)
        ptotalMoney = ptotalMoney+(pH2bets)
    elif s==3:
        totalMoney=totalMoney+(H3bets)
        ptotalMoney = ptotalMoney+(pH3bets)
    elif s==4:
        totalMoney=totalMoney+(H4bets)
        ptotalMoney = ptotalMoney+(pH4bets)
    elif s==5:
        totalMoney=totalMoney+(H5bets)
        ptotalMoney = ptotalMoney+(pH5bets)
    elif s==6:
        totalMoney=totalMoney+(H6bets)
        ptotalMoney = ptotalMoney+(pH6bets)
        
    resetBets()
    lb.config(text=("£" + str(totalMoney)))
    plb.config(text=("£" + str(ptotalMoney)))
    getNewOdds()
    
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
        pb1.config(state=DISABLED)
        pb2.config(state=DISABLED)
        pb3.config(state=DISABLED)
        pb4.config(state=DISABLED)
        pb5.config(state=DISABLED)
        pb6.config(state=DISABLED)
        play.config(state=DISABLED)
    elif x=="enable":
        b1.config(state=NORMAL)
        b2.config(state=NORMAL)
        b3.config(state=NORMAL)
        b4.config(state=NORMAL)
        b5.config(state=NORMAL)
        b6.config(state=NORMAL)
        pb1.config(state=NORMAL)
        pb2.config(state=NORMAL)
        pb3.config(state=NORMAL)
        pb4.config(state=NORMAL)
        pb5.config(state=NORMAL)
        pb6.config(state=NORMAL)
        play.config(state=NORMAL)
        newWeather()
        
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

def putTrophiesOnTrack(lane,position):
    global laneWidth,trophy1on,trophy2on,trophy3on
    if position=="First":
        trophy1on=True
        goldTrophyPath = (r"./environment/items/trophies/0.gif")
        goldTrophyImage = PhotoImage(file=goldTrophyPath)
        goldTrophyItem = canvas1.create_image(finishLineX, (laneWidth)*(int(lane-1)), image=goldTrophyImage)#######################
        goldTrophyImage.image = goldTrophyImage
    if position=="Second":
        trophy2on=True
        silverTrophyPath = (r"./environment/items/trophies/1.gif")
        silverTrophyImage = PhotoImage(file=silverTrophyPath)
        silverTrophyItem = canvas1.create_image(finishLineX, (laneWidth)*(int(lane-1)), image=silverTrophyImage)#######################
        silverTrophyImage.image = silverTrophyImage
    if position=="Third":
        trophy3on=True
        bronzeTrophyPath = (r"./environment/items/trophies/2.gif")
        bronzeTrophyImage = PhotoImage(file=bronzeTrophyPath)
        bronzeTrophyItem = canvas1.create_image(finishLineX, (laneWidth)*(int(lane-1)), image=bronzeTrophyImage)#######################
        bronzeTrophyImage.image = bronzeTrophyImage
    
def displayWinner(Horse1st):
    global H1Stop,H2Stop,H3Stop,H4Stop,H5Stop,H6Stop,trophy1on,trophy2on,trophy3on
    w1.config(text=("Horse " + str(Horse1st) + " wins!"))
    ##Load next race screen?
    H1Stop=H2Stop=H3Stop=H4Stop=H5Stop=H6Stop=False
    trophy1on=trophy2on=trophy3on=False
    reOrderLevels("e")

def eachButtonPress():
    global gameStarted,h1X,h2X,h3X,h4X,h5X,h6X, finishLineX,horseWidth, finishLineWidth,winArray
    global H1Stop,H2Stop,H3Stop,H4Stop,H5Stop,H6Stop
    if gameStarted==True:
        w1.config(text=("Race in progress"))

    moreThan=(horseWidth*2)-finishLineWidth/2
    
    if (len(winArray))>2:
        gameStarted=False
        displayWinner(winArray[0])
        repayMoney(winArray[0],winArray[1])
        enableOrDisableButtons("enable")
        resetAllHorses()
        reOrderLevels("e")
        winArray=[]
    #
    if h1X+(moreThan)>finishLineX:
        winArray.append(1)
        h1X=0
        H1Stop=True
    if h2X+(moreThan)>finishLineX:
        winArray.append(2)
        h2X=0
        H2Stop=True
    if h3X+(moreThan)>finishLineX:
        winArray.append(3)
        h3X=0
        H3Stop=True
    if h4X+(moreThan)>finishLineX:
        winArray.append(4)
        h4X=0
        H4Stop=True
    if h5X+(moreThan)>finishLineX:
        winArray.append(5)
        h5X=0
        H5Stop=True
    if h6X+(moreThan)>finishLineX:
        winArray.append(6)
        h6X=0
        H6Stop=True
    #
    
def newWeather():
    global trackCondition
    randomNumber=randint(0,1)
    arrayOfWeather=["Sunny and Dry", "Wet and Muddy"]
    trackCondition= arrayOfWeather[randomNumber]
  
def resetValues():
    global h1X,h2X,h3X,h4X,h5X,h6X,gameStarted,totalMoney,H1bets,H2bets,H3bets,H4bets,H5bets,H6bets, winner
    global ptotalMoney,pH1bets,pH2bets,pH3bets,pH4bets,pH5bets,pH6bets,menuOpen
    global winArray,H1Stop,H2Stop,H3Stop,H4Stop,H5Stop,H6Stop,finishLineItem,trophy1on,trophy2on,trophy3on    
    H1Stop=H2Stop=H3Stop=H4Stop=H5Stop=H6Stop=False
    trophy1on=trophy2on=trophy3on=False
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
    pH1bets=0
    pH2bets=0
    pH3bets=0
    pH4bets=0
    pH5bets=0
    pH6bets=0
    winArray=[]
    gameStarted=False
    winner=False
    menuOpen=False
    ptotalMoney=10
    totalMoney=10
    newWeather()
    getNewOdds()

####AutoHorseMovement######+NewOdds

def moveHorseWithOdds():
    global oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6,H1Stop,H2Stop,H3Stop,H4Stop,H5Stop,H6Stop
    if H1Stop==False:
        horse1move(movementAlgorithem(1))
    if H2Stop==False:    
        horse2move(movementAlgorithem(2))
    if H3Stop==False:
        horse3move(movementAlgorithem(3))
    if H4Stop==False:
        horse4move(movementAlgorithem(4))
    if H5Stop==False:
        horse5move(movementAlgorithem(5))
    if H6Stop==False:
        horse6move(movementAlgorithem(6))

    ###########################################################################################

def getNewOdds():
    global oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6,H1OddsPic,H2OddsPic,H3OddsPic,H4OddsPic,H5OddsPic,H6OddsPic
    global H1age,H2age,H3age,H4age,H5age,H6age
    H1age = randint(3,20)
    H2age = randint(3,20)
    H3age = randint(3,20)
    H4age = randint(3,20)
    H5age = randint(3,20)
    H6age = randint(3,20)
    oddsH1=randint(2,10)    
    oddsH2=randint(2,10)
    oddsH3=randint(2,10)
    oddsH4=randint(2,10)
    oddsH5=randint(2,10)
    oddsH6=randint(2,10)
    print(oddsH1,oddsH2,oddsH3,oddsH4,oddsH5,oddsH6)
    
    generateIndividualHorseStats()

    #overWritePhotoPath=(r"./2.gif")
    #overWritePhoto=PhotoImage(file=overWritePhotoPath)
    #H1OddsPic=canvas1.create_image(440,y,image=overWritePhoto)
    #overWritePhoto.image = overWritePhoto

    #H1=(r"./Folder/1.gif")
    xVar=325
    H1 = (r"./environment/oddsForTrack/" + str(oddsH1) + ".gif")
    H1Photo = PhotoImage(file=H1)
    H1OddsPic = canvas1.create_image(xVar, y+(laneWidth*0), image=H1Photo)
    H1Photo.image = H1Photo
    H2 = (r"./environment/oddsForTrack/" + str(oddsH2) + ".gif")
    H2Photo = PhotoImage(file=H2)
    H2OddsPic = canvas1.create_image(xVar, y+(laneWidth*1), image=H2Photo)
    H2Photo.image = H2Photo
    H3 = (r"./environment/oddsForTrack/" + str(oddsH3) + ".gif")
    H3Photo = PhotoImage(file=H3)
    H3OddsPic = canvas1.create_image(xVar, y+(laneWidth*2), image=H3Photo)
    H3Photo.image = H3Photo
    H4 = (r"./environment/oddsForTrack/" + str(oddsH4) + ".gif")
    H4Photo = PhotoImage(file=H4)
    H4OddsPic = canvas1.create_image(xVar, y+(laneWidth*3), image=H4Photo)
    H4Photo.image = H4Photo
    H5 = (r"./environment/oddsForTrack/" + str(oddsH5) + ".gif")
    H5Photo = PhotoImage(file=H5)
    H5OddsPic = canvas1.create_image(xVar, y+(laneWidth*4), image=H5Photo)
    H5Photo.image = H5Photo
    H6 = (r"./environment/oddsForTrack/" + str(oddsH6) + ".gif")
    H6Photo = PhotoImage(file=H6)
    H6OddsPic = canvas1.create_image(xVar, y+(laneWidth*5), image=H6Photo)
    H6Photo.image = H6Photo
    canvas1.tag_raise(firstHorse)
    canvas1.tag_raise(secondHorse)
    canvas1.tag_raise(thirdHorse)
    canvas1.tag_raise(fourthHorse)
    canvas1.tag_raise(fithHorse)
    canvas1.tag_raise(sixthHorse)

####AutoHorseMovement######+NewOdds
    
def horse1move(xMove):
    global h1X, winner
    if gameStarted==True:
        canvas1.move(firstHorse, (xMove), 0)
        h1X = h1X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse2move(xMove):
    global h2X
    if gameStarted==True:
        canvas1.move(secondHorse, (xMove), 0)
        h2X = h2X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse3move(xMove):
    global h3X
    if gameStarted==True:
        canvas1.move(thirdHorse, (xMove), 0)
        h3X = h3X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse4move(xMove):
    global h4X
    if gameStarted==True:
        canvas1.move(fourthHorse, (xMove), 0)
        h4X = h4X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse5move(xMove):
    global h5X
    if gameStarted==True:
        canvas1.move(fithHorse, (xMove), 0)
        h5X = h5X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()
def horse6move(xMove):
    global h6X
    if gameStarted==True:
        canvas1.move(sixthHorse, (xMove), 0)
        h6X = h6X+(xMove)
        eachButtonPress()
    else:
        gameNotStarted()
        eachButtonPress()

###########################
image1 = r"./environment/horses/Horse1.gif"
photo1 = PhotoImage(file=image1)
image2 = r"./environment/horses/Horse2.gif"
photo2 = PhotoImage(file=image2)
image3 = r"./environment/horses/Horse3.gif"
photo3 = PhotoImage(file=image3)
image4 = r"./environment/horses/Horse4.gif"
photo4 = PhotoImage(file=image4)
image5 = r"./environment/horses/Horse5.gif"
photo5 = PhotoImage(file=image5)
image6 = r"./environment/horses/Horse6.gif"
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
canvas1.grid(row = 1, column = 2, rowspan=12,columnspan=10)
global horseHeight,horseWidth,laneWidth
horseHeight = photo1.height()
horseWidth = photo1.width()

x = horseHeight/2
y = horseWidth/2
#To add 1/6 of the background height
laneWidth=0
laneWidth=(bheight1/6)

background = canvas1.create_image(bx, by, image=bphoto1)

#############################Put Odds On Track ###################
xVar2=320
genericOdds = r"./environment/track/genericOdds.gif"
genericOdds1 = PhotoImage(file=genericOdds)
laneOneOdds = canvas1.create_image(xVar2, y+(laneWidth*0), image=genericOdds1)
laneTwoOdds = canvas1.create_image(xVar2, y+(laneWidth*1), image=genericOdds1)
laneThreeOdds = canvas1.create_image(xVar2, y+(laneWidth*2), image=genericOdds1)
laneFourOdds = canvas1.create_image(xVar2, y+(laneWidth*3), image=genericOdds1)
laneFiveOdds = canvas1.create_image(xVar2, y+(laneWidth*4), image=genericOdds1)
laneSixOdds = canvas1.create_image(xVar2, y+(laneWidth*5), image=genericOdds1)

#############################Put Odds On Track ###################

firstHorse = canvas1.create_image(x, y+(laneWidth*0), image=photo1)
secondHorse = canvas1.create_image(x, (y+(laneWidth*1)), image=photo2)
thirdHorse = canvas1.create_image(x, (y+(laneWidth*2)), image=photo3)
fourthHorse = canvas1.create_image(x, (y+(laneWidth*3)), image=photo4)
fithHorse = canvas1.create_image(x, (y+(laneWidth*4)), image=photo5)
sixthHorse = canvas1.create_image(x, (y+(laneWidth*5)), image=photo6)

resetValues()

fontforbets="Sans 20"
b1=Button(text="Bet Win P1",command=betH1)
b1.grid(row = 1, column = 0)
lb1 = Label(root, text="£" + str(H1bets),font = fontforbets)
lb1.grid(row=2,column=0)
b2=Button(text="Bet Win P1",command=betH2)
b2.grid(row = 3, column = 0)
lb2 = Label(root, text="£" +str(H2bets),font = fontforbets)
lb2.grid(row=4,column=0)
b3=Button(text="Bet Win P1",command=betH3)
b3.grid(row = 5, column = 0)
lb3 = Label(root, text="£" +str(H3bets),font = fontforbets)
lb3.grid(row=6,column=0)
b4=Button(text="Bet Win P1",command=betH4)
b4.grid(row = 7, column = 0)
lb4 = Label(root, text="£" +str(H4bets),font = fontforbets)
lb4.grid(row=8,column=0)
b5=Button(text="Bet Win P1",command=betH5)
b5.grid(row = 9, column = 0)
lb5 = Label(root, text="£" +str(H5bets),font = fontforbets)
lb5.grid(row=10,column=0)
b6=Button(text="Bet Win P1",command=betH6)
b6.grid(row = 11, column = 0)
lb6 = Label(root, text="£" +str(H6bets),font = fontforbets)
lb6.grid(row=12,column=0)

################
pb1=Button(text="Bet Win P2",command=pbetH1)
pb1.grid(row = 1, column = 1)
plb1 = Label(root, text="£" + str(pH1bets),font = fontforbets)
plb1.grid(row=2,column=1)
pb2=Button(text="Bet Win P2",command=pbetH2)
pb2.grid(row = 3, column = 1)
plb2 = Label(root, text="£" +str(pH2bets),font = fontforbets)
plb2.grid(row=4,column=1)
pb3=Button(text="Bet Win P2",command=pbetH3)
pb3.grid(row = 5, column = 1)
plb3 = Label(root, text="£" +str(pH3bets),font = fontforbets)
plb3.grid(row=6,column=1)
pb4=Button(text="Bet Win P2",command=pbetH4)
pb4.grid(row = 7, column = 1)
plb4 = Label(root, text="£" +str(pH4bets),font = fontforbets)
plb4.grid(row=8,column=1)
pb5=Button(text="Bet Win P2",command=pbetH5)
pb5.grid(row = 9, column = 1)
plb5 = Label(root, text="£" +str(pH5bets),font = fontforbets)
plb5.grid(row=10,column=1)
pb6=Button(text="Bet Win P2",command=pbetH6)
pb6.grid(row = 11, column = 1)
plb6 = Label(root, text="£" +str(pH6bets),font = fontforbets)
plb6.grid(row=12,column=1)
###################
#######Finish Line######################

finishLineX=800
finishLine = (r"./environment/items/finishLine.gif")
finishLinePhoto = PhotoImage(file=finishLine)
finishLineHeight=finishLinePhoto.height()
finishLineWidth=finishLinePhoto.width()
finishLineItem = canvas1.create_image(finishLineX, finishLineHeight/2, image=finishLinePhoto)
#finishLinePhoto.image = finishLinePhoto

########################################

play= Button(text=("Play Game!"),font = "Helvetica 15 bold italic",command=startGame)
play.grid(row=0,column=0,columnspan=2)

w1 = Label(root, text="Please place bets",font = "Helvetica 30 bold italic")
w1.grid(row=0,column=2)

w2 = Label(root, text="P1 Balance:",font = "Calibri 25 bold")
w2.grid(row=0,column=3)
lb = Label(root,text= ("£" + str(totalMoney)),font = "Calibri 20")
lb.grid(row=0,column=4)

pw2 = Label(root, text="P2 Balance:",font = "Calibri 25 bold")
pw2.grid(row=0,column=5)
plb = Label(root,text= ("£" + str(ptotalMoney)),font = "Calibri 20")
plb.grid(row=0,column=6) 

canvas1.tag_bind(firstHorse, '<ButtonPress-1>', H1Clicked)
canvas1.tag_bind(secondHorse, '<ButtonPress-1>', H2Clicked)
canvas1.tag_bind(thirdHorse, '<ButtonPress-1>', H3Clicked)
canvas1.tag_bind(fourthHorse, '<ButtonPress-1>', H4Clicked)
canvas1.tag_bind(fithHorse, '<ButtonPress-1>', H5Clicked)
canvas1.tag_bind(sixthHorse, '<ButtonPress-1>', H6Clicked)

root.bind('<Motion>', updateMouseType)

menubar = Menu(root)
def hello():
    print("Hi")


rulesForGame2="""About:

This game was created in python by the living legend Felix"""

rulesForGame="""How To Play:

1. Click on each horse to see its previous Race Performances

2. Player 1: Click on the 'Bet Win P1' buttons next to each horse to bet £1 on that horse
3. Player 2: Click on the 'Bet Win P2' buttons next to each horse to bet £1 on that horse

4. Click 'Start Game' once all bets have been placed to start the horses"""


def rules():
    toplevel = Toplevel()
    label = Label(toplevel, text= (str(rulesForGame)),font = "Calibri 20",height=0,width = 0)
    label.pack()

def rules2():
    toplevel = Toplevel()
    label = Label(toplevel, text= (str(rulesForGame2)),font = "Calibri 20",height=0,width = 0)
    label.pack()
    
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=rules)
filemenu.add_command(label="Save", command=rules2)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Game", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
#editmenu.add_command(label="Cut", command=hello)
#editmenu.add_command(label="Copy", command=hello)
menubar.add_cascade(label="Testing Commands", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="How To Play", command=rules)
helpmenu.add_command(label="About", command=rules2)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
root.title("Digital Horse Racing 2.0")

while True:
    while winner==False:
        moveHorseWithOdds()
        canvas1.update()    

root.mainloop()
#http://betoclock.com/how-to-read-a-horse-racing-program/?authent_user=TheJohnofGauntSchoolTrowbridge%5C11FAldam-Gates&authent_user_sig=f291086beaabeb14cbeb5707b99b0b8b&authent_session=4a9f3a9fc45a96f4815450fdb0a34fc8&authent_session_sig=5297dd9c5b54b53525ad2d390225dde6
