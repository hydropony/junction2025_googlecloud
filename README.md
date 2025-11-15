# junction2025_aimo-valio

## Local development

- **Warehouse DB**: use the shared compose setup under `warehouse-db/docker-compose.yml`.
  - Start: `cd warehouse-db && docker compose up -d`
  - Stop: `docker compose down` (from the same directory)
- **Order fulfilment service**: expects Postgres on `localhost:6000` with the credentials from `warehouse-db/docker-compose.yml`.
- No extra DB assets live under `order_fulfilment_service/src/main/resources` anymore; everything DB-related comes from `warehouse-db/`.