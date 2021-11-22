# Timinis egen FastAPI

Vi bruker FastAPI som har en grundig dokumentasjon [her](https://fastapi.tiangolo.com/)
**Merk: Selv om typedeklarasjoner ikke faktisk betyr noe i python, er FastAPI strenge på det, og vil validere mhp typehint. BRUK DEM**

## Docker

Størsteparten av kommandoene gitt her skal kjøres inne i docker containeren. For å gå inn i den kan man enten bruke dockers egen GUI eller å kjøre kommandoen: `docker exec -it timini-fastapi-backend-1 /bin/bash`, som åpner bash i containeren. For å forlate skriv `exit`

## For å kjøre koden utenom docker

`uvicorn main:app --reload`

## OpenAPI

Med FastAPI følger OpenAPI, det vil si at API'en dokumenterer seg selv. Dokumentasjonen kan du finne her:
[swagger docs](http://127.0.0.1:8000/docs)  
[alternaltiv docs](http://127.0.0.1:8000/redoc)
'
TODO: `https://auth0.com/docs/security/tokens/refresh-tokens/refresh-token-rotation`

## Alembic

Vi bruker alembic for migrations.
