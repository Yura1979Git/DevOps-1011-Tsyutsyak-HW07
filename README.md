## Develop. Docker-compose. REST API.

### Завдання 1 
1. Створити Dockerfile з Python application (Flask+Redis)
2. Запустити containers з Python app та Redis
3. Написати Docker-compose файл для запуску Python app та Redis
4. Додати ENV, LABELS, ARG до вашого Dockerfile
5. Додати у Docker-compose ENV для вашого Python app container
6. Додати у Docker-compose volume для збереження данних Redis між запусками
7. Перевірити доступність записаних ключів в середині Redis container

### Завдання 2 
1. Запустити цей проект через Docker-compose файл з healthcheck'ом через команду redis-cli ping
2. Запуск Python app зробити залежним від redis healthcheck
3. Обмежити через compose-файл  redis: RAM до 512 МБ и CPU до 0,5
4. Додати ENV, LABELS, ARG до вашого Dockerfile

Виконання завдання оформити у вигляді Pull Request з Dockerfile, Docker-compose та аплікейшном. Посилання на pull request розмістити у особовому кабінеті.

* За бажанням можна використовувати аплікейшн написаний на любій знайомій вам мові програмування.