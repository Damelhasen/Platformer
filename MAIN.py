import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina()
camera.orthographic = True
camera.fov = 10

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')

bg = Entity(model='quad',  scale=(200,21), color = color.rgba(0.9,0.7,0.04,1) , z=5)
bg_2 = Entity(model='quad',  scale=(200,21), z=20,x = 16 )
ground = Entity(model='quad', y = -7 , scale_x = 30, collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 0), x = -8 )
wall = Entity(model='quad',color = color.rgba(0.89, 0.52, 0.28, 1),scale = (0.5,9), x = 30, y = 0.1, collider = 'box'  )
duplicate(wall, x = 30 )

level =  Entity(model='quad', y = -6, scale_x = 12 , collider = 'box' , color = color.rgba(0.89, 0.52, 1, 1), x = 8 )
duplicate(level, x = 8 )
duplicate(level, x = 8 )
player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" , jump_height = 2)
camera.add_script(SmoothFollow(target= player, offset=[0,3,-30], speed=4))






app.run()

