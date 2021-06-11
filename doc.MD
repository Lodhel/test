Для запуска проекта:

    docker-compose up -d --build

    миграции:
        docker-compose exec web sh
        alembic upgrade head

Для теста:

    относительный урл /api/check_url/
        POST
            тело запроса
                {
                    "url": "http://rambler.ru"
                }
        GET
            тело запроса
                {
                    "id": 1
                }
