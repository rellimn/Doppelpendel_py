import pygame
import pygame_gui

import matlab_anbindung
from globals import *
import grafik
import matlab_anbindung as mla
from gamestate import GameState
from pendeldaten import Pendeldaten

# Pygame muss vor Matlab gestartet werden
pygame.init()
pygame.display.set_caption('Doppelpendel')
window_surface = pygame.display.set_mode(screen_dimensions, pygame.FULLSCREEN)
window_surface.fill(0xffffff)
gui_manager = pygame_gui.UIManager(screen_dimensions, theme_path="ui_theme.json")


hello_button_rect = pygame.Rect(screen_width - 100, screen_height - 100, 100, 100)
hello_button = pygame_gui.elements.UIButton(relative_rect=hello_button_rect,
                                            text='Say Hello',
                                            manager=gui_manager)
start_matlab_text_rect = pygame.Rect(pendulum_area_width/2-110, pendulum_area_height/2-30, 250, 50)
start_matlab_text = pygame_gui.elements.UILabel(relative_rect=start_matlab_text_rect,
                                                text="Starte Matlab...",
                                                manager=gui_manager,
                                                object_id=pygame_gui.core.ObjectID(class_id="@notification_label",
                                                                                   object_id="#start_matlab_text"))
gui_manager.update(0)
gui_manager.draw_ui(window_surface)
pygame.display.update()

mla.start_matlab()

start_matlab_text.kill()
del start_matlab_text
del start_matlab_text_rect
gui_manager.update(0)
gui_manager.draw_ui(window_surface)
pygame.display.update()


clock = pygame.time.Clock()

pendeldaten = Pendeldaten(g_0, l_1_0, l_2_0, m_1_0, m_2_0, theta_1_0, d_theta_1_0, theta_2_0, d_theta_2_0)
mla.update_from_matlab(pendeldaten)
t, x_1, y_1, x_2, y_2, theta_1, d_theta_1, theta_2, d_theta_2 = next(mla.matlab_result)

state = GameState(pendeldaten, x_1, y_1, x_2, y_2)
state.running_callback = lambda: print("Still Running")

grafik.update_pendulum_area(window_surface, state.sphere_link)

time_s = 0
while not state.ending.is_active:
    t, x_1, y_1, x_2, y_2, theta_1, d_theta_1, theta_2, d_theta_2 = mla.matlab_result.get_current_item()
    time_delta = clock.tick() / 1000
    if state.running.is_active:
        time_s += time_delta
    while time_s < t and state.running.is_active:
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
                if state.paused.is_active and state.inner_sphere.contains_pos(mouse_pos):
                    state.move_inner_sphere()
        if event.type == pygame.MOUSEBUTTONUP:
            if state.moving_inner_sphere.is_active:
                state.stop_moving_inner_sphere()

        gui_manager.process_events(event)

    # Advance animation if running
    if state.running.is_active or state.starting.is_active:
        state.pendeldaten.update_from_matlab_res(mla.matlab_result)
        state.inner_sphere.pos = mla.convert_math_pos_to_sphere_pos(x_1, y_1)
        state.outer_sphere.pos = mla.convert_math_pos_to_sphere_pos(x_2, y_2)
        next(mla.matlab_result)

    elif state.moving_inner_sphere.is_active:
        mouse_x, mouse_y = mouse_pos = pygame.mouse.get_pos()
        if mouse_x < pendulum_area_width:
            state.inner_sphere.pos = mouse_pos
            #grafik.update_pendulum_area(window_surface)

    grafik.update_pendulum_area(window_surface, state.sphere_link)
    grafik.draw_toolbox_area(window_surface)
    gui_manager.update(time_delta)
    gui_manager.draw_ui(window_surface)
    pygame.display.update()

    if state.starting.is_active:
        state.toggle_pause()

