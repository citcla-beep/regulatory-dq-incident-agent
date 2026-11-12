from datetime import date

from generator.dates import get_quarter


def test_prova1():
    day = date(2026, 11, 12)
    assert get_quarter(day) == 4


def test_prova2():
    day = date(2026, 3, 31)
    assert get_quarter(day) == 1


def test_prova3():
    day = date(2026, 4, 1)
    assert get_quarter(day) == 2
