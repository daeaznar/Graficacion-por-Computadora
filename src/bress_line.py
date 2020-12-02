def linebress(xi, yi, xf, yf):
    dx = xf - xi
    dy = yf - yi
    dosdy = dy * 2
    dosdx = dx * 2
    dosdy_menos_dosdx = dosdy - dosdx
    abs_m = abs(dy / dx)
    pasos = max(abs(dx), abs(dy))



def main():
    xi = int(input("Ingresa Xi: "))
    yi = int(input("Ingresa Yi: "))
    xf = int(input("Ingresa Xf: "))
    yf = int(input("Ingresa Yf: "))

    linebress(xi, yi, xf, yf)


if __name__ == '__main__':
    main()
