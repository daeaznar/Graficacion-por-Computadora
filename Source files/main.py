import lineas
import circunf


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
            lineas.menu_lineas()
        elif opc == 2:
            print("\n---Circunferencias---")
            circunf.menu_circunf()
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


menu()
