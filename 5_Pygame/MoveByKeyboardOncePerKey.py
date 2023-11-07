# one image, move by keyboard

# 1. 패키지 불러우기
import pygame
from pygame.locals import *
import sys
import random

# 2. 상수 정의하기
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3. Initialize
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets: image, sound, etc
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')

# 5. Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # 닫힘 버튼 클릭 시 파이게임 프로그램 종료하기
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if the user pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE

    # 8. '프레임당' 처리해야 할 일 정의하기
    # Check if the ball is colliding with the target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    # 9. 윈도우 클리어 하기
    window.fill(BLACK)

    # 10. 윈도우 내 내용물 그리기
    window.blit(targetImage, (TARGET_X, TARGET_Y))  # draw the target
    window.blit(ballImage, (ballX, ballY))  # draw the ball

    # 11. 윈도우 갱신
    pygame.display.update()

    # 12. 윈도우 갱신 주기 늦추기
    clock.tick(FRAMES_PER_SECOND)
