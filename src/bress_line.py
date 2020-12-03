import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def line_bress(x1, y1, x2, y2):
    #  Cálculo de constantes
    dx = x2 - x1
    dy = y2 - y1
    dosdy = dy * 2
    dosdx = dx * 2
    abs_m = abs(dy / dx)
    global pasos
    pasos = max(abs(dx), abs(dy))

    global pk
    pk = []
    global x
    x = []
    global y
    y = []
    x.append(x1)
    y.append(y1)

    if abs_m == 1:
        for i in range(pasos):
            if dx < 0 > dy:
                x.append(x[i] - 1)
                y.append(y[i] - 1)
            elif dx < 0 < dy:
                x.append(x[i] - 1)
                y.append(y[i] + 1)
            elif dx > 0 >dy:
                x.append(x[i] + 1)
                y.append(y[i] - 1)
            elif dx > 0 <dy:
                x.append(x[i] + 1)
                y.append(y[i] + 1)
    else:
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

    pk.pop()  # Elimina último elemento de pk, sobrante
    print(pk)
    print(x)
    print(y)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 950, 950, 0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    # Drawing Points with coordinate (x,y)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    for i in range(pasos):
        glVertex2f(x[i] * 10, y[i] * 10)
    glEnd()
    glFlush()


def main():
    xi = int(input("Ingresa Xi: "))
    yi = int(input("Ingresa Yi: "))
    xf = int(input("Ingresa Xf: "))
    yf = int(input("Ingresa Yf: "))

    line_bress(xi, yi, xf, yf)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Linea mediante Bressenham")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
