#include "nodo.h"

// Declaración de funciones definidas en ranking.cpp
NodoPartida* cargarHistorial(const string& rutaArchivo);
void mostrarPartidasCargadas(NodoPartida* cabeza);
void liberarPartidas(NodoPartida*& cabeza);

int main() {
    cout << "Inicializando modulo C++ (Fase 3)..." << endl;

    // Cargar y mostrar la lista enlazada básica
    NodoPartida* listaPartidas = cargarHistorial("../python_juego/historial.csv");
    
    if (listaPartidas != nullptr) {
        mostrarPartidasCargadas(listaPartidas);
        liberarPartidas(listaPartidas);
    }

    return 0;
}