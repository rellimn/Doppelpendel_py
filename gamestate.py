from statemachine import StateMachine, State

from globals import *
from grafik import Sphere, Link
from matlab_anbindung import convert_math_pos_to_sphere_pos


class GameState(StateMachine):
    starting = State("Starting", initial=True)
    paused = State("Paused")
    running = State("Running")
    ending = State("Ending", final=True)
    moving_inner_sphere = State("Moving inner sphere")

    toggle_pause = starting.to(paused) | paused.to(running) | running.to(paused)
    end = starting.to(ending) | paused.to(ending) | running.to(ending) #| is_stuck.to(ending)
    move_inner_sphere = paused.to(moving_inner_sphere)
    stop_moving_inner_sphere = moving_inner_sphere.to(paused)

    cont = paused.to(running)
    pause = running.to(paused)

    def __init__(self, pendeldaten, x_1_0, y_1_0, x_2_0, y_2_0):
        self.pendeldaten = pendeldaten
        self.inner_sphere = Sphere(pendeldaten.m_1, *convert_math_pos_to_sphere_pos(x_1_0, y_1_0))
        self.outer_sphere = Sphere(pendeldaten.m_2, *convert_math_pos_to_sphere_pos(x_2_0, y_2_0))
        self.sphere_link = Link(self.inner_sphere, self.outer_sphere)
        self.running_callback = lambda: print("Running")
        super(GameState, self).__init__()

    def on_enter_running(self):
        self.running_callback()


