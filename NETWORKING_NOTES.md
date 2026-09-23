## команды для создания образов, создания сети и запуска 3 контейнеров через чистый Docker

```bash
docker build -t product-service ./product-service

docker build -t discount-service ./discount-service

docker build -t order-service ./order-service

docker network create service-net

docker run -d --name product-service --network service-net product-service:latest

docker run -d --name discount-service --network service-net discount-service:latest

docker run -d --name order-service --network service-net -p 8002:8000 -e PRODUCT_SERVICE_URL=http://product-service:8000 -e DISCOUNT_SERVICE_URL=http://discount-service:8000 order-service:latest
```

далее можно зайти на нашей хост-ОС на http://127.0.0.1:8002/health - мы пробросили 8000-порт изнутри docker-контейнера order-service наружу как 8002-порт нашей хост-ОС

можно получить инфу о заказе с нашей хост-ОС:

```bash
curl -X POST http://127.0.0.1:8002/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id":"notebook","quantity":12,"promocode":"STUDENT10"}'
```

после можно удалить все контейнеры и сеть командой

```bash
docker rm -f order-service product-service discount-service
docker network rm service-net
```

## запускаем 3 контейнера через docker-compose

```bash

