def circ_dda():
    print("Esta es la circunferencia DDA")


def circ_pm():
    print("Esta es la cricunferencia por PM")


def menu_circunf():
    while True:
        print("¿Qué algoritmo quieres usar?\n"
              "1. DDA/Básico\n"
              "2. Punto Medio/Bressenham\n"
              "0. Regresar\n")
        opc = int(input("Opción: "))

        if opc == 1:
            print("\t--DDA--")
            circ_dda()
        elif opc == 2:
            print("\t--Punto Medio--")
            circ_pm()
        elif opc == 0:
            break
        else:
            print("Opción inválida\n")
