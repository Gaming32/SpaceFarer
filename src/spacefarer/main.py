import pygame
from pygame.locals import *
FULLSCREEN_FLAG = FULLSCREEN

from spacefarer.config import *
from spacefarer import shared


def main():
    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE, FULLSCREEN_FLAG if FULLSCREEN else 0)
    pygame.display.set_caption('SpaceFarer')

    clock = pygame.time.Clock()
    while True:
        shared.delta_time = clock.tick(FRAMERATE) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        ## Put code here


if __name__ == '__main__':
    main()
