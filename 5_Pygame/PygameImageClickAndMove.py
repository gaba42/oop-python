# one image, click and move

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

# 3. Initialize
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets: image, sound, etc
ballImage = pygame.image.load('images/ball.png')

# 5. Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # 닫힘 버튼 클릭 시 파이게임 프로그램 종료하기
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # See if user clicked
    if event.type == pygame.MOUSEBUTTONUP:
        # mouseX, mouseY =event.pos  # 필요하면 이런 것도 가능하다

        # Check if the click was in the rect of the ball
        # if so, choose a random new location
        if ballRect.collidepoint(event.pos):
            ballX = random.randrange(MAX_WIDTH)
            ballY = random.randrange(MAX_HEIGHT)
            ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8. '프레임당' 처리해야 할 일 정의하기

    # 9. 윈도우 클리어 하기
    window.fill(BLACK)

    # 10. 윈도우 내 내용물 그리기
    # Draw the ball at the randomized location
    window.blit(ballImage, (ballX, ballY))

    # 11. 윈도우 갱신
    pygame.display.update()

    # 12. 윈도우 갱신 주기 늦추기
    clock.tick(FRAMES_PER_SECOND)
