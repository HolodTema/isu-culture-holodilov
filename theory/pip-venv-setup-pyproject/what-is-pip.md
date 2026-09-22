## pip - package installer for python

стандартный пакетный менеджер python, для установки и управления установленными сторонними
библиотеками на python.

При помощи pip можно ставить пакеты из PyPI - облачного репозитория с кучей python-модулей.

### Как работает команда pip install

Пишем pip install - pip обращается к PyPI и ищет там нужный пакет - загружает этот пакет и 
зависимости для него.

Далее загруженный пакет с зависимости можно установить глобально для всей ОС хоста, либо в 
виртуальное окружение, если оно активировано.

### Основные команды pip

```bash
# current pip version
pip --version

pip install package-name

pip uninstall package-name

# show all the installed modules
pip list

# show info about the package
pip show package-name

# show all the installed modules, but in format like in requirements.txt
pip freeze

# install all the packages from requirements.txt
pip install -r requirements.txt
```

### Работа с версиями пакетов через pip

```bash
# install package of certain version
pip install numpy=1.23.0

# update the package to the last version
pip install --upgrade pandas
```

Если мы находимся в venv и хотим создать requirements.txt из всех установленных в наш venv
пакетов, можно юзать unix-операторы управления stdout:

```bash
pip freeze > requirements.txt
```

### Подробнее о requirements.txt

В requirements.txt перечислены все зависимости проекта с версиями. Можно одной командой
установить все зависимости из этого файла, используя pip.

1. воспроизводимость. Коллега может склонировать репозиторий, запустить venv 
 и легко поставить те же зависимости что и у нас

2. изоляция проекта. requirements.txt + pip + venv = зависимости проекта не смешиваются с 
глобальными python-пакетами хост-ОС вне venv.

### Синтаксис requirements.txt

можно делать комментарии

можно указывать версии, диапазоны версий и тд

можно задавать маркировку, например standard у uvicorn

можно задавать какие-то переменные-маркеры-окружения по типу sys_platform

```
# основные зависимости
requests==2.31.0
flask>=2.2,<3.0
numpy~=1.26.0

# с extras
uvicorn[standard]==0.27.0

# с маркером окружения
pywin32==306; sys_platform == "win32"
importlib-metadata; python_version < "3.8"
```

### Часто requirements.txt разделяют на 3 файла для base, dev, prod

```
requirements/
├── base.txt
├── dev.txt
└── prod.txt
```

base.txt общие зависимости для dev и prod

dev.txt зависимости для разработки, их не будет на проде

prod.txt зависимости, которые работают только на проде

### файл constraints.txt в дополнение к requirements.txt

constraints.txt содержит ограничения для версий зависимостей из requirements.txt

Например

```
urllib3<2
```

используем 2 файла вместе:

```bash
pip install -r requirements.txt -c constraints.txt
```


