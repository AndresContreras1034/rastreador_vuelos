import requests
from datetime import datetime

# Credenciales de prueba
CLIENT_ID = "clienid"
CLIENT_SECRET = "CLIENTSECRET"
BASE_URL = "https://test.api.amadeus.com"


def obtener_token():
    url = f"{BASE_URL}/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


def generar_links(origen, destino, fecha):
    fecha_formateada = fecha.replace("-", "")[-6:]  # yymmdd
    fecha_google = fecha
    return {
        "skyscanner": f"https://www.skyscanner.com/transport/flights/{origen.lower()}/{destino.lower()}/{fecha_formateada}/",
        "kayak": f"https://www.kayak.com/flights/{origen}-{destino}/{fecha}",
        "google": f"https://www.google.com/flights?hl=en#flt={origen}.{destino}.{fecha_google}"
    }


def buscar_vuelos_por_fecha(origen, destino, fecha, adultos=1, moneda="USD", max_resultados=10):
    token = obtener_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": origen,
        "destinationLocationCode": destino,
        "departureDate": fecha,
        "adults": adultos,
        "currencyCode": moneda,
        "max": max_resultados
    }
    url = f"{BASE_URL}/v2/shopping/flight-offers"
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    vuelos = response.json().get("data", [])
    resultados = []
    seen = set()

    for vuelo in vuelos:
        itinerario = vuelo["itineraries"][0]
        segmentos = itinerario["segments"]
        primer_segmento = segmentos[0]
        ultimo_segmento = segmentos[-1]

        salida = primer_segmento["departure"]["at"]
        llegada = ultimo_segmento["arrival"]["at"]
        salida = datetime.fromisoformat(salida).strftime("%Y-%m-%d %H:%M")
        llegada = datetime.fromisoformat(llegada).strftime("%Y-%m-%d %H:%M")
        duracion = itinerario["duration"].replace("PT", "").lower()
        escalas = len(segmentos) - 1
        aerolinea = vuelo["validatingAirlineCodes"][0]
        precio = vuelo["price"]["total"]
        codigo_vuelo = segmentos[0]["carrierCode"] + segmentos[0]["number"]

        id_unico = f"{codigo_vuelo}_{salida}_{precio}"
        if id_unico in seen:
            continue
        seen.add(id_unico)

        enlaces = generar_links(origen, destino, fecha)

        resultados.append({
            "aerolinea": aerolinea,
            "vuelo": codigo_vuelo,
            "precio": precio,
            "salida": salida,
            "llegada": llegada,
            "duracion": duracion,
            "escalas": f"{escalas} escala{'s' if escalas != 1 else ''}",
            "link": enlaces["skyscanner"],  # Principal
            "link_kayak": enlaces["kayak"],
            "link_google": enlaces["google"]
        })

    return resultados


def buscar_vuelos_por_rango(origen, destino, fechas):
    resultados = []
    for fecha in fechas:
        try:
            vuelos = buscar_vuelos_por_fecha(origen, destino, fecha)
            resultados.extend(vuelos)
        except Exception as e:
            print(f"❌ Error buscando en {fecha}: {e}")
    return resultados