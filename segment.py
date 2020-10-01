import pygame
import math

class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def subtract(a, b):
        x = a.x - b.x
        y = a.y - b.y
        return vector2(x, y)
    def add(a, b):
        x = a.x + b.x
        y = a.y + b.y
        return vector2(x, y)
    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)

        return vector2(x, y)
class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def generate(self):
        part = [i for i in range(4)]
        v = vector2.subtract(self.b, self.a)
        v = vector2(v.x/3, v.y/3)
        b1 = vector2.add(self.a, v)
        part[0] = Segment(self.a, b1)
        a1 = vector2.subtract(self.b, v)
        part[1] = Segment(a1, self.b)
        # -60 degree or -pi/3 since it's equilateral triangle
        v = v.rotate(-math.pi/3)
        c = vector2.add(b1, v)
        part[2] = Segment(b1, c)
        part[3] = Segment(c, a1)
        return part

    def Display(self, screen,color):
        pygame.draw.line(screen, color, (int(self.a.x), int(self.a.y)), (int(self.b.x), int(self.b.y)), 4)
