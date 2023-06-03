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

    def update_from_res_arr(self, res_arr, i):
        _, _, _, _, _, theta_1_arr, d_theta_1_arr, theta_2_arr, d_theta_2_arr = res_arr
        self.theta_1 = theta_1_arr[i]
        self.d_theta_1 = d_theta_1_arr[i]
        self.theta_2 = theta_2_arr[i]
        self.d_theta_2 = d_theta_2_arr[i]

