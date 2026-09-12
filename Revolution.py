import numpy as np
import matplotlib.pyplot as plt

def cylindre_revolution(h,nbPoints):

    rayon = np.sqrt(3 ** 2 + 4 ** 2)

    theta = np.linspace(0, 2 * np.pi, nbPoints)
    t = np.linspace(0, h, nbPoints)

    T, z = np.meshgrid(theta, t)


    x = rayon * np.cos(T)
    y = rayon * np.sin(T)



    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,z,cmap="viridis")

    plt.show()

def sphere(nbPoints):
    rayon =2
    phi = np.linspace(-np.pi / 2, np.pi / 2, nbPoints)
    theta = np.linspace(0, 2 * np.pi, nbPoints)

    Phi, Theta = np.meshgrid(phi, theta)

    x = 1 + rayon * np.cos(Phi) * np.cos(Theta)
    y = 1 + rayon * np.cos(Phi) * np.sin(Theta)
    z = 1 + rayon * np.sin(Phi)


    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,z,cmap="viridis")
    ax.set_aspect("equal")
    plt.show()

def cone_revolution(nbPoints,h):
    rayon = np.sqrt(1 ** 2 + 1 ** 2)
    u = np.linspace(0, h, nbPoints)
    v = np.linspace(0, 2 * np.pi, nbPoints)

    U, V = np.meshgrid(u, v)

    x = rayon*U * np.cos(V)
    y = rayon*U * np.sin(V)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,rayon*U,cmap="viridis")
    plt.show()


def paraboloide_revolution(nbPoints,h):
    rayon = np.sqrt(1 ** 2 + 1 ** 2)
    pente = np.sqrt(0 ** 2 + 0 ** 2)

    u = np.linspace(0, h, nbPoints)
    v = np.linspace(0, 2 * np.pi, nbPoints)

    u, v = np.meshgrid(u, v)

    x = u * np.cos(v)
    y = u * np.sin(v)
    z = 0.5*(x**2 + y**2)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,z,cmap="viridis")
    plt.show()

def hyperboloide_revolution(nbPoints,h):
    a = 1
    c = 1

    u = np.linspace(-h, h, nbPoints)
    v = np.linspace(0, 2 * np.pi, nbPoints)

    U, V = np.meshgrid(u, v)

    x = a * np.cosh(U) * np.cos(V)
    y = a * np.cosh(U) * np.sin(V)
    z = c * np.sinh(U)


    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,z,cmap="viridis")
    plt.show()


cylindre_revolution(5,50)
sphere(50)
cone_revolution(50,5)
paraboloide_revolution(50,5)
hyperboloide_revolution(50,5)

