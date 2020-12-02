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
            print("\t---Lineas---")
            lineas.menu_lineas()
        elif opc == 2:
            print("\t---Circunferencias---")
            circunf.menu_circunf()
        elif opc == 3:
            print("\t---Elipses---")
        elif opc == 4:
            print("\t---Parábolas---")
        elif opc == 5:
            print("\t---Polígonos---")
        elif opc == 0:
            print("Cerrando Sistema... Hasta luego")
            break
        else:
            print("Opción inválida\n")


menu()
