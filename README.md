# Server Monitor

Приложение для мониторинга состояния ресурсов серверов с использованием Python 3.12, Django 5 и MySQL 8.

---

## Описание

Приложение выполняет следующие задачи:
1. Периодически опрашивает эндпоинты на 30 машинах каждые 15 минут.
2. Сохраняет данные о CPU, памяти, диске и времени работы в базу данных MySQL.
3. Мониторит ресурсы и фиксирует инциденты при превышении заданных лимитов.
4. Отображает инциденты через веб-интерфейс с автоматическим обновлением.

---

## Технологии

- Python 3.12
- Django 5
- MySQL 8
- Docker

---

## Установка и запуск

### Требования

- Установите [Docker](https://docs.docker.com/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/).

### Шаги для запуска

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/server_monitoring/server_monitor.git
   cd server_monitor
   
2. Соберите и запустите контейнеры:
    ```bash
   docker-compose up --build
   
3. Если вы не используете Docker, установите зависимости с помощью команды:
    ```bash
   pip install -r requirements.txt

4. После запуска контейнеров выполните миграции:
   ```bash
   docker-compose exec web python manage.py migrate
   
5. Приложение будет доступно по адресу: http://localhost:8000.

## Использование

1. Веб-интерфейс
   * Перейдите по адресу http://localhost:8000/monitor/incidents/, чтобы просмотреть список инцидентов.
   * Данные обновляются автоматически каждые 5 секунд.

2. Аутентификация
   * Для доступа к веб-интерфейсу требуется аутентификация. По умолчанию используется простая проверка пользователя.
