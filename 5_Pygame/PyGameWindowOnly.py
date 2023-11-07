# 템플릿
# 윈도우만 존재

# 1. 패키지 불러우기
import pygame
from pygame.locals import *
import sys

# 2. 상수 정의하기
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3. Initialize
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4. Load assets: image, sound, etc

# 5. Initialize variables

# 6. Loop forever
while True:
    # 7. Check for and handle events
    for event in pygame.event.get():
        # 닫힘 버튼 클릭 시 파이게임 프로그램 종료하기
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. '프레임당' 처리해야 할 일 정의하기

    # 9. 윈도우 클리어 하기
    window.fill(BLACK)

    # 10. 윈도우 내 내용물 그리기

    # 11. 윈도우 갱신
    pygame.display.update()

    # 12. 윈도우 갱신 주기 늦추기
    clock.tick(FRAMES_PER_SECOND)