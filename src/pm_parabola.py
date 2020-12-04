import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def elipse_pm(xi, yi):
    #  Cálculo de constantes

    global x
    x = []
    global y
    y = []
    pk = [1]
    i = 0
    x0=[0]
    y0=[0]
    while x0[i] < 100:
        if pk[i] > 0:
            x0.append(x0[i] + 1)
            y0.append(y0[i] + 1)
            pk.append(pk[i] - 2 * y0[i + 1] + 1)
        else:
            x0.append(x0[i] + 1)
            y0.append(y0[i])
            pk.append(pk[i] + 1)
        i += 1

    i = len(x0)-1
    yrev = y0[::-1] # Copy y0 in reverse order to yrev
    for j in range(len(x0)):
        x0.append(x0[i] + 1)
        y0.append(yrev[j])
        i += 1
        j += 1

    for i in range(len(x0)):
        x.append(x0[i]+xi)
        y.append(y0[i]+yi)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 2500, 2500, 0)


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
    xi = int(input("Ingresa Xi: "))
    yi = int(input("Ingresa Yi: "))

    elipse_pm(xi, yi)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Parabola mediante Punto Medio")
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
