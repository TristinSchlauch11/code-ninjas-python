# Happy coding!

WIDTH = 500
HEIGHT = 700

spaceship = Actor("playership1_orange")
spaceship.center = (WIDTH / 2, HEIGHT - 100)

my_bullets = []

bullet_cooldown = 0

def draw():
    screen.fill((100, 50, 255))
    spaceship.draw()

    for bullet in my_bullets:
        bullet.draw()

def update():
    global bullet_cooldown

    if keyboard.a and spaceship.left > 25:
        spaceship.x -= 5
    if keyboard.d and spaceship.right < WIDTH - 25:
        spaceship.x += 5
    if bullet_cooldown > 0:
        bullet_cooldown -= 1
    elif keyboard.space:
        bullet = Actor("laserred16")
        bullet.midtop = spaceship.midtop
        my_bullets.append(bullet)
        bullet_cooldown = 10

    for bullet in my_bullets:
        bullet.y -= 25
        if bullet.y < -50:
            my_bullets.remove(bullet)
