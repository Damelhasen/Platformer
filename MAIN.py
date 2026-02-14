import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina()
camera.orthographic = True
camera.fov = 15

bg = Entity(model='quad',  scale=(16,9), texture= "assets/bg1.png", z=5)
bg_2 = Entity(model='quad',  scale=(16,9), texture= "assets/bg2.png", z=20,x = 15 )
ground = Entity(model='quad', y = -4 , scale_x = 30 , collider = 'box' , color = color.rgba(0.89, 0.52, 0.5, 1))
wall = Entity(model='quad',color = color.rgba(0.89, 0.52, 0.28, 1),scale = (0.5,9), x = 30, y = 0.1, collider = 'box'  )
duplicate(wall, x = 30 )

player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" )
camera.add_script(SmoothFollow(target= player, offset=[0,5,-30], speed=4))






app.run()

