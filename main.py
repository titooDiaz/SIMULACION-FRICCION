import ModeloTeorico, Picture
import math
import os

def main():
    os.makedirs("gifs", exist_ok=True)

    # Fase 1
    angulo_rad_f1 = math.radians(50)
    nombres_f1 = ["Masa 1 (0.2kg)", "Masa 2 (2kg)"]
    velocidades_f1 = [
        {"v": ModeloTeorico.modelo_teorico(0.2, 0.02, angulo_rad_f1), "angulo": angulo_rad_f1},
        {"v": ModeloTeorico.modelo_teorico(2.0, 0.02, angulo_rad_f1), "angulo": angulo_rad_f1},
    ]
    Picture.generar_gif_rampa("gifs/fase1_rampa_abajo.gif", nombres_f1, velocidades_f1, "Fase 1: Masas distintas")

    # Fase 2
    nombres_f2 = ["Triángulo, Area (0.01m^2)", "Cuadrado Area (0.03m^2)"]
    velocidades_f2 = [
        {"v": ModeloTeorico.modelo_teorico(1.0, 0.01, angulo_rad_f1), "angulo": angulo_rad_f1},
        {"v": ModeloTeorico.modelo_teorico(1.0, 0.03, angulo_rad_f1), "angulo": angulo_rad_f1},
    ]
    Picture.generar_gif_rampa("gifs/fase2_rampa_abajo.gif", nombres_f2, velocidades_f2, "Fase 2: Formas y área contacto")

    # Fase 3
    nombres_f3 = ["40°", "50°", "60°"]
    angulos_rad = [math.radians(a) for a in [40, 50, 60]]
    velocidades_f3 = [{"v": ModeloTeorico.modelo_teorico(1.0, 0.02, a), "angulo": a} for a in angulos_rad]
    Picture.generar_gif_rampa("gifs/fase3_rampa_abajo.gif", nombres_f3, velocidades_f3, "Fase 3: Ángulos distintos")

    # Fase 4
    nombres_f4 = ["Madera lisa (u_k = 0.05)", "Plástico (u_k = 0.2)", "Lija (u_k = 0.4)"]
    fricciones = [0.05, 0.2, 0.4]
    velocidades_f4 = [
        {"v": ModeloTeorico.modelo_teorico(1.0, 0.02, angulo_rad_f1, mu), "angulo": angulo_rad_f1}
        for mu in fricciones
    ]
    Picture.generar_gif_rampa("gifs/fase4_rampa_abajo.gif", nombres_f4, velocidades_f4, "Fase 4: Fricción y superficies")

if __name__ == "__main__":
    main()
