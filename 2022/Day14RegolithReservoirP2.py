# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:17:25 2022

@author: MaxKo
"""
import pygame

def SandFall():
    sandLoc = (source[0], source[1])
    caveMap[sandLoc[1]][sandLoc[0]] = 2
    while True:
        
        if sandLoc[1] == len(caveMap) - 1:
            pygame.draw.rect(window, sandColor, pygame.Rect(sandLoc[0]*2, sandLoc[1]*2, 2, 2))

            return True
        if caveMap[sandLoc[1] + 1][sandLoc[0]] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0]] = 2
            sandLoc = (sandLoc[0], sandLoc[1] + 1)
        elif caveMap[sandLoc[1] + 1][sandLoc[0] - 1] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0] - 1] = 2
            sandLoc = (sandLoc[0] - 1, sandLoc[1] + 1)
        elif caveMap[sandLoc[1] + 1][sandLoc[0] + 1] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0] + 1] = 2
            sandLoc = (sandLoc[0] + 1, sandLoc[1] + 1)
        else:
            pygame.draw.rect(window, sandColor, pygame.Rect(sandLoc[0]*2, sandLoc[1]*2, 2, 2))
            if sandLoc == source:
                return False
            return True
         
source = (500, 0)
rocks = []
with open('Input/Day14Input.txt') as f:
    while True:
        path = f.readline()
        if not path:
            break
        path = path.split(' ')
        rock = []
        for line in path[::2]:
            rock.append((eval(line)))
        rocks.append(rock)

yMax = max([ max(x, key = lambda a:a[1]) for x in rocks ], key = lambda a:a[1])[1]

caveMap = [[0 for i in range(0, 1000)] for i in range(0, yMax+2)]
airColor = (164,219,232)
rockColor = (0, 0, 0)
sandColor = (206, 184, 136)
pygame.init()
window = pygame.display.set_mode((len(caveMap[0])*2, (len(caveMap) + 1)*2))
window.fill(airColor)
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial.ttf', 50)
falling = True

for rock in rocks:
    for point in range(0, len(rock)):
        caveMap[rock[point][1]][rock[point][0]] = 1
        
        nextPoint = point + 1
        if nextPoint == len(rock):
            break
        if rock[point][0] == rock[nextPoint][0]:
            if rock[point][1] < rock[nextPoint][1]:
                for y in range(rock[point][1], rock[nextPoint][1]):
                    caveMap[y][rock[point][0]] = 1
            else:
                for y in range(rock[nextPoint][1], rock[point][1]):
                    caveMap[y][rock[point][0]] = 1   
        else:
            if rock[point][0] < rock[nextPoint][0]:
                for x in range(rock[point][0], rock[nextPoint][0]):
                    caveMap[rock[point][1]][x] = 1
            else:
                for x in range(rock[nextPoint][0], rock[point][0]):
                    caveMap[rock[point][1]][x] = 1

for y in range(0, len(caveMap)):
    for x in range(0, len(caveMap[0])):
        if caveMap[y][x] == 1:
            pygame.draw.rect(window, rockColor, pygame.Rect(x*2, y*2, 2, 2))
pygame.draw.rect(window, rockColor,pygame.Rect(0, len(caveMap) * 2, len(caveMap[0]) * 2, 2))
pygame.display.flip()

sandCount = 0
running = True
while running:
    if falling:
        window.fill(airColor, (0, 0, 200, 100))
        falling = SandFall()
        sandCount += 1
        countText = font.render(str(sandCount), True, (255, 255, 255))
        window.blit(countText, (5, 5))
        pygame.display.flip()
        clock.tick(600)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

                
        
        