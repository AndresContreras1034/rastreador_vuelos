# Rastreador de Vuelos Bogotá–Montreal ✈️

Este script en Python rastrea vuelos económicos entre Bogotá y Montreal en fechas definidas, utilizando APIs como Amadeus y otras plataformas. Envía alertas por correo electrónico si encuentra precios por debajo de un umbral configurado por el usuario.

## Características
- Soporte para ida y vuelta
- Filtros por fecha y precio
- Notificaciones por correo
- Conversión COP ↔ USD
- Eliminación de vuelos duplicados

## Cómo usar
1. Clona el repositorio
2. Instala las dependencias con `pip install -r requirements.txt`
3. Configura tus credenciales en un archivo `.env`
4. Ejecuta: `python main.py`

---
```mermaid
---

graph TD

Start([Start: Build the web portfolio])
Start --> Files
Start --> Repo

subgraph Site Structure
  Files --> HTML[index.html]
  Files --> CSS[styles.css]
  Files --> JS[main.js]
end

Repo[Repository: AndresContreras1034.github.io]
Repo --> GitHubPages[GitHub Pages: Static hosting]
GitHubPages --> WebGitHub[andrescontreras1034.github.io]

subgraph Custom Domain
  DNS[DNS configured in Namecheap]
  CNAME[CNAME file with domain]
end

DNS --> GitHubPages
CNAME --> GitHubPages

GitHubPages --> WebFinal[andrescontreras1034.me]

subgraph Final Result
  WebFinal --> End([Website online and accessible])
end
---
