import random

WIDTH = 800
HEIGHT = 600

# game variables
lives = 3
level = 1
score = 0

ball_moving = False
ball_vx = 0
ball_vy = 0

# game objects
paddle = Actor("paddle")
paddle.center = (300, 500)

ball = Actor("ball")
ball.center = (300, 470)

life_balls = []
for x in range(625, 750, 25):
    life_ball = Actor("ball")
    life_ball.center = (x, 425)
    life_balls.append(life_ball)

bricks = []
power_ups = []

def draw():
    # background
    screen.fill((200, 200, 255))
    screen.draw.filled_rect(Rect((50, 50), (500, 500)), (50, 50, 50))
    screen.draw.filled_rect(Rect((600, 150), (150, 300)), (50, 50, 50))

    # text
    screen.draw.text("Level", center = (675, 185), fontsize = 36, color = (255, 255, 255))
    screen.draw.text(str(level), center = (675, 225), fontsize = 36, color = (255, 255, 255))
    screen.draw.text("Score", center = (675, 285), fontsize = 36, color = (255, 255, 255))
    screen.draw.text(str(score), center = (675, 325), fontsize = 36, color = (255, 255, 255))
    screen.draw.text("Lives", center = (675, 385), fontsize = 36, color = (255, 255, 255))
    if lives <= 6:
        for i in range(lives - 1):
            life_balls[i].draw()
    else:
        life_balls[1].draw()
        screen.draw.text("x " + str(lives - 1), midleft = (670, 425), fontsize = 32, color = (255, 255, 255))

    # game over screen
    if lives == 0:
        screen.draw.text("GAME OVER", center = (300, 300), fontsize = 48, color = (255, 255, 255))
    else:
        # game objects
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()
        for power in power_ups:
            power.draw()

def update():
    global ball_moving
    global ball_vx
    global ball_vy
    global lives
    global score
    global level

    # handle events
    if keyboard.a or keyboard.left:
        if paddle.left > 60:
            paddle.x -= 5
            if not ball_moving:
                ball.x -= 5
    if keyboard.d or keyboard.right:
        if paddle.right < 540:
            paddle.x += 5
            if not ball_moving:
                ball.x += 5
    if keyboard.space and not ball_moving:
        ball_moving = True
        ball_vx = 1
        ball_vy = -2 - level*0.5

    # move ball
    ball.x += ball_vx
    ball.y += ball_vy

    # change ball directions if needed
    if ball.right >= 550:
        ball_vx = -abs(ball_vx)
    if ball.left <= 50:
        ball_vx = abs(ball_vx)
    if ball.top <= 50:
        ball_vy = abs(ball_vy)

    # move power ups
    for power in power_ups:
        power.y += 5
        if power.bottom >= 550:
            power_ups.remove(power)

    # check if ball hit a brick
    brick_index = ball.collidelist(bricks)
    if brick_index != -1:
        # get the brick info and update score
        brick = bricks[brick_index]
        score += level

        # change direction of ball
        if (abs(brick.top - ball.bottom) < 5 and ball_vy > 0) or (abs(brick.bottom - ball.top) < 5 and ball_vy < 0):
            ball_vy = -ball_vy
        if (abs(brick.left - ball.right) < 5 and ball_vx > 0) or (abs(brick.right - ball.left) < 5 and ball_vx < 0):
            ball_vx = -ball_vx

        # chance to spawn power up
        if random.randint(1, 10) == 1:
            sel = random.choice(["extra_life", "size_up", "widen"])
            power = Actor(sel)
            power.center = brick.center
            power_ups.append(power)

        # delete the brick
        del bricks[brick_index]

    # check if ball hit the paddle
    if ball.colliderect(paddle):
        ball_vy = -abs(ball_vy)
        if keyboard.right:
            ball_vx = min(ball_vx + 3, 5)
        if keyboard.left:
            ball_vx = max(ball_vx - 3, -5)

    # check if player collected a power up
    power_index = paddle.collidelist(power_ups)
    if power_index != -1:
        # get the power up to determine which one was collected
        power = power_ups[power_index]

        # gain a life
        if power.image == "extra_life":
            lives += 1

        # temporarily make the ball big
        if power.image == "size_up":
            ball.image = "ball_big"
            clock.schedule_unique(shrink_ball, 10.0)

        # temporarily make the paddle big
        if power.image == "widen":
            paddle.image = "paddle_big"
            clock.schedule_unique(shrink_paddle, 10.0)

        # destroy the power up
        del power_ups[power_index]

    # check if the player missed the ball
    if ball.bottom >= 550:
        lives -= 1
        reset_ball()

    # check if all bricks have been cleared
    if len(bricks) == 0:
        level += 1
        reset_ball()
        create_bricks()

def create_bricks():
    global bricks

    for y in range(60, 140, 20):
        for x in range(60, 540, 35):
            brick = Actor("brick")
            brick.topleft = (x, y)
            bricks.append(brick)

    for y in range(160, 240, 20):
        for x in range(60, 540, 70):
            brick = Actor("brick_big")
            brick.topleft = (x, y)
            bricks.append(brick)

def reset_ball():
    global ball_moving
    global ball_vx
    global ball_vy

    # remove all power ups
    shrink_ball()
    shrink_paddle()

    # if no lives left, don't let player start level again
    if lives > 0:
        ball_moving = False

    ball_vx = 0
    ball_vy = 0
    ball.y = 470
    ball.x = paddle.x

def shrink_ball():
    ball.image = "ball"

def shrink_paddle():
    paddle.image = "paddle"

create_bricks()

