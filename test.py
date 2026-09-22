from script import sum, divide

def test_sum():
    a = 1
    b = 2
    expected = 3
    assert sum(a, b) == expected

def test_divide():
    a = 2
    b = 4
    expected = 0.5
    assert divide(a, b) == expected

if __name__ == "__main__":
    test_sum()
    test_divide()

