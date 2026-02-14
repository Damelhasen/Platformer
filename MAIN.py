import importlib.util
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
app = Ursina()
camera.orthographic = True
camera.fov = 10

bg = Entity(model='quad',  scale=(16,9), texture= "assets/bg1.png", z=5)
#bg_2 = Entity(model='quad',  scale=(16,9), texture= "assets/bg2.png", z=10, )
ground = Entity(model='quad', y = -4 , scale_x = 12.80 , collider = 'box' , color = color.rgba(0.89, 0.52, 0.28, 1))
wall = Entity(model='quad',color = color.rgba(0.89, 0.52, 0.28, 1),scale = (0.5,9), x = 6.5, y = 0.1, collider = 'box'  )
duplicate(wall, x = -6.5 )

player = PlatformerController2d(y=-3 ,scale = (2,2,0) , color =color.white, texture = "assets/sprite.png" )
camera.add_script(SmoothFollow(target= player, offset=[0,5,-30], speed=4))


level = Entity(model = 'quad', scale = (1,4), collider = 'box', visible = True, z = 4   )

if player.x > 5.5:
    bg.texture = "assets/bg2.png"

def update():
  \
app.run()

