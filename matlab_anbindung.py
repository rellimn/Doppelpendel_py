import matlab.engine
import numpy as np
from globals import *


class MatlabResult:
    def __init__(self, res):
        self.current_item = 0
        self.t_arr, self.x_1_arr, self.y_1_arr, self.x_2_arr, self.y_2_arr, self.theta_1_arr, self.d_theta_1_arr,\
            self.theta_2_arr, self.d_theta_2_arr = res

    @property
    def res(self):
        return self.t_arr, self.x_1_arr, self.y_1_arr, self.x_2_arr, self.y_2_arr, self.theta_1_arr,\
            self.d_theta_1_arr, self.theta_2_arr, self.d_theta_2_arr

    @res.setter
    def res(self, _res):
        self.t_arr, self.x_1_arr, self.y_1_arr, self.x_2_arr, self.y_2_arr, self.theta_1_arr, \
            self.d_theta_1_arr, self.theta_2_arr, self.d_theta_2_arr = _res

    def get_current_item(self):
        return self[self.current_item]

    def __len__(self):
        return len(self.t_arr)

    def __getitem__(self, item):
        return [x[item] for x in self.res]

    def __next__(self):
        if self.current_item < len(self):
            x = self.get_current_item()
            self.current_item += 1
            return x
        raise StopIteration


_eng = None
matlab_result = None


def start_matlab():
    global _eng
    _eng = matlab.engine.start_matlab()


def update_from_matlab(pendeldaten):
    global matlab_result
    if _eng is None:
        raise RuntimeError("Matlab läuft nicht")
    tspan = np.array([tspan_start, tspan_end], dtype=float)
    y = np.array(pendeldaten.y, dtype=float)
    matlab_result = MatlabResult([np.asarray(x).T[0] for x in _eng.doppelpendel(pendeldaten.g, pendeldaten.l_1, pendeldaten.l_2,
                                                         pendeldaten.m_1, pendeldaten.m_2, tspan, y, nargout=9)])


def convert_math_pos_to_sphere_pos(x, y):
    x_sphere = x * pendulum_area_width / 4 + pendulum_area_center_x
    y_sphere = -y * pendulum_area_height / 4 + pendulum_area_center_y
    return x_sphere, y_sphere


def quit_matlab():
    global _eng
    if _eng is not None:
        _eng.quit()
    _eng = None
