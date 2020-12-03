import bress_line
import dda_line
import dda_circ


def menu():
    print("Bienvenid@")
    while True:
        print("¿Qué desea trazar?\n"  # Menú principal
              "1. Líneas\n"
              "2. Circunferencias\n"
              "3. Elipses\n"
              "4. Parábolas\n"
              "5. Polígonos\n"
              "0. Salir\n")
        opc = int(input("Opción: "))

        if opc == 1:
            print("\n---Lineas---")
            menu_lineas()
        elif opc == 2:
            print("\n---Circunferencias---")
            menu_circ()
        elif opc == 3:
            print("\n---Elipses---")
        elif opc == 4:
            print("\n---Parábolas---")
        elif opc == 5:
            print("\n---Polígonos---")
        elif opc == 0:
            print("Cerrando Sistema... Hasta luego")
            break
        else:
            print("Opción inválida\n")


def menu_lineas():
    while True:
        print("¿Qué algoritmo quieres usar?\n"
              "1. DDA/Básica\n"
              "2. Punto Medio/Bressenham\n"
              "0. Regresar\n")
        opc = int(input("Opción: "))

        if opc == 1:
            print("\n--DDA--")
            dda_line.main()
        elif opc == 2:
            print("\n--Punto Medio - Bressenham--")
            bress_line.main()
        elif opc == 0:
            break
        else:
            print("Opción inválida\n")


def menu_circ():
    while True:
        print("¿Qué algoritmo quieres usar?\n"
              "1. DDA\n"
              "2. Bressenham\n"
              "0. Regresar\n")
        opc = int(input("Opción: "))

        if opc == 1:
            print("\n--DDA--")
            dda_circ.main()
        elif opc == 2:
            print("\n--Bressenham--")
            bress_line.main()
        elif opc == 0:
            break
        else:
            print("Opción inválida\n")


menu()
