import math

def modelo_teorico(masa, area, angulo_rad, friccion=0.1):
    g = 9.81
    d = 1.0 # --> suponemos una distancia de 1m
    mu_k = friccion
    a = g * (math.sin(angulo_rad) - mu_k * math.cos(angulo_rad))
    if a < 0:
        a = 0
    v = math.sqrt(2 * a * d) # --> CAlcular la velocidad
    return v # --> Devuelve la velocidad final