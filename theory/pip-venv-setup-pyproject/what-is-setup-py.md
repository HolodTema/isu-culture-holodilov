## Что такое setup.py

setup.py - скрипт на python в корне проекта, описывающий, как собирать, устанавливать и запускать
python-пакет нашего проекта.

Допустим, мы написали полезную либу на python и хотим поделиться с друзьями, опубликовать на PyPI 
и тд. 

Мы пишем setup.py, где указываем название, зависимости, версию, авторство и тд

### Пример

обычно юзается встроенный python-модуль setuptools и его функции setup(), find_packages()

find_packages() автоматически находит все пакеты в проекте

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "numpy",
    ],
    author="Ivan Ivanov",
    author_email="name@gmail.com",
    description="short description of the project",
    long_description=open("README.md").read()
    long_description_content_type="text/markdown"
)
```

### далее мы можем собрать наш проект как архив .tar в linux или .zip в windows:

```bash
python setup.py sdist
```

в папке dist появится .tar файл

### Можно собрать бинарную версию проекта:

```bash
python setup.py sdist bdist_wheel
```

в папке dist появится .whl файл

.whl - формат файла - готового к установке python-пакета. По сути это тот же zip-архив с 
пакетом внутри.

Можно установить через pip без сборки исходников.

### Пусть мы собрали наш проект в .tar через setup.py и передали другу - что дальше?

Друг должен распаковать архив, перейти в папку и выполнить

```bash
tar -xvf our_package.tar

cd our_package-1.0.0

python setup.py install
```

### Сейчас сборку проекта через setup.py считают уходящей в прошлое - на смену пришел pyproject.toml

хотя setup.py используется в куче старых проектов.

Помимо pyproject.toml есть куча инструментов по типу poetry, uv, conda

### setup.py используется именно для проектов-библиотек

Проект-библиотека, то есть проект, который в итоге собирается в python-модуль, который будут
устанавливать другие программисты.

Если мы пишем чисто python-приложение, то setup.py или pyproject.toml юзают больше для метаданных,
чтобы люди знали что за версия, что за название и тд. А на первый план выходит requirements.txt


