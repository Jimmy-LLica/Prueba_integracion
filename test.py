#!/usr/bin/env python3
"""
ARCHIVO DE PRUEBA PARA SISTEMAS DE SEGURIDAD
NO REALIZA NINGUNA ACCIÓN DAÑINA.
Simula un comportamiento de ransomware mostrando mensajes.
"""

import os
import sys

def main():
    print("⚠️ SIMULACIÓN DE RANSOMWARE - SOLO PARA PRUEBAS ⚠️")
    print("Este archivo no cifra ni modifica ningún dato.")
    print("Si tu extensión detecta esto como sospechoso, ¡funciona!")
    print("Ruta actual:", os.getcwd())
    print("Parámetros:", sys.argv)
    # Cadenas que suelen aparecer en malware real (para pruebas de patrones)
    sospechosas = [
        "ransomware", "encrypt", "decrypt", "bitcoin",
        "pay ransom", "files locked", "malware"
    ]
    print("Palabras clave de prueba:", sospechosas)

if __name__ == "__main__":
    main()
