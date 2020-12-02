from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w, h = 500, 500


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


# ---Section 1---
def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)  # Begin the sketch
    glVertex2f(10, 10)  # Coordinates for the bottom left point
    glVertex2f(20, 10)  # Coordinates for the bottom right point
    glVertex2f(20, 20)  # Coordinates for the top right point
    glVertex2f(10, 20)  # Coordinates for the top left point
    glEnd()  # Mark the end of drawing

def square2():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS)  # Begin the sketch
    glVertex2f(100, 100)  # Coordinates for the bottom left point
    glVertex2f(200, 100)  # Coordinates for the bottom right point
    glVertex2f(200, 200)  # Coordinates for the top right point
    glVertex2f(100, 200)  # Coordinates for the top left point
    glEnd()  # Mark the end of drawing


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# ---Section 2---

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Remove everything from screen (i.e. displays all white)
    glLoadIdentity()  # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0)  # Set the color to pink
    square()
    square2()# Draw a square using our function
    glutSwapBuffers()


# ---Section 3---

x1= int(input("Dame x1: "))
y1= int(input("Dame y1: "))
glutInit()
glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
glutInitWindowSize(500, 500)  # Set the w and h of your window
glutInitWindowPosition(0, 0)  # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Square")  # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)  # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop