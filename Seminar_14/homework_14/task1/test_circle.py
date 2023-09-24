import pytest
from circle import Circle, RadiusError


@pytest.fixture
def c1():
    return Circle(5)


@pytest.fixture
def c2():
    return Circle(10)


@pytest.fixture
def c3():
    return Circle(5)


def test_value():
    with pytest.raises(RadiusError):
        Circle(0)


def test_value_with_text():
    with pytest.raises(RadiusError,
        match=r'Значение радиуса должно быть положительное.Вы вводите: -1'):
        Circle(-1)


def test_calc_len_1(c1):
    assert c1.calc_len() == 31.41592653589793


def test_calc_len_2(c2):
    assert c2.calc_len() == 62.83185307179586


def test_calc_area_1(c1):
    assert c1.calc_area() == 78.53981633974483


def test_calc_area_2(c2):
    assert c2.calc_area() == 314.1592653589793


def test_str_1(c1):
    assert c1.__str__() == 'Круг с радиусом 5'


def test_str_2(c2):
    assert c2.__str__() == 'Круг с радиусом 10'


def test_eq_1(c1, c3):
    assert c1 == c3


def test_eq_2(c1, c2):
    assert c1 != c2


if __name__ == "__main__":
    pytest.main(['-v'])
