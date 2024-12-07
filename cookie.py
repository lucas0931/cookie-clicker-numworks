from math import *
from time import *
from kandinsky import *
from ion import *

menu = 0
click = 22
click_interval = 0.2
Auto_clic = 0.1

def show_score():  
    draw_string("click: "+str(click), 10, 10)

def show_auto_click():
    draw_string("Auto_clic:"+str(Auto_clic),10,30)

def menu_button():
    draw_string("Auto_clic:"+str(Auto_clic),10,30)

def sup():
    fill_rect(1, 1, 320, 240, "white")  # Efface l'écran

while True:
    if menu == 0:
        draw_string("[1]-clicker", 100, 50)
        draw_string("[2]-stats", 100, 70)
        draw_string("[3]-quit", 100, 90)

        if keydown(KEY_ONE):  # Pas besoin de "== True", `keydown` renvoie déjà un booléen
            menu = 1
            sup()
        elif keydown(KEY_TWO):
            menu = 2
            sup()
        elif keydown(KEY_THREE):
            break
    
    if menu == 1:
        show_auto_click()
        show_score()
        if keydown(KEY_EXE)==True:
            click= click+1
            sleep(click_interval)
            

    
