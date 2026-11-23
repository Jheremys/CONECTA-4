#include "nodo.h"

// Función para cargar los datos del CSV a la lista enlazada dinámica
NodoPartida* cargarHistorial(const string& rutaArchivo) {
    ifstream archivo(rutaArchivo);
    if (!archivo.is_open()) {
        cout << "Error: No se pudo abrir el archivo " << rutaArchivo << endl;
        return nullptr;
    }

    string linea;
    getline(archivo, linea); // Omitir cabecera CSV

    NodoPartida* cabeza = nullptr;

    while (getline(archivo, linea)) {
        if (linea.empty()) continue;

        stringstream ss(linea);
        string temp;
        Partida p;

        getline(ss, temp, ','); p.id_partida = stoi(temp);
        getline(ss, p.jugador1, ',');
        getline(ss, p.jugador2, ',');
        getline(ss, p.ganador, ',');
        getline(ss, temp, ','); p.turnos_totales = stoi(temp);
        getline(ss, p.fecha, ',');

        // Inserción dinámica de nodo al inicio de la lista
        NodoPartida* nuevo = new NodoPartida;
        nuevo->datos = p;
        nuevo->siguiente = cabeza;
        cabeza = nuevo;
    }

    archivo.close();
    return cabeza;
}

// Imprime las partidas leídas sin ordenar (Fase 3)
void mostrarPartidasCargadas(NodoPartida* cabeza) {
    cout << "\n=== HISTORIAL DE PARTIDAS CARGADAS (FASE 3) ===\n";
    NodoPartida* aux = cabeza;
    while (aux != nullptr) {
        cout << "ID: " << aux->datos.id_partida 
             << " | J1: " << aux->datos.jugador1 
             << " | J2: " << aux->datos.jugador2 
             << " | Ganador: " << aux->datos.ganador 
             << " | Turnos: " << aux->datos.turnos_totales << endl;
        aux = aux->siguiente;
    }
}

// Liberación explícita de memoria dinámica
void liberarPartidas(NodoPartida*& cabeza) {
    while (cabeza != nullptr) {
        NodoPartida* temp = cabeza;
        cabeza = cabeza->siguiente;
        delete temp;
    }
}

