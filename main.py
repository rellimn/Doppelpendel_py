import pygame
import pygame_gui
import numpy as np
import math
import matlab.engine
from symbols import *
import grafik
from gamestate import GameState

# Pygame muss vor Matlab gestartet werden
pygame.init()

eng = matlab.engine.connect_matlab()
tspan = np.array([tspan_start, tspan_end], dtype=float)
y0 = np.array([theta_2_0, d_theta_2_0, theta_1_0, d_theta_1_0], dtype=float)
t, x_1, y_1, x_2, y_2 = res = [np.asarray(x).T[0] for x in eng.doppelpendel(g, l_1, l_2, m_1, m_2, tspan, y0, nargout=5)]
print(t)
res_count = len(t)
eng.quit()

pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
window_surface.fill(0xffffff)

manager = pygame_gui.UIManager(screen_dimensions)


hello_button_rect = pygame.Rect(screen_width - 100, screen_height - 100, 100, 100)
hello_button = pygame_gui.elements.UIButton(relative_rect=hello_button_rect,
                                            text='Say Hello',
                                            manager=manager)
grafik.update_pendulum_area(window_surface)

clock = pygame.time.Clock()

i = 0
i_max = len(t)
time_s = 0
state = GameState()
while not state.ending.is_active and i < i_max:
    time_delta = clock.tick() / 1000
    if state.running.is_active:
        time_s += time_delta
    while time_s < t[i] and state.running.is_active:
        time_delta = clock.tick() / 1000
        time_s += time_delta

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.end()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state.toggle_pause()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse_pos = pygame.mouse.get_pos()
            if state.paused.is_active:
                if grafik.inner_sphere.x_pos:
                    pass

        manager.process_events(event)

    # Advance animation if running
    if state.running.is_active or state.starting.is_active:
        x_rel = x_1[i] * pendulum_area_width / 4 + pendulum_area_center_x
        y_rel = -y_1[i] * pendulum_area_height / 4 + pendulum_area_center_y
        grafik.inner_sphere.pos = (x_rel, y_rel)
        x_rel = x_2[i] * pendulum_area_width / 4 + pendulum_area_center_x
        y_rel = -y_2[i] * pendulum_area_height / 4 + pendulum_area_center_y
        grafik.outer_sphere.pos = (x_rel, y_rel)
        grafik.update_pendulum_area(window_surface)
        i += 1

    manager.update(time_delta)
    manager.draw_ui(window_surface)
    pygame.display.update()

    if state.starting.is_active:
        state.toggle_pause()

