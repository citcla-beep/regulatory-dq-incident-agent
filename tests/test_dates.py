from datetime import date

from generator.dates import get_quarter


def test_today():
    day = date.today()
    assert get_quarter(day) == 4


def test_last_day_of_march_is_first_quarter():
    day = date(2026, 3, 31)
    assert get_quarter(day) == 1


def test_first_day_of_april_is_second_quarter():
    day = date(2026, 4, 1)
    assert get_quarter(day) == 2


def test_first_day_of_year_is_first_quarter():
    day = date(2026, 1, 1)
    assert get_quarter(day) == 1


def test_last_day_of_year_is_fourth_quarter():
    day = date(2026, 12, 31)
    assert get_quarter(day) == 4
