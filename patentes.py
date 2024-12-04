from PIL import Image, ImageDraw, ImageFont
import random

# Función para generar un texto de patente
def generar_patente():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    parte1 = "".join(random.choices(letras, k=2))  # Dos letras
    parte2 = "".join(random.choices(numeros, k=3))  # Tres números
    parte3 = "".join(random.choices(letras, k=2))  # Dos letras
    return f"{parte1} {parte2} {parte3}"

# Función para generar la imagen de la patente
def generar_imagen_patente(patente, nombre_archivo="patente.png"):
    # Crear un lienzo en blanco
    ancho, alto = 480, 130  # Dimensiones aproximadas de la patente
    imagen = Image.new("RGB", (ancho, alto), "white")
    draw = ImageDraw.Draw(imagen)

    # Colores y estilos
    color_texto = "black"
    color_fondo_superior = (0, 51, 153)  # Azul oscuro
    fuente_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    fuente_texto = ImageFont.truetype(fuente_path, 60)
    fuente_superior = ImageFont.truetype(fuente_path, 16)

    # Dibujar el fondo superior
    draw.rectangle([0, 0, ancho, 35], fill=color_fondo_superior)
    draw.text((ancho//3.6, 10), "REPUBLICA ARGENTINA", fill="white", font=fuente_superior) # centrar mejor

    # Dibujar el texto de la patente
    w_texto, h_texto = draw.textbbox((0, 0), patente, font=fuente_texto)[2:]
    draw.text(((ancho - w_texto) / 2, (alto - h_texto) / 2 + 10), patente, fill=color_texto, font=fuente_texto)

    # Añadir borde negro
    draw.rectangle([0, 0, ancho -1, alto -1], outline="black", width=6)

    # Guardar la imagen
    imagen.save(nombre_archivo)
    print(f"Patente generada y guardada como {nombre_archivo}")

# Ejemplo de uso
if __name__ == "__main__":
    patente = generar_patente()
    print(f"Patente generada: {patente}")
    generar_imagen_patente(patente)
