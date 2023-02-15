import pygame, sys

# 모듈을 초기화 합니다.
pygame.init()

# 창을 생성합니다.
width, height = 640, 480
screen = pygame.display.set_mode(size=(width, height))

# pygame.image.load(): 경로에 있는 파일을 불러올 수 있습니다.
# [예]
# background = pygame.image.load('background.png') # 'background.png' 사진을 불러옵니다.
'''게임에 필요한 사진들을 가져오세요.'''


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # screen.blit( ): 화면에 그림을 그릴 수 있습니다.
    # [예]
    # screen.blit(background, (0, 0)) # (0, 0) 위치에 background 이미지를 출력합니다.
    '''가져온 사진들을 전부 그리세요.'''
    
    
    # pygame.display.flip( ): 지금까지 그린 그림을 창에 띄웁니다. 
    pygame.display.flip()