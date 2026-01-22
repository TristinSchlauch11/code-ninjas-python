# screen dimensions
WIDTH = 1000
HEIGHT = 500

# game variables

on_ground = True
clicked = False

gravity = 1
velocity = 0

player = Actor("cone_straight")
player.bottomleft = (200, 350)

spikes = []

for i in range(900, 1050, 50):
    spike = Actor("cone_down")
    spike.bottomleft = (i, 350)
    spikes.append(spike)

def draw():
    screen.fill((20, 50, 255))
    player.draw()
    for spike in spikes:
        spike.draw()

def update():
    global velocity
    global on_ground

    # player movement
    if (keyboard.space or clicked) and on_ground:
        velocity = -15
        on_ground = False
    else:
        velocity += gravity

    player.y += velocity

    # check if player is on ground
    if player.bottom > 350:
        player.bottom = 350
        velocity = 0
        on_ground = True

    # move all other stuff
    for spike in spikes:
        spike.x -= 10
        if spike.right < 0:
            spike.x = 1000

def on_mouse_down(button):
    global clicked
    if button == mouse.LEFT:
        clicked = True

def on_mouse_up(button):
    global clicked
    if button == mouse.LEFT:
        clicked = False
