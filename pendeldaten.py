import matlab_anbindung


class Pendeldaten:
    def __init__(self, g, l_1, l_2, m_1, m_2, theta_1, d_theta_1, theta_2, d_theta_2):
        self.g = g
        self.l_1 = l_1
        self.l_2 = l_2
        self.m_1 = m_1
        self.m_2 = m_2
        self.theta_1 = theta_1
        self.d_theta_1 = d_theta_1
        self.theta_2 = theta_2
        self.d_theta_2 = d_theta_2

    @property
    def y(self):
        return self.theta_2, self.d_theta_2, self.theta_1, self.d_theta_1

    def update_from_matlab_res(self, res):
        _, _, _, _, _, self.theta_1, self.d_theta_1, self.theta_2, self.d_theta_2 = matlab_anbindung.matlab_result\
            .get_current_item()

