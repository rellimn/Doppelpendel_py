from math import pi, radians
# Konstanten
g = 9.81
l_1 = 1.
l_2 = 0.5
m_1 = 1.
m_2 = 3.
# Startbedingungen
theta_1_0 = radians(90)
d_theta_1_0 = 0
theta_2_0 = radians(90)
d_theta_2_0 = 0
tspan_start = 0
tspan_end = 100

# Grafik
inner_sphere_color = 0xFF0000
outer_sphere_color = 0x0000FF
sphere_base_radius = 10
link_color = 0x0
link_width = 3

screen_width, screen_height = screen_dimensions = (1920, 1080)

pendulum_area_center_x, pendulum_area_center_y = pendulum_area_center_pos = (screen_width*3/8, screen_height/2)
pendulum_area_width = screen_width*3/4
pendulum_area_height = screen_height

fps = 120
