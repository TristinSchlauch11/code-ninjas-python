# screen dimensions
WIDTH = 1000
HEIGHT = 500

# game variables
on_ground = True
clicked = False
x_offset = 0
form = "block"

# physics variables
gravity = 1
velocity = 0

# sprites
bg = Actor("background")
bg.bottomleft = (0, 500)

player = Actor("player")
player.bottomleft = (200, 350)

# spike and platform sprites
def create_obst(pos_list, image, can_land):
    for (col, row) in pos_list:
        # create the sprite and set its position
        sprite = Actor(image)
        sprite.left = 700 + 45*col
        sprite.bottom = 350 - 45*row
        # add it to the neccesary lists
        all_obst.append(sprite)
        if can_land:
            platforms.append(sprite)

platforms = []
all_obst = []

block_coords = [(1,0), (7,2), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4)]
create_obst(block_coords, "block", True)

spike_coords = [(2,0), (3,0), (10,0), (11,0)]
create_obst(spike_coords, "spike", False)

# ring sprites
def create_ring(pos_list, ring):
    for (col, row) in pos_list:
        # create the sprite and set its position
        sprite = Actor(ring)
        sprite.left = 700 + 45*col
        sprite.bottom = 350 - 45*row
        # add it to the neccesary lists
        rings.append(sprite)

rings = []

up_coord = [(15, 0)]
create_ring(up_coord, "up_ring")

down_coord = [(21, 2)]
create_ring(down_coord, "down_ring")

def draw():
    bg.draw()
    player.draw()

    for obst in all_obst:
        obst.draw()

    for ring in rings:
        ring.draw()

def update():
    global velocity
    global x_offset
    global on_ground

    # player movement
    if form == "block":
        if (keyboard.space or clicked) and on_ground:
            velocity = -15*gravity
        elif velocity < 25 and velocity > -25:
            velocity += gravity
        on_ground = False       # to prevent mid-air jumps
    #testing!!
    elif form == "rocket":
        if keyboard.space or clicked:
            velocity += -1*gravity
        else:
            velocity += gravity

    player.y += velocity

    # check if player is on the floor
    if player.bottom > 350:
        player.bottom = 350
        velocity = 0
        on_ground = True

    # check for collision with obstacles
    o_index = player.collidelist(all_obst)
    if o_index != -1:
        # check what we hit
        obstacle = all_obst[o_index]
        if obstacle in platforms:
            # check if we have landed on a square
            if gravity == 1:
                if player.bottom < obstacle.top + 25:
                    player.bottom = obstacle.top
                    velocity = 0
                    on_ground = True
                # we have hit a square
                else:
                    reset_all_obst()
            else:
                if player.top > obstacle.bottom - 25:
                    player.top = obstacle.bottom
                    velocity = 0
                    on_ground = True
                # we have hit a square
                else:
                    reset_all_obst()
        # we have hit something else
        else:
            reset_all_obst()

    # check for collision with rings
    ring_index = player.collidelist(rings)
    if ring_index != -1:
        ring = rings[ring_index]
        pass_ring(ring)

    # move all other stuff
    x_offset += 10
    for obst in all_obst:
        obst.x -= 10
    for ring in rings:
        ring.x -= 10

def on_mouse_down(button):
    global clicked
    if button == mouse.LEFT:
        clicked = True

def on_mouse_up(button):
    global clicked
    if button == mouse.LEFT:
        clicked = False

def on_key_down(key):
    if key == keys.RETURN:
        reset_all_obst()

def pass_ring(ring):
    global gravity
    global form

    if ring.image == "down_ring":
        gravity = 1
    elif ring.image == "up_ring":
        gravity = -1
    if ring.image == "block_ring":
        player.image = "player"
        form = "block"
    elif ring.image == "rocket_ring":
        form = "rocket"

def reset_all_obst():
    global x_offset
    global form
    global gravity
    global velocity

    # reset all obstacles
    for obst in all_obst:
        obst.x += x_offset
    for ring in rings:
        ring.x += x_offset

    # reset player
    player.form = "block"
    player.bottomleft = (200, 350)
    gravity = 1
    velocity = 0

    # reset offset
    x_offset = 0
