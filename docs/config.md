# Документация по модулям config.py и graph.py

## config.py

Модуль для загрузки переменных окружения из .env файла.

### Основные переменные окружения:

#### Neo4j конфигурация
- `NEO4J_URI` - URI для подключения к Neo4j
- `NEO4J_USER` - Имя пользователя Neo4j
- `NEO4J_PASSWORD` - Пароль пользователя Neo4j
- `NEO4J_DB` - Имя базы данных Neo4j

#### Redis конфигурация
- `REDIS_HOST` - Хост Redis сервера
- `REDIS_PORT` - Порт Redis сервера

#### Конфигурация бота и изображений
- `BOT_TOKEN` - Токен для Telegram бота
- `TEMPLATE_IMAGE_FILENAME_SAVE` - Шаблон имени файла для сохранения изображений
- `TEMPLATE_IMAGE_FILENAME_GET` - Шаблон имени файла для получения изображений
- `NODES_GROUP_NAME` - Имя группы узлов
- `TEMPLATE_PANORAMA_IMAGE_FILENAME_SAVE` - Шаблон имени файла для сохранения панорамных изображений
- `PANORAMA_IMAGE_BUCKET` - Имя бакета для панорамных изображений

#### MinIO конфигурация
- `MINIO_ENDPOINT` - Эндпоинт MinIO сервера
- `MINIO_ACCESS_KEY` - Ключ доступа MinIO
- `MINIO_SECRET_KEY` - Секретный ключ MinIO
- `BUCKET_NAME` - Имя бакета

#### Pannellum конфигурация
- `PANNELUM_URL` - URL Pannellum сервера
- `PANNELUM_PORT` - Порт Pannellum сервера

#### Безопасность
- `ALLOWED_USERS` - Список ID пользователей, имеющих доступ к административным функциям бота
