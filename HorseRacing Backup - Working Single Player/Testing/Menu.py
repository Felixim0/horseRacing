from tkinter import *
import os
root=Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

def Button4ARG():
   print("BUTTON4")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/SD.bat")

def Button3ARG():
   print("BUTTON3")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/RB.exe")
   
def Button2ARG():
   print("BUTTON2")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/SPM.bat")

def Button1ARG():
   print ("BUTTON1")
   currentD = (os.getcwd() + "/Programs/pball")
   os.startfile(currentD + "/paintball2.exe")

#######################

def Button17ARG():
   print("BUTTON17")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/Lock.exe")

def Button16ARG():
   print("BUTTON16")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/RBG.exe")

def Button15ARG():
   print("BUTTON15")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/RDP.bat")

def Button14ARG():
   print("BUTTON14")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/STRS.exe")

def Button13ARG():
   print("BUTTON13")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/TV8.exe")

def Button12ARG():
   print("BUTTON12")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/MATRX.bat")
   
def Button11ARG():
   print("BUTTON11")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/EXPLKILL.bat")

def Button10ARG():
   print("BUTTON10")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/NICOFF.bat")

def Button9ARG():
   print("BUTTON9")
   currentD = (os.getcwd() + "/Programs/VBS")
   os.startfile(currentD + "/CDDeath.vbs")

def Button8ARG():
   print("BUTTON8")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/C.bat")

def Button7ARG():
   print("BUTTON7")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/CMD.bat")

def Button6ARG():
   print("BUTTON6")
   currentD = (os.getcwd() + "/Programs/VBS")
   os.startfile(currentD + "/message.vbs")

def Button5ARG():
   print("BUTTON5")
   currentD = (os.getcwd() + "/Programs")
   os.startfile(currentD + "/DSD.bat")
   

currentD = (os.getcwd() + "/buttonPics/")

button1 = Button(bottomframe, text="Red", fg="red", command = Button1ARG)
b1img=PhotoImage(file=currentD + "Picture1.gif")
button1.config(image=b1img)
button1.grid(row=0,column=0)

button2 = Button(bottomframe, text="Red", fg="red", command = Button2ARG)
b2img=PhotoImage(file=currentD + "Picture2.gif")
button2.config(image=b2img)
button2.grid(row=0,column=1)

button3 = Button(bottomframe, text="Red", fg="red", command = Button3ARG)
b3img=PhotoImage(file=currentD + "Picture3.gif")
button3.config(image=b3img)
button3.grid(row=0,column=2)

button4 = Button(bottomframe, text="Black", fg="black", command = Button4ARG)
b4img=PhotoImage(file=currentD + "Picture4.gif")
button4.config(image=b4img)
button4.grid(row=0,column=3)


################
################

button5 = Button(bottomframe, text="Red", fg="red", command = Button5ARG)
b5img=PhotoImage(file=currentD + "Picture5.gif")
button5.config(image=b5img)
button5.grid(row=2,column=0)

button6 = Button(bottomframe, text="Red", fg="red", command = Button6ARG)
b6img=PhotoImage(file=currentD + "Picture6.gif")
button6.config(image=b6img)
button6.grid(row=2,column=1)

button7 = Button(bottomframe, text="Red", fg="red", command = Button7ARG)
b7img=PhotoImage(file=currentD + "Picture7.gif")
button7.config(image=b7img)
button7.grid(row=2,column=2)

button8 = Button(bottomframe, text="Black", fg="black", command = Button8ARG)
b8img=PhotoImage(file=currentD + "Picture8.gif")
button8.config(image=b8img)
button8.grid(row=2,column=3)

##################
##################

button9 = Button(bottomframe, text="Black", fg="black", command = Button9ARG)
b9img=PhotoImage(file=currentD + "Picture9.gif")
button9.config(image=b9img)
button9.grid(row=3,column=0)

button10 = Button(bottomframe, text="Red", fg="red", command = Button10ARG)
b10img=PhotoImage(file=currentD + "Picture10.gif")
button10.config(image=b10img)
button10.grid(row=3,column=1)

button11 = Button(bottomframe, text="Red", fg="red", command = Button11ARG)
b11img=PhotoImage(file=currentD + "Picture11.gif")
button11.config(image=b11img)
button11.grid(row=3,column=2)

button12 = Button(bottomframe, text="Red", fg="red", command = Button12ARG)
b12img=PhotoImage(file=currentD + "Picture12.gif")
button12.config(image=b12img)
button12.grid(row=3,column=3)

##################
##################

button13 = Button(bottomframe, text="Red", fg="red", command = Button13ARG)
b13img=PhotoImage(file=currentD + "Picture13.gif")
button13.config(image=b13img)
button13.grid(row=4,column=0)

button14 = Button(bottomframe, text="Red", fg="red", command = Button14ARG)
b14img=PhotoImage(file=currentD + "Picture14.gif")
button14.config(image=b14img)
button14.grid(row=4,column=1)

button15 = Button(bottomframe, text="Red", fg="red", command = Button15ARG)
b15img=PhotoImage(file=currentD + "Picture15.gif")
button15.config(image=b15img)
button15.grid(row=4,column=2)

button16 = Button(bottomframe, text="Red", fg="red", command = Button16ARG)
b16img=PhotoImage(file=currentD + "Picture16.gif")
button16.config(image=b16img)
button16.grid(row=4,column=3)

##################
##################

button17 = Button(bottomframe, text="Red", fg="red", command = Button17ARG)
b17img=PhotoImage(file=currentD + "Picture17.gif")
button17.config(image=b17img)
button17.grid(row=5,column=0)

root.mainloop()




