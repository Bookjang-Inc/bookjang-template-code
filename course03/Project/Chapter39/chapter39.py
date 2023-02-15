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

# player를 초기화합니다.
player_rect = player.get_rect();
player_rect.x = 320
player_rect.y = 352
player_speed = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    
    # star Update
    star_rect = star_rect.move(0, star_speed)
    if star_rect.y >= height:
        star_rect.y = -128
        star_rect.x = random.randrange(0, 640 - star_rect.width)
    
    # player Update
    if keys[pygame.K_RIGHT]:
        player_rect = player_rect.move(player_speed, 0)
    elif keys[pygame.K_LEFT]:
        player_rect = player_rect.move(-player_speed, 0)
    
    if player_rect.x < 0:
        player_rect.x = 0
    elif player_rect.x > width - player_rect.width:
        player_rect.x = width - player_rect.width
    
    # pygame.Rect.colliderect(A, B): A와 B가 겹쳐있으면 True를 반환합니다..
    '''player_rect와 star_rect가 겹쳐있다면 프로그램을 종료하도록 코드를 작성하세요.'''
    
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(star, star_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)