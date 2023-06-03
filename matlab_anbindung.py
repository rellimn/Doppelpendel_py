import matlab.engine
import numpy as np
from globals import *

_eng = None


def start_matlab():
    global _eng
    _eng = matlab.engine.start_matlab()


def get_new_res_from_matlab(pendeldaten):
    # Return: t, x_1, y_1, x_2, y_2
    if _eng is None:
        raise RuntimeError("Matlab läuft nicht")
    tspan = np.array([tspan_start, tspan_end], dtype=float)
    y = np.array(pendeldaten.y, dtype=float)
    return [np.asarray(x).T[0] for x in _eng.doppelpendel(pendeldaten.g, pendeldaten.l_1, pendeldaten.l_2,
                                                          pendeldaten.m_1, pendeldaten.m_2, tspan, y, nargout=9)]


def convert_math_pos_to_sphere_pos(x, y):
    x_sphere = x * pendulum_area_width / 4 + pendulum_area_center_x
    y_sphere = -y * pendulum_area_height / 4 + pendulum_area_center_y
    return x_sphere, y_sphere


def quit_matlab():
    global _eng
    if _eng is not None:
        _eng.quit()
    _eng = None
