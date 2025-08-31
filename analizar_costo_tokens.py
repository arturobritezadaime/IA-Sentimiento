import google.generativeai as genai
from config import Config

def analizar_costo_tokens():
    """
    Lee un archivo de texto, calcula los tokens de entrada y salida,
    y estima el costo total basado en los precios de Gemini 2.5 Flash.
    """
    # 1. Configurar la API de Gemini
    genai.configure(api_key=Config.GEMINI_API_KEY)
    
    # 2. Solicitar el nombre del archivo al usuario
    nombre_archivo = input("Ingrese el nombre del archivo .txt a analizar: ")
    
    try:
        # 3. Leer el contenido del archivo
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        # 4. Separar el prompt de entrada y la respuesta de salida
        partes = contenido.split("--- RESPUESTA DE GEMINI ---\n\n")
        if len(partes) != 2:
            print("❌ El formato del archivo no es el esperado. Asegúrese de que contenga el separador '--- RESPUESTA DE GEMINI ---'.")
            return
        
        prompt_enviado = partes[0].replace("--- PROMPT ENVIADO A GEMINI ---\n\n", "")
        respuesta_gemini = partes[1]

        # 5. Inicializar el modelo para contar tokens
        modelo = genai.GenerativeModel("gemini-2.5-flash")

        # 6. Contar tokens de entrada y salida
        tokens_entrada = modelo.count_tokens(prompt_enviado).total_tokens
        tokens_salida = modelo.count_tokens(respuesta_gemini).total_tokens

        # 7. Precios por millón de tokens (referencia https://ai.google.dev/gemini-api/docs/pricing?hl=es-419)
        PRECIO_ENTRADA_POR_MILLON = 0.30
        PRECIO_SALIDA_POR_MILLON = 2.50
        
        # 8. Calcular el costo
        costo_entrada = (tokens_entrada / 1_000_000) * PRECIO_ENTRADA_POR_MILLON
        costo_salida = (tokens_salida / 1_000_000) * PRECIO_SALIDA_POR_MILLON
        costo_total = costo_entrada + costo_salida

        # 9. Mostrar los resultados
        print("\n--- RESUMEN DE COSTOS ---")
        print(f"Tokens de entrada: {tokens_entrada}")
        print(f"Tokens de salida: {tokens_salida}")
        print(f"Costo de entrada: ${costo_entrada:.6f} USD")
        print(f"Costo de salida: ${costo_salida:.6f} USD")
        print(f"Costo total: ${costo_total:.6f} USD")

    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    analizar_costo_tokens()
    
    """Ejemplo de uso:
        Asegúrese de tener un archivo de texto con el formato correcto, EJEMPLO: analisis_google.txt 
         incluyendo las secciones de prompt y respuesta separadas por '--- RESPUESTA DE GEMINI ---'.
          
    --- RESUMEN DE COSTOS ---
Tokens de entrada: 809
Tokens de salida: 2316
Costo de entrada: $0.000243 USD
Costo de salida: $0.005790 USD
Costo total: $0.006033 USD