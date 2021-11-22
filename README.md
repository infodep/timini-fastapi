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

Vi bruker alembic for migrations. Du må installere alembic på din egen pc for at migrasjonsskriptene skal komme på git. Det gjør du ved `pip install alembic` eller `pip install -r requirements.txt`. Siste alternaltiv gir deg alt av andre plugins også, som er fint for code completion.

<!-- Det går kanskje an å generere fra inne i docker men jeg fikk det ikke til å funke --iverks  -->

For å generere et skript skriver du i din egen terminal (i timini-fastapi mappen) `alembic revision --autogenerate -m <hva gjør skriptet>`.
For å kjøre skriptet går du inn i docker containeren som forklart tidligere og kjører `alembic upgrade head`. Her betyr head "nyeste versjon". Du kan også spesifisere en versjon med den rare strengen før understreken i filnavnet.
