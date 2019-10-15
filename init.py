import numpy as np
import my_math as m

'''
A  = [
 0   1   0
 0   0   1
-1 -a1 -a2
]
'''


def init_a(a1, a2):
    a = np.zeros((3, 3))
    a[0][1] = 1
    a[1][2] = 1
    a[2][0] = -1
    a[2][1] = -a1
    a[2][2] = -a2
    return a


'''
B = [
    0
    0
    b
]
'''


def init_b():
    b = np.zeros((3, 1))
    b[2] = float(1)
    return b


'''
c=(1 0 0)
'''


def init_c():
    c = np.zeros((1, 3))
    c[0][0] = 1
    return c


def calculate_f(a, t, q):
    f = np.eye(3)
    q = int(q)
    val = a * t

    for i in range(1, q+1):
        f += m.pow_matrix(val, i)/m.fact(i)

    return f


def calculate_g(f, a):
    b = init_b()
    g = f - np.eye(3)
    g = g.dot(a)
    g = g@b
    return g


def calculate_x(f, g, x, u):
    return f@x + g*u


def init_y(x, t):
    y = []
    c = init_c()

    for i in range(len(t)):
        y.append((c@x[i])[0][0])

    return y
