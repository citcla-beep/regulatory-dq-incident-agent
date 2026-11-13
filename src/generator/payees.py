import random
from dataclasses import dataclass


countries = [
    "GB",
    "US",
    "FR",
    "DE",
    "ES",
    "JP",
    "DK",
    "IT",
    "SE",
    "NO",
    "CA",
    "CH",
    "NL",
    "AU",
    "BE",
    "IE",
    "PT",
    "CN",
    "SG",
]


@dataclass
class Payee:
    payee_id: str
    payee_name: str
    payee_country: str
    payee_account: str


def generate_payees(count: int, rng: random.Random) -> list[Payee]:
    """Return a list of synthetic payee"""
    payees = []
    for i in range(1, count + 1):
        country = rng.choice(countries)
        payee = Payee(
            payee_id=f"PAYEE-{i:06d}",
            payee_name=f"Payee {i:04d}",
            payee_country=country,
            payee_account=f"{country}{rng.randint(10000000000000, 99999999999999)}",
        )
        payees.append(payee)
    return payees
