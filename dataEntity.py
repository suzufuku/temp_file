import dataclasses
from decimal import Decimal
from typing import Optional


@dataclasses.dataclass
class DataEntity:
    number: int
    second_number: int
    third_number: int
    level: int
    name: str
    amount: Decimal = Decimal("0.00")
@dataclasses.dataclass
class OutPutEntity:
    number: int
    second_number: int
    third_number: int
    level: int
    amount: Decimal = Decimal("0.00")
