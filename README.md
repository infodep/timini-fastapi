# Timinis egen FastAPI

Vi bruker FastAPI som har en grundig dokumentasjon [her](https://fastapi.tiangolo.com/)
**Merk: Selv om typedeklarasjoner ikke faktisk betyr noe i python, er FastAPI strenge på det, og vil validere mhp typehint. BRUK DEM**

## For å kjøre koden utenom docker

`uvicorn main:app --reload`

## OpenAPI

Med FastAPI følger OpenAPI, det vil si at API'en dokumenterer seg selv. Dokumentasjonen kan du finne her:
[swagger docs](http://127.0.0.1:8000/docs)  
[alternaltiv docs](http://127.0.0.1:8000/redoc)
'
TODO: https://auth0.com/docs/security/tokens/refresh-tokens/refresh-token-rotation
