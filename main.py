from utils.amadeus_scraper import buscar_vuelos_por_rango
from utils.mailer import enviar_correo

# Configuración general
origen = "BOG"
destino = "YUL"
fechas_ida = ["2025-07-28", "2025-07-29", "2025-07-30"]
fechas_regreso = ["2025-07-31", "2025-08-01", "2025-08-02"]
umbral_normal = 600
umbral_brutal = 350

# Buscar vuelos
print("🔎 Buscando vuelos de ida...")
vuelos_ida = buscar_vuelos_por_rango(origen, destino, fechas_ida)
print("🔎 Buscando vuelos de regreso...")
vuelos_regreso = buscar_vuelos_por_rango(destino, origen, fechas_regreso)

# Generar combinaciones de ida + regreso
print("🔗 Combinando vuelos ida + regreso...")
combinados = []
for ida in vuelos_ida:
    for vuelta in vuelos_regreso:
        precio_total = float(ida['precio']) + float(vuelta['precio'])
        combinados.append({
            'ida': ida,
            'regreso': vuelta,
            'precio_total': round(precio_total, 2)
        })

# Ordenar por precio total y tomar top 3
combinados.sort(key=lambda x: x['precio_total'])
top_combinados = combinados[:3]

# Preparar cuerpo del mensaje
mensaje = f"Top 3 combinaciones completas {origen} ⇄ {destino} ({fechas_ida[0]} - {fechas_regreso[-1]}):\n\n"
alerta_brutal = False

for combo in top_combinados:
    ida = combo['ida']
    vuelta = combo['regreso']
    mensaje += f"💼 Total: ${combo['precio_total']} USD\n"
    mensaje += f"   🛫 Ida: {ida['aerolinea']} {ida['vuelo']} ({ida['salida']} → {ida['llegada']}, {ida['duracion']}, {ida['escalas']})\n"
    mensaje += f"       Link: {ida['link']}\n"
    mensaje += f"   🛬 Regreso: {vuelta['aerolinea']} {vuelta['vuelo']} ({vuelta['salida']} → {vuelta['llegada']}, {vuelta['duracion']}, {vuelta['escalas']})\n"
    mensaje += f"       Link: {vuelta['link']}\n\n"
    if combo['precio_total'] < umbral_brutal:
        alerta_brutal = True

# Top 3 vuelos individuales de ida
mensaje += f"\nTop 3 solo IDA ({origen} → {destino}):\n\n"
vuelos_ida.sort(key=lambda x: float(x['precio']))
for vuelo in vuelos_ida[:3]:
    mensaje += f"{vuelo['aerolinea']} {vuelo['vuelo']}: ${vuelo['precio']} USD - {vuelo['salida']} → {vuelo['llegada']} ({vuelo['duracion']}, {vuelo['escalas']})\n"
    mensaje += f"Link: {vuelo['link']}\n\n"

# Top 3 vuelos individuales de regreso
mensaje += f"\nTop 3 solo REGRESO ({destino} → {origen}):\n\n"
vuelos_regreso.sort(key=lambda x: float(x['precio']))
for vuelo in vuelos_regreso[:3]:
    mensaje += f"{vuelo['aerolinea']} {vuelo['vuelo']}: ${vuelo['precio']} USD - {vuelo['salida']} → {vuelo['llegada']} ({vuelo['duracion']}, {vuelo['escalas']})\n"
    mensaje += f"Link: {vuelo['link']}\n\n"

# Enviar correo
asunto = "🛫 Vuelos BOG ⇄ YUL actualizados"
if alerta_brutal:
    asunto = "ALERTA, VUELOS ECONOMICOS A MONTREAL"

enviar_correo(asunto, mensaje)
