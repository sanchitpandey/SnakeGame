import pygame
import time
import random


init = pygame.init()

if init[1] != 0:
    print("Initialization Error!")
    exit()


def Main():
    # Variables
    width = 800
    height = 600
    playing = True
    gameSurface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game!!')
    clock = pygame.time.Clock()
    score = 0
    snakePos = [int(width / 2) - 10, height - 20]
    snakeBody = [snakePos, [int(width / 2) - 10, height - 10]]
    food = [random.randrange(1, width / 10) * 10,
            random.randrange(1, height / 10) * 10]
    foodSpawn = True
    direction = "UP"
    changeTo = direction

    # Functions

    def scoreBoard(go=0):
        sfont = pygame.font.SysFont('monaco', 35)
        ssurf = pygame.font.Font.render(
            sfont, 'Score: {0}'.format(score), 1, black)
        srect = ssurf.get_rect()
        if go == 1:
            srect.midtop = (int(width / 2), int(height / 2))
        else:
            srect.midtop = (60, 20)
        gameSurface.blit(ssurf, srect)
        pygame.display.flip()

    def gameOver():
        GOfont = pygame.font.SysFont('monaco', 72)
        GOsurf = pygame.font.Font.render(GOfont, 'GAME-OVER!', 1, red)
        GOrect = GOsurf.get_rect()
        GOrect.midtop = (int(width / 2), int(height / 3))
        gameSurface.blit(GOsurf, GOrect)
        scoreBoard(1)
        pygame.display.flip()
        time.sleep(4)
        # pygame.quit()
        # exit()
        Main()

    # Color Variables
    '''(r, g, b)'''
    white = pygame.color.Color(255, 255, 255)
    red = pygame.color.Color(255, 0, 0)
    black = pygame.color.Color(0, 0, 0)
    green = pygame.color.Color(0, 255, 0)
    blue = pygame.color.Color(0, 0, 255)

    # Game Loop

    while playing:
        # SNAKE MECHANICS
        if snakePos[0] == food[0] and snakePos[1] == food[1]:
            score += 10
            foodSpawn = False
        elif snakePos[0] <= 0 or snakePos[0] >= width:
            gameOver()
        elif snakePos[1] <= 0 or snakePos[1] >= height:
            gameOver()
        else:
            del(snakeBody[-1])

        # SNAKE MOVEMENT
        if direction == "UP":
            snakePos = [snakePos[0], snakePos[1] - 10]
            snakeBody.insert(0, snakePos)
        elif direction == "DOWN":
            snakePos = [snakePos[0], snakePos[1] + 10]
            snakeBody.insert(0, snakePos)
        elif direction == "LEFT":
            snakePos = [snakePos[0] - 10, snakePos[1]]
            snakeBody.insert(0, snakePos)
        elif direction == "RIGHT":
            snakePos = [snakePos[0] + 10, snakePos[1]]
            snakeBody.insert(0, snakePos)

        # EVENTS
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # KEYPRESS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and event.key != pygame.K_DOWN:
                    changeTo = "UP"
                elif event.key == pygame.K_DOWN and event.key != pygame.K_UP:
                    changeTo = "DOWN"
                elif event.key == pygame.K_LEFT:
                    changeTo = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    changeTo = "RIGHT"

        direction = changeTo
        gameSurface.fill(white)

        # DRAW SNAKE
        for Block in snakeBody:
            body = pygame.Rect((Block[0], Block[1]), (10, 10))
            pygame.draw.rect(gameSurface, green, body)

        # DRAW FOOD
        foodRect = pygame.Rect((food[0], food[1]), (10, 10))
        pygame.draw.rect(gameSurface, blue, foodRect)

        scoreBoard()

        if not foodSpawn:
            food = [random.randrange(1, width / 10) *
                    10, random.randrange(1, height / 10) * 10]
            foodSpawn = True

        pygame.display.flip()
        clock.tick(25)
    Main()


Main()
