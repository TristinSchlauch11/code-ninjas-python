# screen dimensions
WIDTH = 1000
HEIGHT = 500

# game variables
on_ground = True
clicked = False
x_offset = 0

# physics variables
gravity = 1
velocity = 0

# sprites
player = Actor("cone_straight")
player.bottomleft = (200, 350)

spikes = []
squares = []
all_obst = []

for i in range(1100, 1250, 50):
    spike = Actor("cone_down")
    spike.bottomleft = (i, 350)
    spikes.append(spike)
    all_obst.append(spike)

for i in range(700, 900, 50):
    square = Actor("cone_straight")
    square.bottomleft = (i, 350)
    squares.append(square)
    all_obst.append(square)

def draw():
    screen.fill((20, 50, 255))
    player.draw()

    for obst in all_obst:
        obst.draw()

def update():
    global velocity
    global x_offset
    global on_ground

    # player movement
    if (keyboard.space or clicked) and on_ground:
        velocity = -15
    elif velocity < 25:
        velocity += gravity

    on_ground = False
    player.y += velocity

    # check if player is on the floor
    if player.bottom > 350:
        player.bottom = 350
        velocity = 0
        on_ground = True

    # check for collisions
    o_index = player.collidelist(all_obst)
    if o_index != -1:
        # check what we hit
        obstacle = all_obst[o_index]
        if obstacle in squares:
            # check if we have landed on a square
            if player.bottom < square.top + 25:
                player.bottom = square.top
                velocity = 0
                on_ground = True
            # we have hit a square
            else:
                reset_all_obst()
        # we have hit something else
        else:
            reset_all_obst()

    # move all other stuff
    x_offset += 10
    for obst in all_obst:
        obst.x -= 10
        if obst.right < -500:
            reset_all_obst()

def on_mouse_down(button):
    global clicked
    if button == mouse.LEFT:
        clicked = True

def on_mouse_up(button):
    global clicked
    if button == mouse.LEFT:
        clicked = False

def reset_all_obst():
    global x_offset

    # reset all obstacles
    for obst in all_obst:
        obst.x += x_offset

    # reset offset
    x_offset = 0
