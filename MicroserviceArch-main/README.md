# MVC Restful API

FastAPI приложение с аутентификацией на основе JWT и использованием БД PostgreSQL.

## Технологический стек

- **Веб-фреймворк**: FastAPI
- **ORM**: SQLAlchemy 2.0 (Async)
- **Миграции**: Alembic
- **База данных**: PostgreSQL 16 
- **DevOps**: Docker Compose

## Возможности

- Управление пользователями, статьями, комментариями
- Аутентификация и авторизация на основе JWT
- База данных PostgreSQL
- Docker

## Установка и запуск приложения

- **Настройка переменных окружения**
  
   ```bash
   copy env.example .env
   ```
   
- **Запуск приложения**
  
   ```bash
   docker-compose up -d
   ```
   
- **Остановка приложения**:
   ```bash
   docker-compose down
   ```

## Ссылки
- **Развернутое приложение**: https://microservicearch.onrender.com
- **Swagger UI**: https://microservicearch.onrender.com/docs
