#ifndef NODO_H
#ifndef NODO_H_INCLUDED
#define NODO_H_INCLUDED

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

// 1. Estructura para almacenar cada línea/partida del archivo historial.csv
struct Partida {
    int id_partida;
    string jugador1;
    string jugador2;
    string ganador;
    int turnos_totales;
    string fecha;
};

// 2. Nodo de la Lista Enlazada Dinámica de Partidas
struct NodoPartida {
    Partida datos;
    NodoPartida* siguiente; // Puntero al siguiente nodo en la memoria RAM (Heap)
};

// 3. Nodo de la Lista Enlazada Dinámica para la Tabla de Ranking por Jugador
struct NodoRanking {
    string nombre_jugador;
    int victorias;
    int partidas_jugadas;
    double promedio_turnos;
    NodoRanking* siguiente;
};

#endif
#endif