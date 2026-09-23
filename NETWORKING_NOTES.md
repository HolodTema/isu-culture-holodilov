## локальный запуск на 127.0.0.1 вообще без docker

когда мы вообще не используем docker и запускаем 3 сервиса  через poetry:

```bash
# первый терминал
cd product_service
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8001

# второй терминал
cd discount_service
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8002

# третий терминал
cd order_service
export PRODUCT_SERVICE_URL=http://127.0.0.1:8001
export DISCOUNT_SERVICE_URL=http://127.0.0.1:8002
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8003
```

то есть мы обязательно открыли 3 терминала и разнесли сервисы по 3 портам. В order_service мы 
передали через переменные окружения url до других сервисов

### случай, когда запустили 3 сервиса в контейнерах, но 127.0.0.1 не работает

Когда мы внутри контейнера, наш 127.0.0.1 это не localhost нашего ПК - это localhost внутри 
контейнера. 

Например, если мы в order-service передадим PRODUCT_SERVICE_URL=http://127.0.0.1:8001 и запустим
все 3 сервиса в docker-контейнерах, то:

1. order-service будет слать запросы на свой же localhost:8001 своего же контейнера, где 
ничего не запущено. И будет получать connection refused.

### случай, когда мы запустили 3 сервиса в контейнерах, и они успешно взаимодействуют через url с именами друг друга

Чтобы сервисы в контейнерах общались друг с другом, надо юзать общую docker-network и использовать
url по типу http://container-name:port-inside-this-container

По типу:

PRODUCT_SERVICE_URL=http://product-service:8000
DISCOUNT_SERVICE_URL=http://discount-service:8000

Важно, что порты именно те, что внутри контейнеров - то есть у всех 8000-порты.

то есть в чистом docker мы делаем так:

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

через docker-compose было бы все проще - все уже прописано в yaml-файле

```bash
docker compose up -d

curl -X POST http://127.0.0.1:8002/orders   -H "Content-Type: application/json"   -d '{"product_id":"notebook","quantity":12,"promocode":"STUDENT10"}'

docker compose down
```

### Случай, когда контейнеры общаются через host.docker.internal

у меня fedora42, тут с этим сложнее, чем в windows, как я понял

host.docker.internal нужен, когда часть сервисов в контейнерах, а часть работают без, на 
localhost нашего ПК. И надо их связать.

Пусть product-service и order-service в контейнерах.

Пусть discount-service запущен без контейнера на порту 8003

```bash
# в первом терминале
cd discount_service
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8003

# во втором терминале

docker run -d \
    --name product-service \
    --network service-net \
    product-service:latest

docker run -d \
    --name order-service \
    --network service-net \
    -p 8002:8000 \
    --add-host=host.docker.internal:host-gateway \
    -e PRODUCT_SERVICE_URL=http://product-service:8000 \
    -e DISCOUNT_SERVICE_URL=http://host.docker.internal:8003 \
    order-service:latest
```

