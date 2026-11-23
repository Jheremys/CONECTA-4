# 🎮 Proyecto Integrador: Conecta 4 (Python + C++)

**Universidad Internacional del Ecuador (UIDE)**  
**Carrera:** Ingeniería en Inteligencia Artificial (Primer Nivel)  
**Periodo Académico:** Septiembre 2026 – Febrero 2027  

## 👥 Integrantes del Equipo
* **Jeremy Simbaña**
* **Damián Lárraga**
* **Samuel Tipanta**

---

## 📌 Descripción del Proyecto
Este sistema es una implementación del clásico juego de lógica **Conecta 4** en modo local para dos jugadores. El proyecto cuenta con una arquitectura desacoplada compuesta por dos módulos independientes:
1. **Módulo de Juego (Python + Pygame):** Gestiona la interfaz gráfica (GUI), el tablero matricial de $6 \times 7$, la gravedad de las fichas y guarda los datos al finalizar cada partida.
2. **Módulo de Ranking (C++):** Lee el archivo compartido `historial.csv`, carga las partidas en una **Lista Enlazada Dinámica** en memoria RAM y procesa las estadísticas de rendimiento de los jugadores.

---

## 📂 Estructura del Repositorio

```text
ProyectoJuego/
├── python_juego/
│   ├── juego.py         # Punto de entrada principal en Python
│   ├── interfaz.py      # Renderizado visual y eventos en Pygame
│   ├── logica.py        # Control matricial y lógica base
│   └── historial.csv    # Archivo compartido de persistencia
├── cpp_datos/
│   ├── main.cpp         # Punto de entrada del módulo de datos
│   ├── ranking.cpp      # Lectura y gestión de memoria dinámica
│   └── nodo.h           # Declaración de estructuras (NodoPartida, NodoRanking)
├── LICENSE              # Licencia Open Source (MIT)
└── README.md            # Documentación general del proyecto
