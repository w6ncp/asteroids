# Imports
import pygame as pg
from constants import *

def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill("black")
        pg.display.flip()

if __name__ == "__main__":
    main()