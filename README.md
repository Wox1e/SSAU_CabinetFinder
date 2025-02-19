# Навигационный Telegram бот

## Описание
Административный Telegram бот для поиска кабинетов в корпусах Самарского университета.

## Основные возможности
- Создание точек с изображениями ориентиров
- Добавление панорамных изображений к точкам
- Создание связей между точками
- Построение маршрутов
- Просмотр списка всех точек
- Управление таблицей соответствия ID

## Технологии
- Python
- Neo4j (графовая база данных)
- Redis (хранение таблицы ID)
- MinIO (хранение изображений)
- Telegram Bot API

## Установка и настройка
"
1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Настройте переменные окружения в `.env-default` и переименуйте в `.env`
4. Отредактируйте ALLOWED_USERS в src/config.py (список ID пользователей, имеющих доступ к боту)
4. Запустите бота: `python bot.py`
"

## Документация
Подробная документация доступна в директории `docs/`:
- [Конфигурация](docs/config.md)
- [Работа с графовой БД](docs/graph.md)
- [Основная документация](docs/main.md)

## Безопасность
- Доступ ограничен списком разрешенных пользователей
- Проверка прав доступа для всех команд

## Обработка ошибок
Реализована система обработки ошибок с различными кодами для разных типов проблем. Подробности в документации.
