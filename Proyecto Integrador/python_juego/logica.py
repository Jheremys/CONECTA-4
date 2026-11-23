# Módulo de lógica base (Fase 3)

FILAS = 6
COLUMNAS = 7

def crear_tablero():
    #Inicializa la matriz de 6x7 con ceros (0: Vacía, 1: Jugador 1, 2: Jugador 2)
    tablero = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(0)
        tablero.append(fila)
    return tablero

def colocar_ficha(tablero, col, jugador):
    #Calcula la gravedad e inserta la ficha en la fila libre más baja
    if col < 0 or col >= COLUMNAS:
        return False, -1
    
    # Buscar la casilla vacía más profunda de la columna
    f = FILAS - 1
    while f >= 0 and tablero[f][col] != 0:
        f -= 1

    if f >= 0:
        tablero[f][col] = jugador
        return True, f  # Inserción exitosa
    
    return False, -1  # Columna llena

