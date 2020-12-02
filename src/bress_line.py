from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def linebress(x1, y1, x2, y2):
    #  Cálculo de constantes
    dx = x2 - x1
    dy = y2 - y1
    dosdy = dy * 2
    dosdx = dx * 2
    abs_m = abs(dy / dx)
    pasos = max(abs(dx), abs(dy))

    pk = []
    x = []
    y = []
    # Cálculo de p0
    if abs_m < 1:
        if y2 < y1:
            if x2 < x1:
                pk.append(-dosdy + dx)
            else:
                pk.append(-dosdy - dx)
        else:
            if x2 < x1:
                pk.append(dosdy + dx)
            else:
                pk.append(dosdy - dx)
    elif abs_m == 1:
        pass
    else:
        if y2 < y1:
            if x2 < x1:
                pk.append(-dosdx + dy)
            else:
                pk.append(dosdx + dy)
        else:
            if x2 < x1:
                pk.append(-dosdx - dy)
            else:
                pk.append(dosdx - dy)

    x.append(x1)
    y.append(y1)

    for i in range(pasos):
        # Cálculo pk sucesivas
        if abs_m < 1:
            if y2 < y1:
                if x2 < x1:
                    if pk[i] < 0:
                        pk.append(pk[i] - dosdy)
                    else:
                        pk.append(pk[i] - dosdy + dosdx)
                else:
                    if pk[i] < 0:
                        pk.append(pk[i] - dosdy)
                    else:
                        pk.append(pk[i] - dosdy - dosdx)
            else:
                if x2 < x1:
                    if pk[i] < 0:
                        pk.append(pk[i] + dosdy)
                    else:
                        pk.append(pk[i] + dosdy + dosdx)
                else:
                    if pk[i] < 0:
                        pk.append(pk[i] + dosdy)
                    else:
                        pk.append(pk[i] + dosdy - dosdx)
        elif abs_m == 1:
            pass
        else:
            if x2 < x1:
                if y2 < y1:
                    if pk[i] < 0:
                        pk.append(pk[i] - dosdx)
                    else:
                        pk.append(pk[i] - dosdx + dosdy)
                else:
                    if pk[i] < 0:
                        pk.append(pk[i] - dosdx)
                    else:
                        pk.append(pk[i] - dosdx - dosdy)
            else:
                if y2 < y1:
                    if pk[i] < 0:
                        pk.append(pk[i] + dosdx)
                    else:
                        pk.append(pk[i] + dosdx + dosdy)
                else:
                    if pk[i] < 0:
                        pk.append(pk[i] + dosdx)
                    else:
                        pk.append(pk[i] + dosdx - dosdy)

        #  Cálculo en X
        if abs_m > 1:
            if x2 < x1:
                if pk[i] < 0:
                    x.append(x[i])
                else:
                    x.append(x[i] - 1)
            else:
                if pk[i] < 0:
                    x.append(x[i])
                else:
                    x.append(x[i] + 1)
        elif abs_m == 1:
            pass
        else:
            if x2 < x1:
                x.append(x[i] - 1)
            else:
                x.append(x[i] + 1)

        #  Cálculo en Y
        if abs_m > 1:
            if y2 < y1:
                y.append(y[i] - 1)
            else:
                y.append(y[i] + 1)
        elif abs_m == 1:
            pass
        else:
            if y2 < y1:
                if pk[i] < 0:
                    y.append(y[i])
                else:
                    y.append(y[i] - 1)
            else:
                if pk[i] < 0:
                    y.append(y[i])
                else:
                    y.append(y[i] + 1)
        #  setpixel(x[i], y[i])
    else:
        pk.pop()  # Elimina último elemento de pk, sobrante
        print(pk)
        print(x)
        print(y)


def main():
    xi = int(input("Ingresa Xi: "))
    yi = int(input("Ingresa Yi: "))
    xf = int(input("Ingresa Xf: "))
    yf = int(input("Ingresa Yf: "))

    linebress(xi, yi, xf, yf)



if __name__ == '__main__':
    main()
