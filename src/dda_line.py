import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def line_dda(x1, y1, x2, y2):
    #  Cálculo de constantes
    dx = x2 - x1
    dy = y2 - y1
    abs_m = abs(dy / dx)
    global pasos
    pasos = max(abs(dx), abs(dy))
    xinc = dx / pasos
    yinc = dy / pasos

    global x
    x = []
    global y
    y = []
    x.append(x1)
    y.append(y1)

    if dx!= 0:
        if abs_m == 1:
            for i in range(pasos):
                if dx < 0 > dy:
                    x.append(x[i] - 1)
                    y.append(y[i] - 1)
                elif dx < 0 < dy:
                    x.append(x[i] - 1)
                    y.append(y[i] + 1)
                elif dx > 0 > dy:
                    x.append(x[i] + 1)
                    y.append(y[i] - 1)
                elif dx > 0 < dy:
                    x.append(x[i] + 1)
                    y.append(y[i] + 1)
        else:
            # Cálculo de X
            for i in range(pasos):
                if x2 > x1:
                    if abs_m > 1:
                        x.append(x[i] + 1 / abs_m)
                    else:
                        x.append(x[i] + 1)
                else:
                    if abs_m > 1:
                        x.append(x[i] - 1 / abs_m)
                    else:
                        x.append(x[i] - 1)

                # Cálculo de Y
                if y2 > y1:
                    if abs_m > 1:
                        y.append(y[i] + 1)
                    else:
                        y.append(y[i] + abs_m)
                else:
                    if abs_m > 1:
                        y.append(y[i] - 1)
                    else:
                        y.append(y[i] - abs_m)
                if abs_m > 1:
                    x[i] = round(x[i])
                else:
                    y[i] = round(y[i])
    else:
        if dy == 0:
            x.append(x1)
            y.append(y1)
        else:
            for i in range(pasos):
                if dy > 0:
                    x.append(x[i])
                    y.append(y[i] + 1)

                else:
                    x.append(x[i])
                    y.append(y[i] - 1)



def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 950, 950, 0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    # Drawing Points with coordinate (x,y)
    pixelcolor()
    glPointSize(10.0)
    glBegin(GL_POINTS)
    print("X", "Y")
    for i in range(pasos):
        glVertex2f(x[i] * 10, y[i] * 10)
        print(x[i], y[i])
    glEnd()
    glFlush()


def main():
    xi = int(input("Ingresa Xi: "))
    yi = int(input("Ingresa Yi: "))
    xf = int(input("Ingresa Xf: "))
    yf = int(input("Ingresa Yf: "))

    line_dda(xi, yi, xf, yf)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Linea mediante DDA")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
    # glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS);


def pixelcolor():
    print("Escoja color para trazado de pixeles: \n"  # Menú principal
          "1. Rojo\n"
          "2. Verde\n"
          "3. Azul\n"
          "4. Amarillo\n"
          "5. Rosa\n"
          "6. Blanco\n")
    opc = int(input("Opción: "))

    if opc == 1:
        glColor3f(255, 0, 0)
    elif opc == 2:
        glColor3f(0, 255, 0)
    elif opc == 3:
        glColor3f(0, 0, 255)
    elif opc == 4:
        glColor3f(255, 255, 0)
    elif opc == 5:
        glColor3f(255, 0, 127)
    elif opc == 6:
        glColor3f(255, 255, 255)
    else:
        print("Opción inválida\n")
