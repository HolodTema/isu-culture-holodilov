from script import sum, divide, substract

def test_sum():
    a = 1
    b = 2
    expected = 3
    assert sum(a, b) == expected

def test_substract():
    a = 5
    b = 3
    expected = 2
    assert sum(a, b) == expected
    print("Test substract is passed")

def test_divide():
    a = 2
    b = 4
    expected = 0.5
    assert divide(a, b) == expected

def test_divide_zero():
    a = 2
    b = 0
    try:
        divide(a, b)
    except ValueError as e:
        print("Test (division by zero) is passed")

def test_divide_lists():
    try:
        divide([1, 2, 3], [4, 5, 6])
        print("Test (division lists) is failed")
    except:
        print("Test (divizion lists) is passed")

if __name__ == "__main__":
    test_sum()
    test_substract()
    test_divide()
    test_divide_zero()
    test_divide_lists()

