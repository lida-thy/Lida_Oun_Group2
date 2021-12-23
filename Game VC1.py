
import tkinter as tk
import random
import winsound
window = tk.Tk()
window.geometry("800x500")
frame = tk.Frame()
frame.master.title("Shooting Game")
canvas=tk.Canvas(frame)
# Image===============================================================
backgroun = tk.PhotoImage(file="Image/Background.png")
Hero = tk.PhotoImage(file="Image/amei.png")
annamei = tk.PhotoImage(file="Image/anamei.png")
#Globle Variable=======================================================
Grid_Game=[
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
          ]
# Display Grid=======================================================

def Grid_background():
    canvas.delete("all")
    backgrounGame()
    global Grid_Game
    y1=0
    y2=50
    for num in range(len(Grid_Game)):
        x1=0
        x2=50
        for value in range (len(Grid_Game[num])):
            if Grid_Game[num][value]==1 and  Grid_Game[num][value]!=3:
                canvas.delete("move")
                canvas.create_image(x1+25,y1+25,image=Hero,tags="move")
            elif Grid_Game[num][value]==0 :
                canvas.create_rectangle(x1,y1,x2,y2,fill="",outline="")
            elif Grid_Game[num][value]==3:
                canvas.create_image(x1+25,y1+25,image=annamei,tags="move")
            x1=x2
            x2+=50
        y1=y2
        y2+=50
#--------------------move to right---------------------------------------
def MoveToRight(event):
    global Grid_Game
    check=True
    for index in range(len(Grid_Game)):
        for i in range(len(Grid_Game[index])-1):
            if Grid_Game[index][i]==1 and check :
                Grid_Game[index][i]=0
                Grid_Game[index][i+1]=1
                check=False
    Grid_background()
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#-------------------move to left--------------------------------------
def moveToLeft(event):
    global Grid_Game
    check=True
    for index in range(len(Grid_Game)):
        for i in range(1,len(Grid_Game[index])):
            if Grid_Game[index][i]==1 and check :
                Grid_Game[index][i]=0
                Grid_Game[index][i-1]=1
                check=False
    Grid_background()
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#-----------------move up---------------------------------------------
def moveUp(event):
    global Grid_Game
    Stop=True
    for row in  range(len(Grid_Game)):
        for col in range(len(Grid_Game[0])):
            if Grid_Game[row][col]==1 and row>7 and Stop :
                Grid_Game[row][col]=0
                Grid_Game[row-1][col]=1
                Stop=False
    Grid_background()
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#------------------move down-----------------------------------------
def moveDown(event):
    global Grid_Game
    Stop=True
    for row in  range(len(Grid_Game)):
        for col in range(len(Grid_Game[0])):
            if Grid_Game[row][col]==1 and row<len(Grid_Game)-1 and Stop :
                Grid_Game[row][col]=0
                Grid_Game[row+1][col]=1
                Stop=False
    Grid_background()
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#---------------------background image-----------------------------------
def backgrounGame():
    canvas.create_image(400,250,image=backgroun)


#--------------------random anamei----------------------------------------

def anameiRandom():
    global Grid_Game
    place=random.randrange(8,10)
    for idx in range(len(Grid_Game)):
        for index in range(len(Grid_Game[idx])):
            if idx==place and index==15 and Grid_Game[idx][index]==0:
                Grid_Game[idx][index]=3
    Grid_background()
    print(Grid_Game)
# Button------------------------------------------------------------------
def button_Click_play():
    winsound.PlaySound("Sound/sound back.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    anameiRandom()
    Grid_background()
    buttonClickToPlay.pack_forget()



window.bind("<Right>",MoveToRight)
window.bind("<Left>",moveToLeft)
window.bind("<Up>",moveUp)
window.bind("<Down>",moveDown)
# Main Code===========================================================
buttonClickToPlay = tk.Button(window,text="Click To Play",font=("Prisa",40),command=button_Click_play)
buttonClickToPlay.pack(expand=True,fill="both")

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()