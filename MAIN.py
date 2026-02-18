import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import random
import time
app = Ursina()
camera.orthographic = True


camera.fov = 30
lives = 100

def platform_generator():

    p1 = duplicate(platform1, random.randint(10,20), x = random.randint(4,8) , y = random.randint(-10,10))
    p1.animate_x(p1.x + 8, duration=2, curve=curve.in_out_quad, loop=True)
    p2 = duplicate(platform1, random.randint(10,20), x = random.randint(8,12) , y = random.randint(-10,10))
    p3 = duplicate(platform1, random.randint(10,20), x = random.randint(12,16) , y = random.randint(-10,10))
    p3.animate_x(p1.x + 8, duration=2, curve=curve.in_out_quad, loop=True)
    p4 = duplicate(platform1, random.randint(10,20), x = random.randint(16,20) , y = random.randint(-10,10))
    p4.animate_x(p1.x + 8, duration=2, curve=curve.in_out_quad, loop=True)

    p5 =duplicate(platform1, random.randint(10,20), x = random.randint(20,24) , y = random.randint(-10,10))
    p6 = duplicate(platform1, random.randint(10,20), x = random.randint(28,32) , y = random.randint(-10,10))
    p7 = duplicate(platform1, random.randint(10,20), x = random.randint(36,40) , y = random.randint(10,10))
    p8 = duplicate(platform1, random.randint(10,20), x = random.randint(44,48) , y = random.randint(-10,10))
    p8.animate_x(p1.x + 8, duration=2, curve=curve.in_out_quad, loop=True)

    p9 =duplicate(platform1, random.randint(10,20), x = random.randint(52,56) , y = random.randint(-10,10))
    p12 = duplicate(platform1, random.randint(10,20), x = random.randint(60,64) , y = random.randint(-10,10))
def contact(obj1 :str , obj2:str):
    if abs(obj1.x - obj2.x) < 0.5 and abs(obj1.y - obj2.y) < 0.5 :
        return True
    else :
        return False
    
    
powerup = Entity(model='quad', scale=(1,1), color=color.rgba(0.04,0.7,0.9,1), collider = False , x = -2 , y = 2 ,texture= "assets/fruit.png",)

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')
input_handler.bind('gamepad left stick right', 'd')
input_handler.bind('gamepad left stick left', 'a')


###################################Map Loading########################################################################################################################
bg = Entity(model='quad',  scale=(16**2,16**2), color = color.rgba(0.9,0.7,0.04,1) , z=5)
duplicate(bg, x = 50, z = 5 , y = -10)

ground = Entity(model='quad', y = -7 , scale_x = 15, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1), x = -8 )

platform1 = Entity(model='quad', scale=(1,1), collider='box', color=color.rgba(0.89, 0.52, 0.5, 1) , scale_x = 4)

platform_generator()




####################################################################################################################################

player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" , jump_height = 10)
player.y = -3
player.x = -7
camera.add_script(SmoothFollow(target= player, offset=[0,3,-30], speed= 4))

def update():
    
    global lives
    
    if player.y < -10:
        lives -= 1
        player.y = -3
        player.x = -7
    if lives <= 0:
        print("Game Over")
        
        quit() 
    if contact(player,powerup) == True :
        print("HIT")
        powerup.y = -1000
        player.jump_height = 15
    
    
    
   
app.run()

