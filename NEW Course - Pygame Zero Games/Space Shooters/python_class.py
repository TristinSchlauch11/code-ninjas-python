# Happy coding!
import random

WIDTH = 500
HEIGHT = 700

spaceship = Actor("playership1_orange")
spaceship.center = (WIDTH / 2, HEIGHT - 100)

my_bullets = []
enemy_bullets = []
enemies = []

bullet_cooldown = 0
enemy_cooldown = 0

game_over = False
score = 0

def draw():
    if game_over:
        screen.fill((0,0,0))
    else:
        screen.fill((100, 50, 255))
        screen.draw.text("Score: " + str(score), midright = (WIDTH - 25, HEIGHT - 25))
        spaceship.draw()

        for enemy in enemies:
            enemy.draw()

        for bullet in my_bullets:
            bullet.draw()

        for bullet in enemy_bullets:
            bullet.draw()

def update():
    global bullet_cooldown
    global enemy_cooldown
    global game_over
    global score

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

    for enemy in enemies:
        enemy.y += 3

    for bullet in enemy_bullets:
        bullet.y += 10
        if bullet.y > HEIGHT + 50:
            enemy_bullets.remove(bullet)

    for enemy in enemies:
        if enemy_cooldown > 0:
            enemy_cooldown -= 1
        else:
            bullet = Actor("laserblue16")
            bullet.midtop = enemy.midtop
            enemy_bullets.append(bullet)
            enemy_cooldown = 60

    for enemy in enemies:
        bullet_index = enemy.collidelist(my_bullets)
        if bullet_index != -1:
            enemies.remove(enemy)
            del my_bullets[bullet_index]
            score += 1

    if spaceship.collidelist(enemy_bullets) != -1:
        game_over = True

def create_enemy():
    enemy = Actor("enemyblue2")
    enemy.center = (73 + 118*random.randint(0, 3), 100)
    enemies.append(enemy)

clock.schedule_interval(create_enemy, 1.5)
