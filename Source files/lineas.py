def dda():
    print("Esta es la linea DDA")


def bress():
    print("Esta es la linea Bressenham")


def menu_lineas():
    while True:
        print("¿Qué algoritmo quieres usar?\n"
              "1. DDA\n"
              "2. Bressenham\n"
              "0. Regresar\n")
        opc= int(input("Opción: "))

        if opc == 1:
            print("\n--DDA--")
            dda()
        elif opc == 2:
            print("\n--Bressenham--")
            bress()
        elif opc == 0:
            break
        else:
            print("Opción inválida\n")
