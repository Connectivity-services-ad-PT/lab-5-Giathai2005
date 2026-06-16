# Run Lab 05

## Start system
docker compose up -d --build

## Check services
- API: http://localhost:8000/health
- AI: http://localhost:9000/health
- DB: running postgres

## Stop system
docker compose down