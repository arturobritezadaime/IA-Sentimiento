import requests
from config import Config

def obtener_noticias_gnews(empresa, max_noticias=5, idioma="en"):
    """
    Obtiene noticias recientes desde la API GNews.
    """
    api_key = Config.GNEWS_API_KEY 
    url = f"https://gnews.io/api/v4/search?q={empresa}&lang={idioma}&max={max_noticias}&apikey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            articulos = data.get("articles", [])
            return [
                {
                    "titulo": art.get("title"),
                    "descripcion": art.get("description"),
                    "contenido": art.get("content"),
                    "url": art.get("url")
                }
                for art in articulos
            ]
        else:
            print(f"Error en GNews: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"Error al obtener noticias de GNews: {e}")
        return []

"""
# 🚀 TEST rápido si ejecutas este archivo directamente
if __name__ == "__main__":
    empresa = "Apple"
    noticias = obtener_noticias_gnews(empresa, max_noticias=3)

    if noticias:
        print(f"\n✅ Noticias encontradas para {empresa}:")
        for i, n in enumerate(noticias, 1):
            print(f"\n[{i}] {n['titulo']}")
            print(f"Descripción: {n['descripcion']}")
            print(f"URL: {n['url']}")
    else:
        print(f"\n⚠️ No se encontraron noticias para {empresa}")
"""