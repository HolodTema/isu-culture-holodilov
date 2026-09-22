## pyproject.toml как замена для setup.py с 2022 года

### Недостаток setup.py - это простой python-файл, в нем может быть любой код

Это создает проблемы безопасности и сложности - прогер скачивает проект, запускает setup.py - а в 
нем может быть что угодно, надо проверять.

### pyproject.toml
pyproject.toml - декларативный конфиг проекта, содержит метаданные проекта, информацию о 
зависимостях и тд. 

Также там содержится инфа о системе сборки, в разделе build-system. Обычно система сборки - это 
setuptools, но можно указать poetry, flit etc.

Сейчас это стандарт для python-проектов.

### Пример pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "1.0.0"
description = "Мой замечательный пакет"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    {name = "Ваше Имя", email = "email@example.com"}
]
dependencies = [
    "requests>=2.28.0",
    "numpy>=1.21.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
]
```

### Как собрать проект с pyproject.toml

Пусть у нас есть проект с pyproject.toml - хотим собрать из него tar или .whl python-пакета.

Сначала через pip устанавливаем пакет build - эта либа читает pyproject.toml и собирает его,
используя указанную в файле систему сборки

```bash
pip install build

# далее собираем проект
python -m build
```

В папке dist появятся 2 файла .tar и .whl

### Причем build юзает изолированное окружение для сборки, чтобы не засорять pip list хост-ОС

### запуск проекта через editable install

Пусть мы написали либу с pyproject.toml и хотим проверить ее в другом нашем проекте.

Мы можем собрать либу через build, сделать pip install mylib, юзать нашу либу и тестить.

Но если мы хотим внести изменения в либу, нам придется заново пересобирать через build, 
заново делать pip install mylib и тд. Это неудобно.

editable install - когда мы собираем и устанавливаем библиотеку в систему, но pip запоминает, 
где лежат исходники библиотеки, следит за изменениями в .py-файлах либы и автоматически
их подхватывает. То есть получается что-то по типу hot reload при разработке сайта.

Для запуска editable install мы не юзаем build, мы сразу запускаем pip-команду:

```bash
cd mylib

pip install -e .
```

Однако, если мы добавим новую зависимость в pyproject.toml, изменим точки входа в секции
[project.scripts] и тд - придется перезапустить editable install для применения изменений.

### dev-dependencies в pyproject.toml

Можно указывать обычные и dev-зависимости

Чтобы запустить editable-install с dev-зависимостями, пишем:

```bash
pip install -e ".[dev]"
```


