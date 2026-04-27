# 🚀 Flask + Nginx Dockerized Application

Демо приложение на базе **Flask**, проксируемое через **Nginx**, с поддержкой healthcheck и конфигурацией через переменные окружения.

---

## 📦 Структура проекта

```
.
│   docker-compose.yml
│   README.md
│
├───backend
│       .env
│       app.py
│       Dockerfile
│
└───nginx
        nginx.conf
```

---

## 🧩 Описание компонентов

### 🔹 Backend (Flask)

Http сервер на Flask с двумя эндпоинтами:

* `GET /` — возвращает сообщение из переменной окружения `MESSAGE`
* `GET /health` — endpoint для проверки состояния сервиса

---

### 🔹 Nginx

Используется как reverse proxy:

* Пробрасывает `/health`  и `/`.

---

### 🔹 Docker Compose

Оркестрирует два сервиса:

* `backend` — Flask приложение
* `nginx` — reverse proxy

Также:

* Настроен `healthcheck` для backend
* Используется общая сеть `bridge`

---

## ⚙️ Зависимости

### Требования:

* Docker ≥ 20.x
* Docker Compose ≥ 1.29 / Docker Compose Plugin

---

## 🔧 Переменные окружения

Файл: `backend/.env`

Пример:

```
MESSAGE=Hello world!
```

---

## 🐳 Сборка и запуск

### 1. Запуск приложения

```bash
docker compose up --build
```

---

### 2. Проверка работы

После запуска:

* Основной endpoint:

  ```
  http://localhost/
  ```

* Healthcheck:

  ```
  http://localhost/health
  ```

---

## 🌐 Сетевое взаимодействие

* Все сервисы находятся в сети `app`
* Nginx обращается к backend по имени сервиса:

```
http://backend:8080
```

---

## 🛠️ Возможные улучшения

* ✅ Добавить requirements.txt
* ✅ Добавить логирование
* ✅ Настроить HTTPS

---

## 🐞 Отладка

### Проверка логов:

```bash
docker-compose logs -f
```

### Проверка статуса контейнеров:

```bash
docker ps
```

---

## 🧪 Тестирование вручную

* curl http://localhost/

```
Hello from Effective Mobile!
```

* curl http://localhost/health

```
{
  "status": "healthy"
}
```
---
