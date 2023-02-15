import pygame, sys
import time

# 모듈을 초기화합니다.
pygame.init()

# 창을 생성합니다.
width, height = 640, 480
screen = pygame.display.set_mode(size=(width, height))

# 게임 제작에 필요한 사진들을 불러옵니다.
background = pygame.image.load('Background.png')
player = pygame.image.load('Player.png')
star = pygame.image.load('Star.png')

# image.get_rect(): image의 정보(rect)를 구할 수 있습니다.
# [예]
# star_rect = star.get_rect() #star 이미지의 rect를 구합니다
'''star와 player의 rect를 구하고, x와 y값을 수정해 보세요.'''
# Star
star_rect = 


star_speed =5

# Player
player_rect = 


player_speed = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # pygame.key.get_pressed( ): 현재 눌려있는 키를 구할 수 있습니다.
    '''현재 눌려있는 키를 구하는 코드를 완성해 보세요.'''
    keys = pygame.key.()
    
    # rect.move(): 현재 위치에서 입력받은 값 만큼 이동합니다.
    # [예]
    # star_rect = star_rect.move(0, 1) # star_rect의 현재 위치에서 0, 1만큼 이동합니다.
    '''star가 계속 아래로 이동하도록 코드를 작성하세요.'''
    
    
    #pygame.K_RIGHT: 오른쪽 방향키를 의미합니다.
    #pygame.K_LEFT: 왼쪽 방향키를 의미합니다.
    '''1. 오른쪽 방향키가 눌리면, player가 오른쪽으로 이동하는 코드를 작성하세요.'''
    '''2. 왼쪽 방향키가 눌리면, player가 왼쪽으로 이동하는 코드를 작성하세요.'''
    if keys[]:
        
    elif keys[]:
        
    
    '''(0, 0)과 같은 좌표가 아닌, rect를 넣어보세요.'''
    screen.blit(background, (0, 0))
    screen.blit(player, (0, 0))
    screen.blit(star, (128, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(60)