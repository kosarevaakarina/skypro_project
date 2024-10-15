## Технологии
* Python
* Django
* PostgreSQL
## Сущности
* Категории
* Товары
* Заказы
* Пользователь

### Запуск проекта в Docker:
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.example:_
```
SECRET_KEY=

#Database
POSTGRES_DB=
POSTGRES_HOST=db
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=
```
_Для создания образа из Dockerfile и запуска контейнера запустить команду:_
```
docker-compose up --build
```
_или_
```
docker-compose up -d --build
```
_Второй вариант для запуска в фоновом режиме._
### Запуск приложения в локальной сети:
_Для запуска проекта необходимо клонировать репозиторий, создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv
```
```
source venv/bin/activate
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_
```
SECRET_KEY=

#Database
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_USER=
POSTGRES_PASSWORD=

```
_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для заполнения БД запустить команду:_
```
python3 manage.py fill
```
_Для создания администратора запустить команду:_
```
python3 manage.py createsuperuser
```
_Для запуска приложения:_
```
python3 manage.py runserver
```