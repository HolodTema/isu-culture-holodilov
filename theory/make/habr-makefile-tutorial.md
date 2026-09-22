## Полное руководство по make и Makefile

### источник - habr https://habr.com/ru/articles/155201/

make - GNU-утилита для автоматической сборки программ.

Makefile - файл с набором правил для сборки проекта.

Основная идея make: отслеживать зависимости и пересобирать только изменившиеся файлы. Таким образом, сокращается время сборки проекта.

### Термины и концепции make

1. target - цель - файл, который надо создать

2. prerequisites - зависимости - файлы, от которых зависит цель

3. recipe - рецепт - команды для создания target

4. переменные хранят повторяющиеся значения

### Структура make-правила

```makefile
target: prerequisites
    recipe
    recipe
```

Причем recipe начинаются с таба, не с пробела!

### Пример простого Makefile

Пусть есть проект на С - это папка с такими файлами внутри:

```
./main.c
./utils.c
Makefile
```

Рассмотрим наш Makefile

Здесь есть разные target: program, main.o, utils.o, clean

Причем для создания одних target нужны другие target - это prerequisites

Есть специальный target clean - он очищает проект.

```makefile
program: main.o utils.o
    gcc -o program main.o utils.o


main.o: main.c
    gcc -c main.c


utils.o: utils.c
    gcc -c utils.c


clean:
    rm -f *.o program
```

Используем наш makefile

```bash
# собирает первый target в Makefile
# в нашем случае program
make

# выполняет clean - очистку проекта
make clean

# вызывает target по имени
# в нашем случае main.o
make main.o
```

### Комментарии в Makefile

```makefile
# single-line comment
```

### Переменные в Makefile

```makefile
# CC is C-compiler
CC = gcc
# CXX is C++ compiler
CXX = g++
# AR - archivator
AR = ar
# Some aliases for rm
RM = rm -rf
# CFLAGS is flags for C-compiler
CFLAGS = -Wall -Wextra -02
TARGET = program
SOURCES = main.c utils.c
# заменяем расширение .c на .o
OBJECTS = $(SOURCES:.c=.o)

# переменные можно юзать
$(CC) $(CFLAGS) -c $< -o $@

# здесь $< и $@ автоматические переменные
```

### Автоматические переменные в Makefile

```makefile
$@ # имя цели

$< # Имя первой зависимости

$^ # Список всех зависимостей

$? # Список зависимостей, измененных после цели

$* # Имя цели без суффикса
```

