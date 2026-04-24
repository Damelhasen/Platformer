from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
import random
import math
import time

app = Ursina()
camera.orthographic = True
camera.fov = 30
lives = 100

oscillating_platforms = []  # (entity, start_x, start_y, x_dist, y_dist, x_speed, y_speed)

def platform_generator():
    positions = [
        # (x, y, x_moves, y_moves)
        (random.randint(4,8),   random.randint(-4,4), True,  False),
        (random.randint(8,12),  random.randint(-4,4), False, False),
        (random.randint(12,16), random.randint(-4,4), True,  True),
        (random.randint(16,20), random.randint(-4,4), True,  False),
        (random.randint(20,24), random.randint(-4,4), False, True),
        (random.randint(28,32), random.randint(-4,4), False, False),
        (random.randint(36,40), random.randint(-4,4), False, True),
        (random.randint(44,48), random.randint(-4,4), True,  True),
        (random.randint(52,56), random.randint(-4,4), False, False),
        (random.randint(60,64), random.randint(-4,4), False, False),
    ]
    for px, py, x_moves, y_moves in positions:
        p = duplicate(platform1, x=px, y=py)
        x_dist = 4 if x_moves else 0
        y_dist = 2 if y_moves else 0
        x_speed = random.uniform(0.8, 1.5)
        y_speed = random.uniform(0.8, 1.5)
        oscillating_platforms.append((p, px, py, x_dist, y_dist, x_speed, y_speed))

def contact(obj1, obj2, x_thresh=1, y_thresh=1):
    return abs(obj1.x - obj2.x) < x_thresh and abs(obj1.y - obj2.y) < y_thresh

def game_over(message):
    Text(message, origin=(0, 0), scale=3, color=color.white)
    player.enabled = False
    invoke(quit, delay=3)

# Input bindings
input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')
input_handler.bind('gamepad left stick right', 'd')
input_handler.bind('gamepad left stick left', 'a')

# Map
bg = Entity(model='quad', scale=(16**2, 16**2), color=color.rgba(0.9, 0.7, 0.04, 1), z=5)
duplicate(bg, x=50, z=5, y=-10)

ground = Entity(model='quad', y=-7, scale_x=15, collider='box', color=color.rgba(0.89, 0.52, 0.5, 1), x=-8)

platform1 = Entity(model='quad', scale=(4, 1), collider='box', color=color.rgba(0.89, 0.52, 0.5, 1), x=-9999)

platform_generator()

endplatform = Entity(model='quad', scale=(4, 1), collider='box', color=color.rgba(0.04, 0.7, 0.9, 1), x=64, y=-3)

# Powerup
powerup = Entity(
    model='quad', scale=(1, 1),
    color=color.rgba(0.04, 0.7, 0.9, 1),
    collider=None,
    x=-2, y=2,
    texture="assets/fruit.png"
)

# Player
player = PlatformerController2d(
    y=-3, scale=(2, 2, 0),
    color=color.white,
    texture="assets/sprite.png",
    jump_height=10
)
player.x = -7
camera.add_script(SmoothFollow(target=player, offset=[0, 3, -30], speed=4))

def update():
    global lives

    for p, start_x, start_y, x_dist, y_dist, x_speed, y_speed in oscillating_platforms:
        p.x = start_x + math.sin(time.time() * x_speed) * x_dist
        p.y = start_y + math.sin(time.time() * y_speed) * y_dist

    if player.y < -10:
        lives -= 1
        player.y = -3
        player.x = -7

    if lives <= 0:
        game_over("Game Over!")

    if contact(player, powerup):
        print("HIT")
        powerup.y = -1000
        player.jump_height = 15

    if contact(player, endplatform, x_thresh=3, y_thresh=1.5):
        game_over("You Win!")

app.run()