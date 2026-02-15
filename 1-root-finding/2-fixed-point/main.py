''' Roberto Sanchez Santoyo 2177547
    Punto Fijo'''

import math

def f (x:float) -> float:
    return math.exp(x) - math.pi * x

def g (x:float) -> float:
    return math.exp(x) / math.pi

def punto_fijo(x0:float, tolerancia:float) -> float:
    print(f"{'I':<5}{'x_i':>16}{'xi+1':>20}{'Error':>16}")
    print("-" * 57)
    iteracion:int = 1
    x1:float = g(x0)
    error:float = abs(x1-x0)
    while error > tolerancia:
        print(f"{iteracion:<5}{x0:>16.9f}{x1:>20.9f}{error:>16.9e}")
        x0 = x1
        x1 = g(x0)
        error = abs((x1-x0)/x1)
        iteracion += 1
    return x1, iteracion

raiz, iteracion = punto_fijo(x0=0.6, tolerancia=0.000001)
print(f"\nRaíz aproximada: {raiz:.12f}  (iteraciones: {iteracion})")
