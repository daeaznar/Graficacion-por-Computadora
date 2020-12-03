import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def circ_dda(xc, yc, r):
    #  Cálculo de constantes

    r = r
    r2 = r ** 2
    global x
    x = []
    global y
    y = []

    x0 = [0]
    y0 = [r]
    i = 0
    while y0[i] >= x0[i]:    # 1° Octante en (x0,y0)
        y_temp = (r ** 2 - x0[i] ** 2) ** 0.5
        x0.append(i + 1)
        y0.append(round(y_temp))
        i += 1
    x0.pop()
    y0.pop(0)
    for i in range(len(x0)):    # 2° Octante para Completar 1° Cuadrante
        x0.append(y0[i])
        y0.append(x0[i])
        i += 1

    for i in range(len(x0)): # 2° Octante sumando (xc,yc)
        x.append(x0[i]+xc)
        y.append(y0[i]+yc)
        i += 1

    espejoY=[]
    for i in range(len(x)): # 2° Cuadrante en Y hacia arriba
        x.append(x[i])
        espejoY.append(y[i]-2*(r-((yc+r)-y[i])))
        y.append(espejoY[i])

    espejoX=[]
    for i in range(len(x0)):  # 3° Cuadrante en X hacia izquierda
        y.append(y[i])
        espejoX.append(x[i]-2*(r-((xc+r)-x[i])))
        x.append(espejoX[i])

    for i in range(len(x0)):  # 4° Cuadrante, esquina opuesta
        x.append(espejoX[i])
        y.append(espejoY[i])

    print("X","Y")
    print(x, y)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 1500, 1500, 0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    # Drawing Points with coordinate (x,y)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    for i in range(len(x)):
        glVertex2f(x[i] * 10, y[i] * 10)
        print(x[i], y[i])
    glEnd()
    glFlush()


def main():
    xc = int(input("Ingresa Xc: "))
    yc = int(input("Ingresa Yc: "))
    r = int(input("Ingresa el radio: "))

    circ_dda(xc, yc, r)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(950, 950)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Linea mediante DDA")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
