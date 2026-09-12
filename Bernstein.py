import numpy as np
import matplotlib.pyplot as plt


def pascal_triangle(n):
    triangle = np.zeros((n, n), dtype=int)
    for i in range(n):
        triangle[i][0] = 1
        for j in range(1, i + 1):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def binomial_coef(n,i):
    if i > n:
        return 0
    triangle = pascal_triangle(n + 1)
    return triangle[n][i]

def bernstein_pol(n, i, t):
    if not (0 <= i <= n):
        return 0
    return binomial_coef(n, i) * (t ** i) * ((1 - t) ** (n - i))

def bezier_bernstein(points, t):
    curve = np.zeros((len(t), 2))

    for i in range(len(points)):
        weights = bernstein_pol(len(points) - 1, i, t)  # shape (len(t),)
        curve += weights[:, np.newaxis] * points[i]

    return curve

def bezier_patch(ctrlpoints,u,v):

    curve = np.zeros(3)
    p = ctrlpoints.shape[0] - 1
    t = ctrlpoints.shape[1] - 1

    u = float(np.asarray(u))
    v = float(np.asarray(v))

    for n in range(p + 1):
        k1 = bernstein_pol(p, n, u)
        for m in range(t + 1):
            k2 = bernstein_pol(t, m, v)
            curve += (k1 * k2) * ctrlpoints[n, m]
    return curve



points = np.array([[[0, 0, 0], [0,1,0], [0,2,0], [0,3,0]],
                  [[1,0,0], [1,1,2], [1,2,3], [1,3,0]],
                  [[2,0,0], [2,1,1], [2,2,1], [2,3,0]],
                  [[3,0,0], [3,1,0], [3,2,0], [3,3,0]]])


t = np.linspace(0, 1, 10)
bezier_test = bezier_patch(points,0.5,0.5)
print("Point de la courbe de Bézier pour t=[0.5,0.5] : ", bezier_test)

bezier = bezier_patch(points, 0.25,0.75)


u_vals = np.linspace(0, 1, 30)
v_vals = np.linspace(0, 1, 30)
surface = np.zeros((len(u_vals), len(v_vals), 3))

for i, u in enumerate(u_vals):
    for j, v in enumerate(v_vals):
        surface[i, j] = bezier_patch(points, u, v)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(surface[:, :, 0], surface[:, :, 1], surface[:, :, 2], cmap="viridis", alpha=0.85)
ax.set_title("Patch de Bezier")

plt.show()
