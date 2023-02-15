import pygame, sys, random
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

# star를 초기화합니다.
star_rect = star.get_rect();
star_rect.x = 128
star_rect.y = 0
star_speed = 5

# player를 초기화 합니다.
player_rect = player.get_rect();
player_rect.x = 320
player_rect.y = 352
player_speed = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    
    star_rect = star_rect.move(0, star_speed)
    '''star_rect의 y좌표가 창 밖을 벗어났다면, 초기화 하는 코드를 작성하세요.'''
    '''1. y 좌표는 -128로 설정하세요.'''
    '''2. x 좌표는 random.randrange( )를 이용해서 임의의 한 좌표로 설정하세요.'''
    
    
    if keys[pygame.K_RIGHT]:
        player_rect = player_rect.move(player_speed, 0)
    elif keys[pygame.K_LEFT]:
        player_rect = player_rect.move(-player_speed, 0)
    
    '''player_rect가 창 안에 있도록 이동범위를 제한하는 코드를 작성하세요.'''
    
    
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(star, star_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)