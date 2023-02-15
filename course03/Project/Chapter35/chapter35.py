import pygame, sys

# pygame으로 작업을 수행하려면 먼저 초기화해야 합니다.
# init function을 사용하면 자동으로 초기화를 진행합니다.
'''pygame module을 초기화하세요.'''
pygame.init()

# pygame.display.set_mode(size=(width, height)): width, height 크기만큼 창을 생성합니다.
'''창을 만드는 코드를 완성해 보세요.'''
width, height = 640, 480
screen = pygame.display.set_mode(size=())

while True:
    # pygame.QUIT: 프로그램 창의 'X' 버튼을 누르면 발생하는 이벤트입니다.
    # sys.exit(): 프로그램을 종료합니다.
    '''event.type이 pygame.QUIT이면 프로그램을 종료하도록 코드를 완성해 보세요.'''
    for event in pygame.event.get():
        if :
