import sys
import time
import pygame

pygame.init()
screen = pygame.display.set_mode((16*50, 16*50))
screen.fill((255, 255, 255))


def draw(game, step):
    ind = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ind += 1
                    if ind == len(step):
                        ind = 0
        for i in range(16):
            for j in range(16):
                if game.map[i][j] == "x":
                    pygame.draw.rect(screen, "#00ffff",
                                     (i * 50, j * 50, 50, 50))
        pygame.draw.rect(screen, "#ff0000", (game.goal.x *
                                             50, game.goal.y * 50, 50, 50))
        pygame.draw.rect(
            screen, "#0000ff", (game.block.node1.x * 50, game.block.node1.y * 50, 50, 50))

        pygame.draw.rect(
            screen, "#FFF000", (step[ind].block.node1.x * 50, step[ind].block.node1.y * 50, 50, 50))
        pygame.draw.rect(
            screen, (0, 0, 10), (step[ind].block.node2.x * 50, step[ind].block.node2.y * 50, 50, 50))

        pygame.display.update()
