import pygame

# Configuración de pantalla e interfaz
ANCHO = 700
ALTO = 700
FILAS = 6
COLUMNAS = 7
TAM_CASILLA = 80
INICIO_X = 70
INICIO_Y = 130

# Colores (RGB)
BLANCO = (255, 255, 255)
AZUL = (30, 90, 180)
ROJO = (230, 50, 50)
AMARILLO = (250, 210, 40)
NEGRO = (20, 20, 20)
VERDE = (40, 150, 80)

def inicializar_gui():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Conecta 4 - Fase 3")
    fuente = pygame.font.SysFont(None, 42)
    fuente_peq = pygame.font.SysFont(None, 30)
    return pantalla, fuente, fuente_peq

def dibujar_tablero(pantalla, fuente, fuente_peq, tablero, jugador_actual):
    pantalla.fill(BLANCO)

    # Título y estado del turno
    titulo = fuente.render("4 EN RAYA", True, NEGRO)
    pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 25))

    txt_turno = f"Turno: Jugador {jugador_actual}"
    color_turno = ROJO if jugador_actual == 1 else (180, 140, 0)
    texto = fuente_peq.render(txt_turno, True, color_turno)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 85))

    # Base azul del tablero
    pygame.draw.rect(
        pantalla, AZUL,
        (INICIO_X, INICIO_Y, COLUMNAS * TAM_CASILLA, FILAS * TAM_CASILLA)
    )

    # Dibujar círculos (0: Vacío/Blanco, 1: Rojo, 2: Amarillo)
    for i in range(FILAS):
        for j in range(COLUMNAS):
            x = INICIO_X + j * TAM_CASILLA + TAM_CASILLA // 2
            y = INICIO_Y + i * TAM_CASILLA + TAM_CASILLA // 2

            if tablero[i][j] == 1:
                color = ROJO
            elif tablero[i][j] == 2:
                color = AMARILLO
            else:
                color = BLANCO

            pygame.draw.circle(pantalla, color, (x, y), 31)

    # Botón Reiniciar
    pygame.draw.rect(pantalla, VERDE, (250, 635, 200, 40), border_radius=8)
    txt_btn = fuente_peq.render("REINICIAR", True, BLANCO)
    pantalla.blit(txt_btn, (ANCHO // 2 - txt_btn.get_width() // 2, 640))

def obtener_columna(pos_x):
    """Convierte la posición X del ratón a un índice de columna (0 a 6)"""
    if INICIO_X <= pos_x < INICIO_X + COLUMNAS * TAM_CASILLA:
        return (pos_x - INICIO_X) // TAM_CASILLA
    return -1