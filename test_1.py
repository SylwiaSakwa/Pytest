def funkcja_1(liczba):
    return liczba + 10

def test_funkcja_1():
    assert funkcja_1(5) == 2 #czy funkcja_1 o wartości 5 zwróci nam wartość 6?


def test_funkcja_2():
    assert funkcja_1(5) == 15
