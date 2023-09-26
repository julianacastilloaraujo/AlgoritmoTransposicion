def cifrado_encriptacion():
    mensaje = input("ESCRIBE EL TEXTO: ").replace(" ", "").upper()
    clave = input("INGRESA LA PALABRA: ").upper()

    lista_num_clave = asignar_numeros_clave(clave)

    for i in range(len(clave)):
        print(clave[i], end=" ", flush=True)
    
    print()
    for i in range(len(clave)):
        print(str(lista_num_clave[i]), end=" ", flush=True)
    
    print()
    print("EL RESULTADO ES")
    print("---------------")

    letras_extra = len(mensaje) % len(clave)
    caracteres_dummy = len(clave) - letras_extra

    if letras_extra != 0:
        for i in range(caracteres_dummy):
            mensaje += "."

    num_filas = int(len(mensaje) / len(clave))
    matriz = [[0] * len(clave) for i in range(num_filas)]
    z = 0
    for i in range(num_filas):
        for j in range(len(clave)):
            matriz[i][j] = mensaje[z]
            z += 1

    for i in range(num_filas):
        for j in range(len(clave)):
            print(matriz[i][j], end=" ", flush=True)
        print()

    ubicacion_num = obtener_ubicacion_numero(clave, lista_num_clave)
    print(ubicacion_num)

    texto_cifrado = ""
    k = 0
    for i in range(num_filas):
        if k == len(clave):
            break
        else:
            d = int(ubicacion_num[k])

        for j in range(num_filas):
            texto_cifrado += matriz[j][d]
        k += 1

    print("Texto Cifrado: {}".format(texto_cifrado))


def obtener_ubicacion_numero(clave, lista_num_clave):
    ubicacion_num = ""
    for i in range(len(clave) + 1):
        for j in range(len(clave)):
            if lista_num_clave[j] == i:
                ubicacion_num += str(j)
    return ubicacion_num


def asignar_numeros_clave(clave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lista_num_clave = list(range(len(clave)))

    init = 0
    for i in range(len(alfabeto)):
        for j in range(len(clave)):
            if alfabeto[i] == clave[j]:
                init += 1
                lista_num_clave[j] = init
    return lista_num_clave


def cifrado_desencriptacion():
    mensaje = input("INGRESA EL TEXTO: ").replace(" ", "").upper()
    clave = input("INGRESA LA PALABRA: ").upper()
    lista_num_clave = asignar_numeros_clave(clave)

    num_filas = int(len(mensaje) / len(clave))

    ubicacion_num = obtener_ubicacion_numero(clave, lista_num_clave)

    matriz = [[0] * len(clave) for i in range(num_filas)]

    texto_plano = ""
    k = 0
    itr = 0

    for i in range(len(mensaje)):
        d = 0
        if k == len(clave):
            k = 0
        else:
            d = int(ubicacion_num[k])
        for j in range(num_filas):
            matriz[j][d] = mensaje[itr]
            itr += 1
        if itr == len(mensaje):
            break
        k += 1
    print()

    for i in range(num_filas):
        for j in range(len(clave)):
            texto_plano += str(matriz[i][j])

    print("EL TEXTO ES: " + texto_plano)


def main():
    eleccion = int(input("1. ENCRIPTAR\n2. DESENCRIPTAR\nSELECCIONA (1, 2): "))
    if eleccion == 1:
        print("ENCRIPTAR")
        cifrado_encriptacion()
    elif eleccion == 2:
        print("DESENCRIPTAR")
        cifrado_desencriptacion()
    else:
        print("INGRESASTE ALGO INVÁLIDO")

if __name__ == "__main__":
    main()
1