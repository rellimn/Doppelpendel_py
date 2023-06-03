import math
import pygame
from globals import *


class Sphere:
    def __init__(self, m, x=0, y=0):
        self.radius = None
        self.set_radius_from_m(m)
        self.x_pos, self.y_pos = (x, y)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, self.pos, self.radius)

    @property
    def pos(self):
        return self.x_pos, self.y_pos

    @pos.setter
    def pos(self, value):
        self.x_pos, self.y_pos = value

    def contains_pos(self, pos):
        x, y = pos
        return math.sqrt((x - self.x_pos)**2 + (y - self.y_pos)**2) < self.radius

    def set_radius_from_m(self, m):
        self.radius = math.floor(math.sqrt(m)*sphere_base_radius)


class Link:
    def __init__(self, inner_sphere, outer_sphere):
        self.inner_sphere = inner_sphere
        self.outer_sphere = outer_sphere

    def draw(self, screen):
        pygame.draw.line(screen, link_color, self.outer_sphere.pos, self.inner_sphere.pos, link_width)
        pygame.draw.line(screen, link_color, self.inner_sphere.pos, pendulum_area_center_pos, link_width)


pendulum_area_rect = pygame.Rect(0, 0, screen_width*3/4, screen_height)
toolbox_area_rect = pygame.Rect(screen_width*3/4, 0, screen_width/4, screen_height)


def draw_axes(screen):
    pygame.draw.line(screen, 0x0, (0, screen_height / 2), (screen_width * 3 / 4, screen_height / 2))
    pygame.draw.line(screen, 0x0, (screen_width*3/8, 0), (screen_width*3/8, screen_height))


def draw_toolbox_area(screen):
    pygame.draw.rect(screen, 0xFFFFFF, toolbox_area_rect)
    pygame.draw.line(screen, 0x0, (toolbox_area_rect.x, 0), (toolbox_area_rect.x, toolbox_area_rect.height))


def clear_pendulum_area(screen):
    screen.fill(0xFFFFFF, rect=pendulum_area_rect)


def update_pendulum_area(screen, sphere_link):
    clear_pendulum_area(screen)
    sphere_link.draw(screen)
    draw_axes(screen)
    sphere_link.inner_sphere.draw(screen, inner_sphere_color)
    sphere_link.outer_sphere.draw(screen, outer_sphere_color)

