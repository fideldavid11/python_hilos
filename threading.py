import threading
import time
import random

# Función que imprimirá números en intervalos de tiempo aleatorios
def imprimir_numeros():
    # Ciclo infinito para imprimir números continuamente
    while True:
        numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
        print(f"Número generado: {numero}")
        time.sleep(random.uniform(0.5, 2))  # Espera un tiempo aleatorio entre 0.5 y 2 segundos

# Crear 5 hilos que ejecutarán la función imprimir_numeros
for i in range(5):
    t = threading.Thread(target=imprimir_numeros)
    t.daemon = True  # Hace que el hilo se detenga cuando el programa principal termine
    t.start()

# Mensaje para indicar que los hilos se están ejecutando
print("Los hilos están ejecutándose...")

# Esperar a que el usuario presione Enter para terminar el programa
input("Presiona Enter para terminar...\n")
