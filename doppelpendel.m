function [t,x_1,y_1,x_2,y_2, theta_1, d_theta_1, theta_2, d_theta_2]=doppelpendel(g,l_1,l_2,m_1,m_2,tspan,y_0)
    [t, y] = ode89(@(t, y) doppelpendel_rechte_seite(t, y, g, l_1, l_2, m_1, m_2), tspan, y_0);
    theta_1 = y(:, 3);
    d_theta_1 = y(:, 4);
    theta_2 = y(:, 1);
    d_theta_2 = y(:, 2);
    x_1 = l_1*sin(theta_1);
    y_1 = -l_1*cos(theta_1);
    x_2 = x_1 + l_2*sin(theta_2);
    y_2 = y_1 - l_2*cos(theta_2);
end
