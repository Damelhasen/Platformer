import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import random
import time
app = Ursina()
camera.orthographic = True
camera.fov = 100
lives = 3

   

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

platform1 = Entity(model='quad', y = -4 , scale_x = 3, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1), x = 3 )
platform2 = Entity(model='quad', y = 0 , scale_x = 3, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1), x = 4 )
platform3 = Entity(model='quad', y = 3 , scale_x = 3, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1), x = -2 )
duplicate(platform1, random.randint(10,20), x = random.randint(10,20) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(10,20) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(10,20) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(20,30) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(20,30) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(20,30) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(30,40) , y = random.randint(10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(30,40) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(30,40) , y = random.randint(-10,10))
duplicate(platform1, random.randint(10,20), x = random.randint(50,60) , y = random.randint(-10,10))



####################################################################################################################################

player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" , jump_height = 10)
player.y = -3
player.x = -7
camera.add_script(SmoothFollow(target= player, offset=[0,3,-30], speed=3))

def update():
    platform1.animate('x', platform1.x + 5, duration=2, curve=curve.in_out_quad)

    global lives
 
    if player.y < -10:
        lives -= 1
        player.y = -3
        player.x = -7
    if lives <= 0:
        print("Game Over")
        
        quit() 

app.run()

