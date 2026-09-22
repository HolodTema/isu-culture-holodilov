from math_demo import (
    add,
    add_with_bug
)

# [DONE] Ранее тестирование позволяет съэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не их отсутвие 
# [DONE] Тесты не должны дублировать логику тестируемого кода 
# и не делать предположений о внутреннем устройстве кода
# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# [DONE] Тесты должны покрывать "кластеры" входных параметров

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

def test_addition_duplicate():
    # этот тест пытается угадать внутреннюю логику тестируемого кода - мы предполагаем, 
    # что под капотом юзается операция сложения, мы так и пишем 6 + 7
    # лучше было бы написать add(6, 7) == 13
    # так мы бы не пытались угадать внутреннюю логику
    assert add(6, 7) == 6 + 7
    print("Test duplicate-addition is passed")

def test_addition_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32):
            assert add(i, j) == i + j # violation of duplication 
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i - j
            assert add(i, -j) == i - j

def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("Test CLUSTERS PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill() # it will run too long...
    test_addition_clusters()

