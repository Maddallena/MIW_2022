import numpy as np
from numpy.linalg import eigh, norm

# zaczynamy od macierzy A
a = np.array([[-5,2,3],[2,5,1],[-3,1,-5]])

# obliczamy wartosci własne do macierzy V
#
wartosci_walsne_do_v, V = np.linalg.eigh(a.T @ a)
print(V)

# obliczanie U wykorzystując macierz a i odpowiednią kolumnę macierzy V
u0 = a @ V[:, 0] / norm(a @ V[:, 0])
u1 = a @ V[:, 1] / norm(a @ V[:, 0])
u2 = a @ V[:, 2] / norm(a @ V[:, 0])


U = np.array([u0,u1,u2]).T
# v nie trzeba transponować, bo takie właśnie powstaje w numpy

np.round(U.T @ a @ V, decimals=5)