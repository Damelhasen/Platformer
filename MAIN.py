import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import random
import time
app = Ursina()
camera.orthographic = True
camera.fov = 10
lives = 3

   

platform = Entity(model='quad', y = 2, scale_x = 12 , collider = 'box' , color = color.rgba(0.89, 0.52, 1, 1), x = 4 )
input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

###################################Map Loading########################################################################################################################
bg = Entity(model='quad',  scale=(16**2,16**2), color = color.rgba(0.9,0.7,0.04,1) , z=5)
duplicate(bg, x = 50, z = 5 , y = -10)

ground = Entity(model='quad', y = -7 , scale_x = 15, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1), x = -8 )
wall = Entity(model='quad',color = color.rgba(0.89, 0.52, 0.28, 1),scale = (0.5,9), x = 30, y = 0.1, collider = 'box'  )
duplicate(wall, x = -30)

level =  Entity(model='quad', y = 2, scale_x = 12 , collider = 'box' , color = color.rgba(0.89, 0.52, 1, 1), x = -18 )

duplicate(level, x = -20 , y = -2)
duplicate(level, x = -40 , y = 3)
duplicate(level, x = -60 , y = 0)
duplicate(level, x = -80 , y = -1)  
duplicate(level, x = -100 , y = 2)
####################################################################################################################################

player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" , jump_height = 10)
player.y = -3
player.x = -7
camera.add_script(SmoothFollow(target= player, offset=[0,3,-30], speed=3))

def update():
    global lives 
    if player.y < -10:
        lives -= 1
        player.y = -3
        player.x = -7
    if lives <= 0:
        print("Game Over")
        
        quit() 

app.run()

