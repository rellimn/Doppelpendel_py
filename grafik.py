import math
import pygame
from symbols import *


class Sphere:
    def __init__(self, m, x=0, y=0):
        self.x_pos, self.y_pos = (x, y)
        self.radius = math.floor(math.sqrt(m)*sphere_base_radius)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.pos, self.radius)

    @property
    def pos(self):
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, value):
        self.x_pos, self.y_pos = value


class Link:
    def __init__(self, inner_sphere, outer_sphere):
        self.inner_sphere = inner_sphere
        self.outer_sphere = outer_sphere

    def draw(self, screen):
        pygame.draw.line(screen, link_color, self.outer_sphere.pos, self.inner_sphere.pos, link_width)
        pygame.draw.line(screen, link_color, self.inner_sphere.pos, pendulum_area_center_pos, link_width)


pendulum_area_rect = pygame.Rect(0, 0, screen_width*3/4, screen_height)
toolbox_area_rect = pygame.Rect(screen_width*3/4, 0, screen_width/4, screen_height)
inner_sphere = Sphere(m_1, pendulum_area_center_x + 100, pendulum_area_center_y + 50)
outer_sphere = Sphere(m_2, pendulum_area_center_x + 20, pendulum_area_center_y - 60)
link = Link(inner_sphere, outer_sphere)


def draw_axes(screen):
    pygame.draw.line(screen, 0x0, (0, screen_height / 2), (screen_width * 3 / 4, screen_height / 2))
    pygame.draw.line(screen, 0x0, (screen_width*3/8, 0), (screen_width*3/8, screen_height))


def draw_toolbox_are(screen):
    pygame.draw.rect(screen, 0x0, toolbox_area_rect)


def clear_pendulum_area(screen):
    screen.fill(0xFFFFFF, rect=pendulum_area_rect)


def update_pendulum_area(screen):
    clear_pendulum_area(screen)
    link.draw(screen)
    draw_axes(screen)
    inner_sphere.draw(screen, inner_sphere_color)
    outer_sphere.draw(screen, outer_sphere_color)
