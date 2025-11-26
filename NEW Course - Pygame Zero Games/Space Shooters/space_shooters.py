import random

# pygame variables
WIDTH = 500
HEIGHT = 700

# game variables
bullet_cooldown = 0
enemy_cooldown = 0

lives = 3
score = 0
game_over = False

# player spaceship
spaceship = Actor("playership3_red")
spaceship.center = (WIDTH / 2, 600)

# player bullets
my_bullets = []

# enemy spaceships
enemies = []

# enemy bullets
enemy_bullets = []

def draw():
    if game_over:
        screen.fill((30, 0, 70))
        screen.draw.text("Game over", color = (255, 255, 255), center = (WIDTH / 2, HEIGHT / 2 - 25))
        screen.draw.text("Score: " + str(score), color = (255, 255, 255), center = (WIDTH / 2, HEIGHT / 2 + 25))

    else:
        # draw background
        screen.fill((30, 0, 70))

        # draw score and life info
        screen.draw.text("Score: " + str(score), color = (255, 255, 255), midleft = (25, HEIGHT - 25))
        screen.draw.text("Lives: " + str(lives), color = (255, 255, 255), midright = (WIDTH - 25, HEIGHT - 25))

        # draw bullets
        for bullet in my_bullets:
            bullet.draw()

        # draw enemy bullets
        for bullet in enemy_bullets:
            bullet.draw()

        # draw spaceship
        spaceship.draw()

        # draw enemies
        for enemy in enemies:
            enemy.draw()

def update():
    # define global variables
    global bullet_cooldown
    global enemy_cooldown
    global lives
    global score
    global game_over

    # move spaceship
    if keyboard.right and spaceship.right < WIDTH - 25:
        spaceship.x += 5
    if keyboard.left and spaceship.left > 25:
        spaceship.x -= 5

    # move enemy spaceships
    for enemy in enemies:
        if enemy.image in ["meteorgrey_big3", "meteorgrey_big4"]:
            enemy.y += 5
        else:
            enemy.y += 1 + score * 0.05
        if enemy.y >= HEIGHT + 50:
            enemies.remove(enemy)

    # create new bullets
    if bullet_cooldown > 0:
        bullet_cooldown -= 1
    elif keyboard.space and not game_over:
        bullet = Actor("laserblue01")
        bullet.midtop = spaceship.midtop
        my_bullets.append(bullet)
        bullet_cooldown = 10

    # move bullets
    for bullet in my_bullets:
        bullet.y -= 25
        if bullet.y < -50:
            my_bullets.remove(bullet)

    # create new enemy bullets
    if enemy_cooldown > 0:
        enemy_cooldown -= 1
    else:
        for enemy in enemies:
            if enemy.image not in ["meteorgrey_big3", "meteorgrey_big4"]:
                # create default bullet
                bullet = Actor("laserred01")
                # change bullet to green if enemy is green
                if enemy.image == "enemygreen2":
                    bullet.image = "lasergreen11"

                bullet.angle = 180
                bullet.midtop = enemy.midbottom

                enemy_bullets.append(bullet)
        enemy_cooldown = 60

    # move enemy bullets
    for bullet in enemy_bullets:
        if bullet.image == "lasergreen11":
            bullet.y += 5 + score * 0.025
        else:
            bullet.y += 10 + score * 0.05
        if bullet.y >= HEIGHT + 50:
            enemy_bullets.remove(bullet)

    # check if enemy got shot
    for enemy in enemies:
        bullet_index = enemy.collidelist(my_bullets)
        if bullet_index != -1:
            del my_bullets[bullet_index]
            if enemy.image not in ["meteorgrey_big3", "meteorgrey_big4"]:
                score += 1
                enemies.remove(enemy)

    # check if you got shot
    bullet_index = spaceship.collidelist(enemy_bullets)
    if bullet_index != -1:
        lives -= 1
        del enemy_bullets[bullet_index]

        if lives == 0:
            game_over = True
            my_bullets.clear()

    # check if you collided with object
    if spaceship.collidelist(enemies) != -1:
        game_over= True
        my_bullets.clear()

# spawning enemies
def create_enemy():
    enemy = Actor(random.choice(["enemyblack2", "enemyred2", "enemyblue2", "enemygreen2", "meteorgrey_big3", "meteorgrey_big4"]))
    enemy.center = (73 + 118*random.randint(0, 3), 50)
    enemies.append(enemy)

clock.schedule_interval(create_enemy, 1.5)
