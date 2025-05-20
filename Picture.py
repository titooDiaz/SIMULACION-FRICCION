from PIL import Image, ImageDraw, ImageFont
import math

# Datos de imagen
WIDTH, HEIGHT = 500, 500
RAMP_LENGTH = 300
FRAMES = 30 
BG_COLOR = (255, 255, 255)
OBJ_COLOR = (30, 144, 255)
TEXT_COLOR = (0, 0, 0)
RAMP_COLOR = (139, 69, 19)

def crear_frame_rampa(posiciones, nombres, velocidades, titulo):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

    y_start = 50
    spacing_y = 60
    draw.text((10, 10), titulo, fill=TEXT_COLOR, font=font)
    radius = 10

    for i, d in enumerate(posiciones):
        y_base = y_start + i * spacing_y
        x0, y0 = 50, y_base
        x1 = x0 + RAMP_LENGTH * math.cos(velocidades[i]['angulo'])
        y1 = y0 + RAMP_LENGTH * math.sin(velocidades[i]['angulo'])
        
        draw.line([(x0, y0), (x1, y1)], fill=RAMP_COLOR, width=6)
        
        x_obj = x0 + d * math.cos(velocidades[i]['angulo'])
        y_obj = y0 + d * math.sin(velocidades[i]['angulo'])

        draw.ellipse([x_obj - radius, y_obj - radius, x_obj + radius, y_obj + radius], fill=OBJ_COLOR)

        draw.text((5, y0 - radius), nombres[i], fill=TEXT_COLOR, font=font)

        # ESta linea muestra la velcidad final en el gif
        v_text = f"vf={velocidades[i]['v']:.2f} m/s"
        draw.text((x1 + 10, y1 - 10), v_text, fill=TEXT_COLOR, font=font)

    return img

def generar_gif_rampa(nombre_gif, nombres, velocidades_info, titulo):
    frames = []
    posiciones = [0] * len(nombres)

    velocidad_px = [v['v'] * 10 for v in velocidades_info] # escalar visualizacion

    for frame_idx in range(FRAMES):
        for i in range(len(posiciones)):
            posiciones[i] += velocidad_px[i]
            if posiciones[i] > RAMP_LENGTH:
                posiciones[i] = RAMP_LENGTH

        img = crear_frame_rampa(posiciones, nombres, velocidades_info, titulo)
        frames.append(img)

    frames[0].save(
        nombre_gif,
        save_all=True,
        append_images=frames[1:],
        duration=60,
        loop=0
    )
    print(f"GIF guardado: {nombre_gif}")