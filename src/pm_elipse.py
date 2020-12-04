import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def elipse_pm(xc, yc, rx, ry):
    #  Cálculo de constantes

    rx2 = rx ** 2
    ry2 = ry ** 2
    global x
    x = []
    global y
    y = []

    p1k = [ry2 - rx2 * ry + 1 / 4 * rx2]
    x0 = [0]
    y0 = [ry]
    i = 0
    while 2 * ry2 * x0[i] < 2 * rx2 * y0[i]:
        if p1k[i] < 0:
            x0.append(x0[i] + 1)
            y0.append(y0[i])
            p1k.append(p1k[i] + 2 * ry2 * x0[i + 1] + ry2)
        else:
            x0.append(x0[i] + 1)
            y0.append(y0[i] - 1)
            p1k.append(p1k[i] + 2 * ry2 * x0[i + 1] + ry2 - 2 * rx2 * y0[i + 1])
        i += 1
    print(x0, y0)
    p2k = [ry2 * (x0[i] + 1 / 2) ** 2 + rx2 * (y0[i] - 1) ** 2 - rx2 * ry2]
    j = 0
    while y0[i] != 0:
        if p2k[j] > 0:
            x0.append(x0[i])
            y0.append(y0[i] - 1)
            p2k.append(p2k[j] - 2 * rx2 * y0[i + 1] + rx2)
        else:
            x0.append(x0[i] + 1)
            y0.append(y0[i] - 1)
            p2k.append(p2k[j] + 2 * ry2 * x0[i + 1] - 2 * rx2 * y0[i + 1] + rx2)
        i += 1
        j += 1
    print(p1k)
    print(p2k)
    print(x0, y0)
    # ***ESPEJEO***

    for i in range(len(x0)):  # 2° Octante sumando (xc,yc)
        x.append(x0[i] + xc)
        y.append(y0[i] + yc)
        i += 1

    espejoY = []
    for i in range(len(x)):  # 2° Cuadrante en Y hacia arriba
        x.append(x[i])
        espejoY.append(y[i] - 2 * (ry - ((yc + ry) - y[i])))
        y.append(espejoY[i])

    espejoX = []
    for i in range(len(x0)):  # 3° Cuadrante en X hacia izquierda
        y.append(y[i])
        espejoX.append(x[i] - 2 * (rx - ((xc + rx) - x[i])))
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
    rx = int(input("Ingresa el radio en X: "))
    ry = int(input("Ingresa el radio en Y: "))

    elipse_pm(xc, yc, rx, ry)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Elipse mediante Punto Medio/Bressenham")
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
