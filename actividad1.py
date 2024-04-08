import random
def pedirDim (): #funcion para pedir las dimenciones del tablero al usuario
    #pido la cantidad de filas al usuario asegurandome que el usuario compelta con un numero mayor a 1
    try:
        filas = int(input("ingresa el numero de filas del tablero: "))
    except:
        filas = int(input("no ingresaste un numero por favor intenta de nuevo: "))
    if(filas < 1):
        filas = int(input("el numero ingresado es menor a uno, intenta nuevamente: "))
    #pido la cantidad de columnas al usuario asegurandome que el usuario compelta con un numero mayor a 1
    try:
        columnas = int(input("ingresa el numero de columnas del tablero: "))
    except:
        columnas = int(input("no ingresaste un numero por favor intenta de nuevo: "))
    if(columnas < 1):
        columnas = int(input("el numero ingresado es menor a uno, intenta nuevamente: "))
    return [filas,columnas]
def ingresar (cordenadas):
    filas = cordenadas[0]
    columnas = cordenadas[1]
    tablero = [] # creo el tablero para cargar los numero
    for numDeFila in range(0,(filas)): # creo un bucle para iterar por las filas
        listaAux = []
        for numDeColumna in range(0,(columnas)): # creo un bucle para iterar por los elementos de cada sub lista
            try:
                numAux = int(input("dime el numero que se guardara en la fila: " + str(numDeFila) + " columna: " + str(numDeColumna) + " :"))
            except:
                numAux = int(input("no ingresaste un numero, intenta nuevamente: "))
            if(numAux < 1):
                numAux = int(input("el numero que ingresaste es menor a 1, intenta nuevamente: "))
            listaAux.append(numAux)
        tablero.append(listaAux)
    return tablero
def ponerBarco (tablero):
    # lo que hago con esta funcion es: elijo cordenadas aleatorias entre 0 y la cantidad de filas
    # elijo otra posicion aleatoria entre 0 y la cantidad de columnas
    # cambio el numero ingresado en esa posicion por la palabara "barco"
    tablero[random.randint(-1,len(tablero))-1][random.randint(-1,len(tablero[0]))-1] = "barco"
    return tablero
def pedirCordenadas (tablero,intentos):
    try:
        filas = int(input("ingresa un numero que indique la fila donde crees que se encuentra el barco: "))
    except:
        filas = int(input("no ingresaste un numero por favor intenta de nuevo: "))
    if(filas < 0 or filas > len(tablero)):
        intentos += 1
        print("as utilizado 1 intento, intentos actuales: " + str(intentos))
        filas = int(input("el numero ingresado es menor a uno o es mayor a la cantidad de filas, intenta nuevamente: "))
    
    try:
        columnas = int(input("ingresa un numero que indique la columna donde crees que se encuentra el barco: "))
    except:
        columnas = int(input("no ingresaste un numero por favor intenta de nuevo: "))
    if(columnas < 0 or columnas > len(tablero)):
        intentos += 1
        print("as utilizado 1 intento, intentos actuales: " + str(intentos))
        columnas = int(input("el numero ingresado es menor a uno o es mayor a la cantidad de columnas, intenta nuevamente: "))
    print("jugaste la posicion: " + str(filas) + " " + str(columnas))
    return [filas,columnas,intentos]
def jugar (tablero):

    print("dentro del tablero que creaste e puesto un barco, intenta encontrarlo")
    intentos = 0
    print("contare cuantos intentos utilisas")
    while True:
        intentos += 1
        datos = pedirCordenadas(tablero,intentos)
        if(tablero[int(datos[0])][datos[1]] == "barco"):
            print("¡¡¡FELICIDADES ENCONTRASTE EL BARCO!!!")
            print("te a tomado " + str(datos[2]) + " intentos")
            break
jugar(ponerBarco(ingresar(pedirDim())))
