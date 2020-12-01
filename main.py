def menu(opc):  # Dictionary Menú principal
    switch = {
        1: "Líneas",
        2: "Círculos/Circunferencias",
        3: "Elipses",
        4: "Parábolas",
        5: "Polígonos",
        0: "Salir",
    }
    return switch.get(opc, "Opción inválida")


print("Bienvenido, qué desea trazar?\n"  # Menú principal
      "1. Líneas\n"
      "2. Círculos/Circunferencias\n"
      "3. Elipses\n"
      "4. Parábolas\n"
      "5. Polígonos\n"
      "0. Salir")
opc = int(input("Opción: "))
print(menu(opc))

