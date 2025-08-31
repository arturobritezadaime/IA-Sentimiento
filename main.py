import google.generativeai as genai
import datetime
import re
from config import Config
from obtener_noticias_NEWSAPI import obtener_noticias_newsapi
from obtener_noticias_GNEWS import obtener_noticias_gnews

def guardar_analisis_en_archivo(empresa, prompt_completo, respuesta_gemini):
    """
    Guarda el prompt completo y la respuesta de Gemini en un archivo de texto con un
    nombre de archivo único basado en la empresa, fecha y hora.
    """
    # Eliminar caracteres no válidos para nombres de archivo
    nombre_empresa_limpio = re.sub(r'[^\w\s-]', '', empresa).strip().replace(' ', '_')
    
    # Generar la marca de tiempo para el nombre del archivo
    now = datetime.datetime.now()
    fecha_hora_str = now.strftime("%d-%m-%Y-%H_%Mhs")
    
    # Construir el nombre del archivo
    nombre_archivo = f"analisis_{nombre_empresa_limpio}_{fecha_hora_str}.txt"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("--- PROMPT ENVIADO A GEMINI ---\n\n")
            f.write(prompt_completo)
            f.write("\n\n--- RESPUESTA DE GEMINI ---\n\n")
            f.write(respuesta_gemini)
        print(f"✅ Análisis completado. Resultado guardado en {nombre_archivo}")
    except IOError as e:
        print(f"❌ Error al guardar el archivo: {e}")


def ejecutar_prompt_gemini(empresa, noticias):
    """
    Ejecuta el análisis en Gemini con el prompt definido.
    """
    genai.configure(api_key=Config.GEMINI_API_KEY)

    modelo = genai.GenerativeModel("gemini-2.5-flash")

    noticias_texto = "\n\n".join(
        [f"Título: {n['titulo']}\nContenido: {n['contenido'] or n['descripcion']}" for n in noticias]
    )

    prompt = f"""
        Analiza las 10 noticias más recientes sobre {empresa} y determina el sentimiento predominante (positivo, negativo, neutral).
        Evalúa cómo este sentimiento podría impactar el precio en el próximo mes e identifica riesgos potenciales.

        Noticias recientes:
        {noticias_texto}
        """

    respuesta = modelo.generate_content(prompt)
    return prompt, respuesta.text


if __name__ == "__main__":
    empresa = ""

    while not empresa.strip():
        empresa = input("Ingrese la empresa tecnológica a analizar: ").strip()

    # Obtener noticias de ambas fuentes
    noticias_newsapi = obtener_noticias_newsapi(empresa, max_noticias=5)
    noticias_gnews = obtener_noticias_gnews(empresa, max_noticias=5)

    todas_las_noticias = noticias_newsapi + noticias_gnews

    if not todas_las_noticias:
        print("No se encontraron noticias recientes. Intente con otra empresa.")
    else:
        print(f"\nSe encontraron {len(todas_las_noticias)} noticias sobre {empresa}. Ejecutando análisis en Gemini...\n")

        # Ahora la función ejecutar_prompt_gemini devuelve el prompt y la respuesta
        prompt_enviado, resultado = ejecutar_prompt_gemini(empresa, todas_las_noticias)

        # Llamar a la nueva función para guardar ambos en un archivo
        guardar_analisis_en_archivo(empresa, prompt_enviado, resultado)