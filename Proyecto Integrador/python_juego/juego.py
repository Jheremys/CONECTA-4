import sys
import pygame
from logica import crear_tablero, colocar_ficha
from interfaz import inicializar_gui, dibujar_tablero, obtener_columna

def main():
    pantalla, fuente, fuente_peq = inicializar_gui()
    tablero = crear_tablero()
    jugador_actual = 1
    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos

                # Detección del botón Reiniciar
                if 250 <= x <= 450 and 635 <= y <= 675:
                    tablero = crear_tablero()
                    jugador_actual = 1

                # Detección de clic en el tablero
                else:
                    col = obtener_columna(x)
                    if col != -1:
                        exito, fila = colocar_ficha(tablero, col, jugador_actual)
                        if exito:
                            # Cambio simple de turno 
                            jugador_actual = 2 if jugador_actual == 1 else 1

        dibujar_tablero(pantalla, fuente, fuente_peq, tablero, jugador_actual)
        pygame.display.update()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()