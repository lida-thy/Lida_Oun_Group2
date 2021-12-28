from os import X_OK
import tkinter as tk
from typing import Text
import winsound
import random
window=tk.Tk()
window.geometry("800x500")
window.resizable(False,False)
frame=tk.Frame()
frame.master.title("Group2_game_VC1")
canvas=tk.Canvas(frame)


# Constants ===================================================================
MOVE_AMEI=10
MOVE_ENEMI=10
WINDOWS_WIDTH=800

BACKGROUND_IMAGE = tk.PhotoImage(file="Image/Background.png")
AMEI_IMAGE = tk.PhotoImage(file="Image/amei.png")
ENNEMI_IMAGE = tk.PhotoImage(file="Image/anamei.png")
bulet_game=tk.PhotoImage(file="Image/Bullet-1.png")
backGround_infront=tk.PhotoImage(file="Image/Background_Screen.png")
WIN_IMAGE=tk.PhotoImage(file="Image/WIN_GAME .png")


# Vaiable===================================================================
my_hero = None
my_ennemi=None
my_bulet=None
my_score=None
my_ennemi_position=None
my_bulete_position=None
my_hero_position=None
score=0


#Move ennemi======================================================================================
 
def move(delta_x, delta_y) :
    canvas.move(my_hero, delta_x, delta_y)
    winsound.PlaySound("Sound/move_sound.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
#Move right=======================================================================================
def move_to_right(event):
    move(MOVE_AMEI, 0)

#Move Left========================================================================================
 
def move_to_left(event):
     move(-MOVE_AMEI, 0) 

#Move Down========================================================================================
def move_to_Down(event):
   move(0, MOVE_AMEI) 

#Move Up===========================================================================================
def move_to_Up(event):
   move(0,-MOVE_AMEI)

# Increase score===========================================================================

def score_increase(bulet,ennemi):
    global score,to_stop_bullet
    equal_position_x=bulet[0]<=ennemi[0]+25 and bulet[0]>=ennemi[0]-25 
    equal_position_y=bulet[1]<=ennemi[1] and bulet[1]>=ennemi[1]-50
    if equal_position_x and equal_position_y and to_stop_bullet:
        score+=1
        to_stop_bullet=False
        canvas.itemconfig(my_score,text="Score : "+str(score)+"/50")
    elif score==50:
        canvas.create_image(400,250,image=WIN_IMAGE)
# Game Over===========================================================================================
def to_lost():
    global my_hero_position,my_ennemi_position
    equal_hero_x=my_hero_position[0]-25==my_ennemi_position[0]-25
    equal_hero_y=my_hero_position[1]-25==my_ennemi_position[1]-25
    if equal_hero_x==equal_hero_y:
        canvas.delete("all")
        canvas.create_text(400,250,text="lost",font=("Purisa",26))
# #Shooting==========================================================================================
def to_move_bulete(move_to):
    global my_bulet,my_ennemi_position
    canvas.move(move_to,10,0)
    my_bulete_position=canvas.coords(my_bulet)
    score_increase(my_bulete_position,my_ennemi_position)
    canvas.after(15,lambda:to_move_bulete(move_to))
    

def shoot_enamei():
    global my_bulet,my_hero_position
    my_hero_position =canvas.coords(my_hero)
    my_hero_x = my_hero_position[0]
    my_hero_y = my_hero_position[1]
    my_bulet=canvas.create_image(my_hero_x , my_hero_y-20, image=bulet_game,anchor="nw")
    to_move_bulete(my_bulet)


def to_shoot(event):
    global to_stop_bullet
    to_stop_bullet=True
    shoot_enamei()
# to move enemi================================================================================
def move_enamei(moving):
    canvas.move(moving,-MOVE_ENEMI,0)
    canvas.after(200,lambda:move_enamei(moving))
# to random annemi=============================================================================

def to_random_ennemi():
    global my_ennemi_position,my_ennemi
    my_ennemi_x=775
    my_ennemi_y=random.randrange(100,475)
    my_ennemi=canvas.create_image(my_ennemi_x,my_ennemi_y,image=ENNEMI_IMAGE,tags="delete")
    my_ennemi_position=canvas.coords(my_ennemi)
    move_enamei(my_ennemi)
    # canvas.after(50000,lambda:canvas.delete(my_ennemi))
    canvas.after(2000,lambda:to_random_ennemi())

# button to click==============================================================================
def button_Click_play():
    global my_hero,my_ennemi,my_score,score

    # create background 
    canvas.create_image(400,250,image=BACKGROUND_IMAGE)

    # create my hero
    my_hero=canvas.create_image(100,100,image=AMEI_IMAGE)
   
    # create enemi
    to_random_ennemi()
    my_score=canvas.create_text(70,20,text="Score : "+str(score)+"/50",font=("Purisa",15),fill="red",tags="remove_old_score")
# Text to demo player====================================
def to_demo():
    canvas.create_image(400,250,image=backGround_infront)
    canvas.create_text(400,250,text="Prest key ( Left, Right, Up and Down ) to move player and key <b> to shoot",font=("Purisa",15),fill="#fff")
    canvas.after(3000,lambda:canvas.delete("all"))
    canvas.after(3000,lambda:button_Click_play())
    buttonClickToPlay.place_forget()

   
 



#Main code==================================================================
canvas.create_image(400,250,image=backGround_infront)
canvas.create_text(400,250,text="WELCOME TO OUR GAME",font=("Purisa",30),fill="pink")

window.bind("<Right>",move_to_right)
window.bind("<Left>",move_to_left)
window.bind("<Down>",move_to_Down)
window.bind("<Up>",move_to_Up)
window.bind("<b>",to_shoot)
buttonClickToPlay =tk.Button(window, text="Start Game",fg="red",font=("",20),width=10, height=1, bd="10", command=to_demo, background="blue")
buttonClickToPlay.place(x=320, y=400)
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
