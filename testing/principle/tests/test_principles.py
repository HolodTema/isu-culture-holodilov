from math_demo import (
    add,
    add_with_bug,
    calculate_tax_bugged,
    calculate_tax
)

# [DONE] Ранее тестирование позволяет съэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не их отсутвие 
# [DONE] Тесты не должны дублировать логику тестируемого кода 
# и не делать предположений о внутреннем устройстве кода
# [DONE] Тесты не должны использовать ВСЕ наборы входных параметров
# [DONE] Тесты должны покрывать "кластеры" входных параметров
# [DONE] Тестовые функции покрывают логические блоки
# [DONE] Тесты должны обнаруживать новые ошибки (pescicide paradox)
# [DONE] Тесты покрывают как успешные так и ошибочные кейсы

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
    print("Test addition-clusters is passed")

def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Test addition-commutative is passed")

def test_tax_caculator_pesticide():
    # only integers don't allow some test cases 
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("Test TAX CALCULATOR PASSED")
    # float may give us test cases not available when using int
    #assert calculate_tax_bugged(2.34) == 0.35 # 0.351

def test_tax_caculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    print("Test UNBUGGED TAX CALCULATOR PASSED")

def test_negative_income():
    try:
        calculate_tax(-100)
        print("Test NEGATIVE INCOME FAILED")
    except ValueError as e:
        print("Test NEGATIVE INCOME PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill() # it will run too long...
    test_addition_clusters()
    test_addition_commutative()
    test_tax_calculator_pesticide()
    test_tax_calculator()
    test_negative_income()

