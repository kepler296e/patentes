import cv2
import numpy as np
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
    # Crear un lienzo en blanco (480x130 pixeles, fondo blanco)
    ancho, alto = 480, 130
    imagen = np.ones((alto, ancho, 3), dtype=np.uint8) * 255  # Fondo blanco

    # Colores
    color_texto = (0, 0, 0)  # Negro (BGR)
    color_fondo_superior = (0, 51, 153)  # Azul oscuro (BGR)

    # Cargar la fuente (asegurate de tener la fuente adecuada en tu sistema)
    # OpenCV usa fuentes predeterminadas o fuentes que tengas en tu sistema
    fuente_texto = cv2.FONT_HERSHEY_SIMPLEX
    fuente_superior = cv2.FONT_HERSHEY_SIMPLEX

    # Dibujar el fondo superior (rectángulo azul)
    cv2.rectangle(imagen, (0, 0), (ancho, 35), color_fondo_superior, -1)

    # Añadir texto "REPUBLICA ARGENTINA"
    cv2.putText(imagen, "REPUBLICA ARGENTINA", (ancho // 3, 10), fuente_superior, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # Calcular el tamaño del texto de la patente para centrarlo
    (w_texto, h_texto), _ = cv2.getTextSize(patente, fuente_texto, 2, 2)

    # Dibujar el texto de la patente centrado en la imagen
    x_texto = (ancho - w_texto) // 2
    y_texto = (alto + h_texto) // 2
    cv2.putText(imagen, patente, (x_texto, y_texto), fuente_texto, 2, color_texto, 2, cv2.LINE_AA)

    # Añadir borde negro
    cv2.rectangle(imagen, (0, 0), (ancho - 1, alto - 1), (0, 0, 0), 3)

    # Guardar la imagen
    cv2.imwrite(nombre_archivo, imagen)
    print(f"Patente generada y guardada como {nombre_archivo}")

# Ejemplo de uso
if __name__ == "__main__":
    patente = generar_patente()
    print(f"Patente generada: {patente}")
    generar_imagen_patente(patente)
