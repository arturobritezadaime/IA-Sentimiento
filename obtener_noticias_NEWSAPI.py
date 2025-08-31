from config import Config
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=Config.NEWSAPI_API_KEY)

def obtener_noticias_newsapi(empresa, max_noticias=5):
    """
    Obtiene noticias recientes de NewsAPI.
    """
    try:
        articulos = newsapi.get_everything(
            q=empresa,
            language='en',
            sort_by='publishedAt',
            page_size=max_noticias
        )
        return [
            {
                "titulo": art.get("title"),
                "descripcion": art.get("description"),
                "contenido": art.get("content"),
                "url": art.get("url")
            }
            for art in articulos.get("articles", [])
        ]
    except Exception as e:
        print(f"Error en NewsAPI: {e}")
        return []
        
"""        
# 🚀 TEST rápido si ejecutas este archivo directamente
if __name__ == "__main__":
    empresa = "Google"
    noticias = obtener_noticias_newsapi(empresa, max_noticias=2)

    if noticias:
        print(f"\n✅ Noticias encontradas para {empresa}:")
        for i, n in enumerate(noticias, 1):
            print(f"\n[{i}] {n['titulo']}")
            print(f"Descripción: {n['descripcion']}")
            print(f"URL: {n['url']}")
    else:
        print(f"\n⚠️ No se encontraron noticias para {empresa}")
"""