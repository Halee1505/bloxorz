import sys
import time
import pygame


def draw(step, start, goal, mode='auto'):
    pygame.init()
    screen = pygame.display.set_mode((16*50, 16*50))
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("arial", 20)
    ind = 0
    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ind += -1
                    if ind < 0:
                        ind = 0

                if event.key == pygame.K_SPACE and mode == 'manual':
                    ind += 1
                    if ind == len(step):
                        break

        for i in range(16):
            for j in range(16):
                if step[ind].map[i][j] == "x":
                    pygame.draw.rect(screen, "#00ffff",
                                     (i * 50, j * 50, 50, 50))
        screen.blit(font.render(step[ind].direction, True, (0, 0, 0)),
                    (1, 1))

        pygame.draw.rect(screen, "#ff0000", (goal.x *
                                             50, goal.y * 50, 50, 50))
        pygame.draw.rect(
            screen, "#0000ff", (start.x * 50, start.y * 50, 50, 50))
        if ind < len(step):
            pygame.draw.rect(
                screen, "#FFF000", (step[ind].block.node1.x * 50, step[ind].block.node1.y * 50, 50, 50))
            pygame.draw.rect(
                screen, (0, 0, 10), (step[ind].block.node2.x * 50, step[ind].block.node2.y * 50, 50, 50))
        if mode == 'auto':
            clock.tick(5)
            pygame.display.update()
            ind += 1
        else:
            pygame.display.update()
        if ind == len(step):
            clock.tick(2)
            break
