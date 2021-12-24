import tkinter as tk
import winsound
import random
window=tk.Tk()
window.geometry("800x500")
window.resizable(False,False)
frame=tk.Frame()
frame.master.title("Group2_game_VC1")
canvas=tk.Canvas(frame)
# Image======================================================================

background = tk.PhotoImage(file="Image/Background.png")
Hero = tk.PhotoImage(file="Image/amei.png")
annamei = tk.PhotoImage(file="Image/anamei.png")
bulet_game=tk.PhotoImage(file="Image/Bullet-1.png")
backGround_infront=tk.PhotoImage(file="Image/bg_creen.png")
# Vaiable===================================================================
MOVEAMEI=20
# myhero=''
Hero_position=0
X=400
#Player======================================================================================


# Move to right================================================================================
def move_to_right(event):
    global MOVEAMEI,myhero,Hero_position
    Hero_position=canvas.coords(myhero)
    canvas.move(myhero,MOVEAMEI,0)
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
# Move to left=================================================================================
def move_to_left(event):
    global MOVEAMEI,myhero,Hero_position
    Hero_position=canvas.coords(myhero)
    canvas.move(myhero,-MOVEAMEI,0)
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#Move Down====================================================================================
def move_to_Down(event):
    global MOVEAMEI,myhero,Hero_position
    Hero_position=canvas.coords(myhero)
    canvas.move(myhero,0,MOVEAMEI)
    
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#Move Up===========================================================================================
def move_to_Up(event):
    global MOVEAMEI,myhero,Hero_position
    Hero_position=canvas.coords(myhero)
    canvas.move(myhero,0,-MOVEAMEI)
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#Shooting==========================================================================================
def shoot_enamei():
    global X,Hero_position
    Y=Hero_position[1]
    X+=5
    bulete=canvas.create_image(X,Y,image=bulet_game,anchor="nw")
    if X>-150:
        canvas.after(10,lambda:shoot_enamei())
    canvas.after(10,lambda:canvas.delete(bulete))
def to_shoot(event):
    global X , Hero_position
    X=Hero_position[0]
    shoot_enamei()


#Anamei ===========================================================================================
def Anamei_random():
    canvas.delete("delete")
    x=775
    y=random.randrange(25,475)
    canvas.create_image(x,y,image=annamei,tags="delete")
    canvas.after(10000,lambda:Anamei_random())
    print(y,x)
#Display =====================================================================
position_x=35
position_y=400
score=00
def button_Click_play():
    global myhero,gameBul,x,y,bulet,score
    winsound.PlaySound("Sound/sound back.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
    Anamei_random()
    canvas.create_image(400,250,image=background)
    # gameBul=canvas.create_oval(40,400,50,410,fill="red")
    canvas.create_text(70,20,text="Score is : "+str(score),font=("Purisa",20))
    myhero=canvas.create_image(position_x,position_y,image=Hero)
    buttonClickToPlay.place_forget()
#Main code==================================================================
canvas.create_image(400,250,image=backGround_infront)
#Event=====================================================================
window.bind("<Right>",move_to_right)
window.bind("<Left>",move_to_left)
window.bind("<Down>",move_to_Down)
window.bind("<Up>",move_to_Up)
window.bind("<b>",to_shoot)
buttonClickToPlay =tk.Button(window, text="Start Game",width=20, height=3, bd="10", command=button_Click_play, background="brown")
buttonClickToPlay.place(x=320, y=400)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
