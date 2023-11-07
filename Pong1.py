import pygame
import random
import math

# start pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# set caption and icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('pong.png')
pygame.display.set_icon(icon)

# Colours to be used later
white = (255, 255, 255)


# Paddle
# function to create_paddle
def create_paddle(surface, x, y, w, h, color):
    paddle_global = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, paddle_global)
    return paddle_global


paddleX = 370
paddleY = 480
paddleX_change = 0


# Ball
def create_ball(surface, x, y, w, h, color):
    ball_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, ball_rect)
    return ball_rect

#ball starting point
ballX = 385
ballY = 100

# ballX = random.randint(0, 770)
# ballY = random.randint(0, 120)


#ball trajectory (need to set a max speed)
ballY_change = random.randint(300, 500)
ballX_change = random.randint(-400, 400)
ballY_change: ballX_change < 0.8

# Game Over Font
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Game Over text
def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 20)
def score_text():
    show_score = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(show_score, (10, 20))

running = True

while running:
    screen.fill((0, 0, 0))

    score_text()

    for event in pygame.event.get():
        # Exit Game
        if event.type == pygame.QUIT:
            running = False

        # Paddle Movement KEYS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddleX_change = -0.5
            if event.key == pygame.K_RIGHT:
                paddleX_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddleX_change = 0

    # Paddle Boundaries
    if paddleX >= 740:
        paddleX = 740
    if paddleX <= 0:
        paddleX = 0

    # Is Paddle still moving?
    paddleX += paddleX_change

    # Ball Movement
    ballY += ballY_change/2000
    ballX += ballX_change/2000

    # Ball Boundaries
    if ballX >= 770:
        ballX_change = ballX_change-(2*ballX_change)
    if ballX <= 0:
        ballX_change = ballX_change - (2 * ballX_change)
    if ballY <= 0:
        ballY_change = ballY_change - (2 * ballY_change)
    # Game Over
    if ballY >= 600:
        game_over_text()

    # Create new instance of paddle
    paddle = create_paddle(screen, paddleX, paddleY, 60, 10, white)
    # Create new instance of ball
    ball = create_ball(screen, ballX, ballY, 30, 30, white)

    # Ball / Paddle Collision
    if ball.colliderect(paddle):
        # if paddleX <= ballX - 30 <= paddleX + 60:
        #     ballY_change = ballY_change - (2 * ballY_change)
        #     score = score + 1

        # collision with the top of the paddle
        if paddleX - 30 <= ballX <= paddleX + 60 and ballY <= paddleY + 30:
            ballY_change = ballY_change - (2 * ballY_change)
            score += 1
        else:
            pass





        # if i <= 20:
        #     ballX_change = -0.2
        # elif i <= 40:
        #     ballX_change = -0.1
        # elif i <= 50:
        #     ballX_change = 0
        # elif i <= 70:
        #     ballX_change = 0.1
        # elif i <= 90:
        #     ballX_change = 0.2


        # if ballX < paddleX < ballX and (ballY + 30) > paddleY:
        #     ballY_change = ballY_change - (2 * ballY_change)
        #     ballX_change = ballX_change - (2 * ballX_change)
        #     score = score + 1

    pygame.display.update()
