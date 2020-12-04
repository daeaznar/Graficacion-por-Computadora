from turtle import Turtle
import subprocess


def OKI(n):
    try:
        n = int(n)
    except:
        n = OKI(input("Caracter no valido: "))
    return n


def OK(n):
    try:
        n = float(n)
    except:
        n = OK(input("Caracter no valido: "))
    return n


def set_color(cf):
    try:
        t.screen.bgcolor(cf)
    except:
        pass
    return cf


def set_color2(ct):
    try:
        t.color(ct)
    except:
        ct = set_color2(input("Color no válido, escríbelo de nuevo: "))
    return ct


def main():
    subprocess.call(["cmd.exe", "/C", "cls"])
    t = Turtle()
    t.hideturtle()
    while True:
        print("DIBUJANDO POLIGONOS")

        global cf
        cf = set_color("black")
        global ct
        ct = set_color2(input("Color de trazado, escríbelo (en inglés): "))
        while ct == cf:
            ct = set_color2(input("El fondo es negro, escribe color diferente: "))

        t.pensize(5)
        n = OKI(input("Indica el número de lados del polígono: "))
        ln = OK(input("Indica la longitud del lado: "))
        ang = 180 - (((n - 2) / n) * 180)  # ángulo de giro
        for i in range(n):
            t.left(ang)
            t.fd(ln)

        t.clear()

        break


main()
