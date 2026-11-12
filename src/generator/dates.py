from datetime import date


def get_quarter(day: date) -> int:
    """Take in input a date and return the quarter from 1 to 4"""
    quarter = (day.month - 1) // 3 + 1
    return quarter
