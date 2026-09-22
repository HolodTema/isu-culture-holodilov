## venv - виртуальные окружения python

У python-разработчика без venv в списке установленных пакетов pip list начинается бардак -
пакеты могут быть несовместимы по версиям или в целом друг с другом.

Хороший тон - создавать для каждого проекта на python свой venv

### Создаем venv

```bash
# here .venv - directory with venv, it can have any name, like env, .venv, venv etc.
python3 -m venv .venv
```

в результате появляется папка .venv, внутри есть папки bin, include, lib, lib64 и файл-конфиг
pyvenv.cfg

Внутри конфига pyvenv.cfg указана версия python, где в ОС находится исполняемый файл python и тд

### Активируем venv

```bash
# linux
source ./.venv/bin/activate

# windows
env\Scripts\activate.bat
```

### Когда работа окончена, можно деактивировать venv

```bash
deactivate
```

### нужно добавлять папку c venv в .gitignore

