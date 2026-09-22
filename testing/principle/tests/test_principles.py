from math_demo import (
    add,
    add_with_bug
)

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не их отсутвие 
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test addition is passed")

def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутвие 
    # то есть эта функция это ложноположительный тест, ибо ошибки не нашел
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    print("Test addition with bug is passed")
    # finally we found data that make test reliable
    # если бы мы написали строчку ниже, мы бы нашли баг этим тестом
    # assert add_with_bug(7, 6) == 13 # will fail here

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()

