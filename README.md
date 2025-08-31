# 📊 Análisis de Noticias con Gemini

Este proyecto permite obtener noticias recientes de empresas tecnológicas utilizando **NewsAPI** y **GNews**, para luego analizarlas con **Google Gemini** y determinar el sentimiento predominante, junto con un posible impacto en el precio de la acción.

---

## 🚀 Características principales

- Obtención de noticias desde **dos fuentes** (NewsAPI y GNews).
- Análisis de sentimiento y riesgos usando **Gemini 2.5 Flash**.
- Guardado automático del **prompt** y la **respuesta del modelo** en archivos `.txt`.
- Utilidad adicional para calcular el **costo estimado en tokens** consumidos (`analizar_costo_tokens.py`).

---

## 📂 Estructura del proyecto

```
.
├── .gitignore                 # Archivos y carpetas ignoradas por Git
├── config.py                  # Configuración centralizada con variables de entorno
├── main.py                    # Script principal para ejecutar el análisis
├── obtener_noticias_GNEWS.py  # Módulo para consumir la API de GNews
├── obtener_noticias_NEWSAPI.py# Módulo para consumir la API de NewsAPI
├── analizar_costo_tokens.py   # Script para calcular el costo de tokens en Gemini
├── requirements.txt           # Dependencias del proyecto 
└── README.md                  # Documentación del proyecto
```

---

## ⚙️ Requisitos previos

1. **Python 3.10+**
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux / Mac
   venv\Scripts\activate    # En Windows
   ```
3. Instalar dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### Dependencias principales
- `google-generativeai`
- `python-dotenv`
- `requests`
- `newsapi-python`

---

## 🔑 Configuración de API Keys

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
FRED_API_KEY=tu_api_key_fred
NEWSAPI_API_KEY=tu_api_key_newsapi
GNEWS_API_KEY=tu_api_key_gnews
GEMINI_API_KEY=tu_api_key_gemini
EMAIL=tu_email_para_user_agent
```

---

## ▶️ Uso

### 1. Ejecutar el análisis principal
```bash
python main.py
```
El sistema pedirá el nombre de una **empresa tecnológica** y obtendrá las 10 noticias más recientes para analizar el **sentimiento predominante**.

El resultado se guardará en un archivo con el formato:
```
analisis_<empresa>_<fecha-hora>.txt
```

### 2. Calcular costo de tokens de un análisis
```bash
python analizar_costo_tokens.py
```
Este script solicitará un archivo `.txt` generado y estimará el costo en USD según el consumo de tokens.

---

## 🧑‍💻 Buenas prácticas aplicadas

- **Separación de responsabilidades** en módulos (`main`, `config`, `fuentes de noticias`, `análisis de costos`).
- **Uso de `.env`** para mantener seguras las credenciales y evitar exponer claves en el código.
- **Logs de error controlados** para facilitar debugging sin interrumpir la ejecución completa.
- **Compatibilidad multiplataforma** para nombres de archivo y ejecución.

---

## 📌 Próximas mejoras

- Soporte para múltiples idiomas en análisis de noticias.
- Exportación de resultados a formatos adicionales (CSV, JSON).

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT. Siéntete libre de usarlo y adaptarlo a tus necesidades.

##  Autor

Arturo Britez Adaime