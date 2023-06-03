% g: Erdbeschleunigung
% l_1, l_2: Länge der Verbindungsstangen
% m_1, m_2: Pendelmassen
% theta_1, theta_2: Winkel der Teilpendel zum Lot
% _1: Inneres Pendel
% _2: Äußeres Pendel
syms g l_1 l_2 m_1 m_2 theta_1(t) theta_2(t)

% Position der Pendelmassen im Koordinatensystem (Trigonometrie)
x_1 = l_1 * sin(theta_1(t));
y_1 = -l_1 * cos(theta_1);

x_2 = x_1 + l_2*sin(theta_2);
y_2 = y_1 - l_2*cos(theta_2);

% Geschwindigkeiten der Pendelmassen (dx/dt bzw. dy/dt)
dx_1 = diff(x_1);
dy_1 = diff(y_1);
dx_2 = diff(x_2);
dy_2 = diff(y_2);

% Kinetische Energie der Pendelmassen
T_1 = m_1 * (dx_1^2 + dy_1^2) / 2;
T_2 = m_2 * (dx_2^2 + dy_2^2) / 2;
T   = T_1 + T_2;

% Potenzielle Energie der Pendelmassen
V_1 = m_1 * g * y_1;
V_2 = m_2 * g * y_2;
V   = V_1 + V_2;

% Lagrange-Funktion
L = T - V;

% Euler-Lagrange-Gleichungen
G_1 = diff(diff(L, diff(theta_1, t)), t) - diff(L, theta_1) == 0;
G_2 = diff(diff(L, diff(theta_2, t)), t) - diff(L, theta_2) == 0;

% Nichtlineare Gleichungen zweiter Ordnung zu System linearer DGLs erster Ordnung umwandeln
% Aus zwei Gleichungen werden vier
% In V stehen die Gleichungen, in S die Symbole
[V, S] = odeToVectorField(G_1,G_2);

% System in Matlab-Funktion unwandeln
matlabFunction(V,"File", "doppelpendel_rechte_seite", "comment", "Y(" + join([string([1;2;3;4] + "):") string(S)]), "vars", {'t', 'Y', 'g', 'l_1', 'l_2', 'm_1', 'm_2'});

