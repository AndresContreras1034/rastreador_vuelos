
# ✈️ Amadeus Flight Alert Bot

Este proyecto automatiza la búsqueda de vuelos entre dos ciudades usando la API de Amadeus, analiza las combinaciones más económicas y envía por correo electrónico las mejores ofertas cada 12 horas. Ideal para encontrar vuelos baratos entre fechas específicas.

---

## 🚀 Características

- ✅ Consulta vuelos desde Amadeus API (modo sandbox o productivo)
- ✅ Combina vuelos de ida y regreso, y los ordena por precio
- ✅ Alerta si hay vuelos con precios muy bajos (por debajo de umbrales definidos)
- ✅ Envío automático de correos con las mejores combinaciones
- ✅ Formato legible para humanos
- ✅ Programado en Python con estructura modular
- ✅ Configurable fácilmente desde un solo archivo
- ✅ Ejecutable en **PythonAnywhere** u otro servidor con tareas programadas

---

## 📁 Estructura del proyecto

amadeus-alert/
│
├── main.py # Script principal que ejecuta todo
├── config.py # Fechas, umbrales y correos
├── utils/
│ ├── amadeus_scraper.py # Lógica de scraping de vuelos vía Amadeus
│ └── mailer.py # Envío de correos por SMTP
├── .env # (Opcional) Claves privadas si decides usar dotenv
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo

---

## ⚙️ Configuración inicial

1. **Clona el repositorio o sube los archivos a tu servidor**
   git clone https://github.com/tuusuario/amadeus-alert.git
   cd amadeus-alert

2. Crea un entorno virtual (opcional pero recomendado)
    -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Instala dependencias
   pip install -r requirements.txt

4. Llena los valores en config.py
   ORIGEN = "BOG"
   DESTINO = "YUL"
   FECHAS_IDA = ["2025-07-28", "2025-07-29"]
   FECHAS_REGRESO = ["2025-08-01", "2025-08-02"]
   UMBRAL_NORMAL = 600
   UMBRAL_BRUTAL = 350
   DESTINATARIOS = ["tunombre@correo.com"]

5. Llena tus credenciales en utils/mailer.py
   email_remitente = "tucorreo@gmail.com"
   password = "clave_de_aplicacion"

6. Llena tus credenciales Amadeus en utils/amadeus_scraper.py
   CLIENT_ID = "TU_CLIENT_ID"
   CLIENT_SECRET = "TU_CLIENT_SECRET"

🧪 Ejecución manual
    main.py

🕐 Automatización (con PythonAnywhere u otro)
   /home/tu_usuario/.virtualenvs/venv/bin/python3.10 /home/tu_usuario/amadeus-alert/main.py

Elige el intervalo de repetición (cada 12h, por ejemplo).

📬 Ejemplo de correo

🛫 Vuelos BOG ⇄ YUL actualizados

Top 3 combinaciones completas BOG ⇄ YUL (2025-07-28 - 2025-08-02):

💼 Total: $392.75 USD
   🛫 Ida: Avianca AV92 (2025-07-28 04:15 → 2025-07-28 10:40, 6h25m, 0 escalas)
       Link: https://www.skyscanner.com/...
   🛬 Regreso: Air Canada AC187 (2025-08-02 13:00 → 2025-08-02 19:30, 6h30m, 1 escala)
       Link: https://www.skyscanner.com/...

...

Top 3 solo IDA:
...

Top 3 solo REGRESO:
...

🔐 Seguridad
No subas tus claves API ni contraseñas a GitHub.

Usa .env y librerías como -dotenv si vas a compartir el proyecto públicamente.

Añade un .gitignore si usas Git:
.env
__pycache__/
*.pyc

📌 Dependencias
requests
-dotenv

```mermaid
graph TD
graph TD

Start([Start: Ejecutar alerta de vuelos])
Start --> Config[config.py]
Start --> Main[main.py]

subgraph Lógica de Búsqueda
  Main --> Scraper[amadeus_scraper.py]
  Scraper --> Token[obtener_token()]
  Scraper --> Buscar[buscar_vuelos_por_rango()]
end

subgraph Lógica de Alertas
  Main --> Procesamiento[Combina y filtra vuelos]
  Procesamiento --> Umbrales[Umbral normal / brutal]
end

subgraph Envío de Correo
  Main --> Mailer[mailer.py]
  Mailer --> SMTP[SMTP Gmail]
  SMTP --> CorreoUsuario[Destinatarios de config.py]
end

subgraph Automatización
  Tarea[Scheduled Task en PythonAnywhere] --> Main
end

CorreoUsuario --> End([Correo recibido con vuelos])
```
