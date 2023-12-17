# Документация по проекту


## 1. Активация виртуального окружения

Виртуальное окружение создается в папке, где будет реализован проект. Далее необходимо набрать команды на терминале для создания и активации:

```
python3 -m venv venv

. venv/bin/activate
```

## 2. Установка расширений

Для установки сразу нескольких расширений создается текстовый файл **req.txt** и все их наименования прописываются в данном файле. Далее через терминал производится их установка по команде:

```
pip install -r req.txt
```


## 3. Создание базы данных

Для этого необходимо зайти через терминал в PostgreSql и создать базу данных по следующей команде:

```
CREATE DATABASE <Наименование базы данных>
```

(в данном проекте название БД - dj_queryset)


## 4. Создание самого проекта

На терминале необходимо прописать следующую команду:

```
django-admin startproject config . 
```

После чего в папке нашего будет создан проект **config** со встроенными папками и файлами


## 5. Создания приложения ***Study***

Для создания новых приложений необходимо написать на терминале следующие команды:

```
python3 manage.py startapp Study

```

## 6. Загрузка приложения в файле settings.py

В данном файле необходимо добавить наши приложения в **INSTALLED_APPS**:
```python
INSTALLED_APPS = [
    ...
    'OnetoOneApp',
    'ManytoManyApp'
]
```

Также необходимо соединиться с базой данных, которую мы создали ранее:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_queryset',
        ...
        'HOST': 'localhost',
        'PORT':5432
    }
}

```
## 7. Создание моделей для приложения

Создание моделей для приложения **OnetoOneApp** и **ManytoManyApp** в файле models.py (Study/models.py):


**OnetoOneApp**


```python
from django.db import models

class CapitalCity(models.Model):
    cityname = models.CharField(max_length = 50)
    strength = models.IntegerField()
    
    def __str__(self) -> str:
        return self.cityname
    
class Country(models.Model):
    name = models.CharField(max_length = 100)
    language = models.CharField(max_length = 20)
    capital_city = models.OneToOneField(
        CapitalCity,
        on_delete = models.CASCADE,
        related_name = 'countries',
        related_query_name = 'country'
    )
    
    def __str__(self) -> str:
        return f'{self.name} : {self.capital_city}'
```

**ManytoManyApp**

```python
from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length = 100)
    singer_name = models.CharField(max_length = 100)
    listened = models.IntegerField()
    created_at = models.DateField()
    
class Listener(models.Model):
    account_name = models.CharField(max_length = 50)
    registration_date = models.DateField()
    songs = models.ManyToManyField(
        Song,
        related_name = 'Song',
        related_query_name = 'song'
    )
```


## 8. Миграции

Миграция является способом отслеживания изменений в структуре базы данных. В терминале необходимо будет прописать следующие команды:

```
python manage.py makemigrations
python manage.py migrate
```

## 9. Работа на интерактивной консоли

Необходимо прописать в терминале следующую команду:

```
python manage.py shell
```
таким образом мы запускаем интерактивную консоль, где будет прописываться CRUD функционал.


В первую очередь будет производится импорт моделей:
```
from OnetoOneApp.models import CapitalCity, Country
```

```
from ManytoMany.models import Song, Listener
```

##  Более подробную работу смотрите в файлах zametki_OnetoOne.txt и zametki_ManytoMany.txt
