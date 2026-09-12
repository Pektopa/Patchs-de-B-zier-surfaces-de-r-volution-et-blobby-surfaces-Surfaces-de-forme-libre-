import numpy as np
import matplotlib.pyplot as plt

def gauss(h,x0):
    x = np.linspace(-4, 4, 400)
    y = h * np.exp(-(x - x0) ** 2)

    fig = plt.figure()
    plt.plot(x,y)
    plt.show()

def gauss_formula(h,x0):
    x= np.linspace(-4, 4, 400)
    return h * np.exp(-(x - x0) ** 2)

def gauss_sum(g1,g2):
    x = np.linspace(-4, 4, 400)
    somme = g1 + g2

    plt.figure(figsize=(10, 6))
    plt.plot(x, g1, '--', label='g1 (x0 = -1.5)', alpha=0.6)
    plt.plot(x, g2, '--', label='g2 (x0 = 1.5)', alpha=0.6)
    plt.plot(x, somme, label='C1 : g1(x) + g2(x)', color='red', linewidth=3)
    plt.show()

def gauss_sum2(nbPoints):
    x = np.linspace(-4, 4, nbPoints)
    y = np.linspace(-4, 4, nbPoints)
    X, Y = np.meshgrid(x, y)


    g1 = 2 * np.exp(-((X + 1.5) ** 2 + Y ** 2))
    g2 = 2 * np.exp(-((X - 1.5) ** 2 + Y ** 2))

    Z = g1 + g2

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')
    plt.show()



def courbe_blobby(nbPoints,seuil=0.2):
    x = np.linspace(-4, 4, nbPoints)
    y = np.linspace(-4, 4, nbPoints)
    X, Y = np.meshgrid(x, y)


    g1 = 2 * np.exp(-((X + 1.5) ** 2 + Y ** 2))
    g2 = 2 * np.exp(-((X - 1.5) ** 2 + Y ** 2))

    Z = g1 + g2

    plt.figure(figsize=(8, 6))
    c= plt.contour(X, Y, Z, levels=[seuil], colors='red', linewidths=2)
    plt.clabel(c, inline=True, fontsize=10, fmt={seuil: f'z={seuil}'})
    plt.show()

def surface_blobby(nbPoints):
    x = np.linspace(-4, 4, nbPoints)
    y = np.linspace(-4, 4, nbPoints)
    X, Y = np.meshgrid(x, y)

    cx, cy = -1.5, 0

    g1 = 2 * np.exp(-((X - cx) ** 2 + (Y - cy) ** 2))

    d2 = np.abs(X - cx) + np.abs(Y - cy)
    g2 = 2 * np.exp(-(d2 ** 2))

    Z = g1 + g2

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='terrain', edgecolor='none', alpha=0.9)

    plt.show()

def courbe_blobby_S2(nbPoints,seuil=0.2):
    x = np.linspace(-5, 5, nbPoints)
    y = np.linspace(-5, 5, nbPoints)
    X, Y = np.meshgrid(x, y)

    c1x, c1y = -1.5, 0
    c2x, c2y = -1.5, 0

    d1 = (X - c1x) ** 2 + (Y - c1y) ** 2
    g1 = 2 * np.exp(-d1)

    d2 = np.abs(X - c2x) + np.abs(Y - c2y)
    g2 = 2 * np.exp(-(d2 ** 2))

    Z = g1 + g2

    plt.figure(figsize=(8, 8))
    plt.contour(X, Y, Z, levels=[seuil], colors='blue', linewidths=2)
    plt.show()

gauss(2,-1.5)
gauss_sum(gauss_formula(2,-1.5),gauss_formula(2,1.5))
gauss_sum2(400)
courbe_blobby(nbPoints=400,seuil=0.2)
surface_blobby(nbPoints=400)
courbe_blobby_S2(300, 0.2)

