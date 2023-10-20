# Використовуємо офіційний образ PostgreSQL з Docker Hub
FROM postgres:latest

# Задаємо змінні оточення для налаштування бази даних
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=563421

# Запускаємо контейнер з PostgreSQL
CMD ["postgres"]
