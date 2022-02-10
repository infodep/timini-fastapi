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

**Kommentar: vi bruker ikke alembic nå fordi vi bruker SQLModel som ikke har dokumentasjon for hvordan man bruker det med alembic. [Så fort dokumentasjonen kommer](https://sqlmodel.tiangolo.com/advanced/) så må det fikses.**

Vi bruker alembic for migrations. Du må installere alembic på din egen pc for at migrasjonsskriptene skal komme på git. Det gjør du ved `pip install alembic` eller `pip install -r requirements.txt`. Siste alternaltiv gir deg alt av andre plugins også, som er fint for code completion.

<!-- Det går kanskje an å generere fra inne i docker men jeg fikk det ikke til å funke --iverks  -->

For å generere et skript skriver du i din egen terminal (i timini-fastapi mappen) `alembic revision --autogenerate -m <hva gjør skriptet>`.
For å kjøre skriptet går du inn i docker containeren som forklart tidligere og kjører `alembic upgrade head`. Her betyr head "nyeste versjon". Du kan også spesifisere en versjon med den rare strengen før understreken i filnavnet.

## Testing

Jeg implementerte testing fordi det gjorde utviklingen av kjernen mye enklere, og gjorde at jeg kunne være sikker på at tabellene og forholdene mellom de oppførte seg som det skulle.
Om testing gjør at det blir vanskeligere for dere å utvikle trenger dere ikke å gjøre det, men jeg tror det kommer til å hjelpe. Jeg kunne ingenting om det før jeg begynte, og tutorialen under er mer en grundig nok men tar allikevel bare maks 30 min å lese. I mange tilfeller holder det å ha lest [denne (som tar kanskje 5min.)](https://fastapi.tiangolo.com/tutorial/testing/)
Vi bruker pytest og FastApis(starlettes) testclient for testing. [Du kan lese om det her](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/).
