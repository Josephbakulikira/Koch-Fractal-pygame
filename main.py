import pygame
import os
from segment import vector2, Segment
import math
import colorsys

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1920, 1080
size = (width, height)
black, green = (0,0,0), (71, 228, 187)
pygame.init()
pygame.display.set_caption("Koch Snowflake Fractal ")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

hue = 0.1
segments = []
a = vector2(600, 300)
b = vector2(1400, 300)
magnitude = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
height = magnitude * math.sqrt(3)/2
c = vector2(a.x + (b.x-a.x)/2, 300 + height)
s1 = Segment(a, b)
s2 = Segment(b, c)
s3 = Segment(c, a)
segments.append(s1)
segments.append(s2)
segments.append(s3)

def onMousePressed():
    global segments
    next_gen = []
    for s in segments:
        childs = s.generate();
        next_gen = childs+next_gen
    segments = next_gen

run = True
while run:
    screen.fill(black)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            onMousePressed()
    for s in segments:
        s.Display(screen, hsv_to_rgb(hue, 1, 1))
    hue += 0.002
    pygame.display.update()

pygame.quit()
