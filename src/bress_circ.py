import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def circ_pm(xc, yc, r):
    #  Cálculo de constantes

    global x
    x = []
    global y
    y = []

    pk = [1 - r]
    x0 = [0]
    y0 = [r]
    dosx = [x0[0] * 2]
    dosy = [y0[0] * 2]
    i = 0
    while y0[i] > x0[i]:
        if pk[i] < 0:
            x0.append(x0[i] + 1)
            y0.append(y0[i])
            dosx.append(x0[i + 1] * 2)
            dosy.append(y0[i + 1] * 2)
            pk.append(pk[i] + dosx[i] + 3)
        else:
            x0.append(x0[i] + 1)
            y0.append(y0[i] - 1)
            dosx.append(x0[i + 1] * 2)
            dosy.append(y0[i + 1] * 2)
            pk.append(pk[i] + dosx[i] - dosy[i] + 5)
        i += 1

    #   ***ESPEJEO***
    for i in range(len(x0)):  # 2° Octante para Completar 1° Cuadrante
        x0.append(y0[i])
        y0.append(x0[i])
        i += 1

    for i in range(len(x0)):  # 2° Octante sumando (xc,yc)
        x.append(x0[i] + xc)
        y.append(y0[i] + yc)
        i += 1

    espejoY = []
    for i in range(len(x)):  # 2° Cuadrante en Y hacia arriba
        x.append(x[i])
        espejoY.append(y[i] - 2 * (r - ((yc + r) - y[i])))
        y.append(espejoY[i])

    espejoX = []
    for i in range(len(x0)):  # 3° Cuadrante en X hacia izquierda
        y.append(y[i])
        espejoX.append(x[i] - 2 * (r - ((xc + r) - x[i])))
        x.append(espejoX[i])

    for i in range(len(x0)):  # 4° Cuadrante, esquina opuesta
        x.append(espejoX[i])
        y.append(espejoY[i])


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
    for i in range(len(x)):
        glVertex2f(x[i] * 10, y[i] * 10)
        print(x[i], y[i])
    glEnd()
    glFlush()


def main():
    xc = int(input("Ingresa Xc: "))
    yc = int(input("Ingresa Yc: "))
    r = int(input("Ingresa el radio: "))

    circ_pm(xc, yc, r)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Circunferencia mediante Punto Medio/Bressenham")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()


def pixelcolor():
    glColor3f(255, 0, 0)
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