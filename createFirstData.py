import dataclasses
from decimal import Decimal
from typing import Optional
from dataEntity import DataEntity


def create_first_data(
    counter: int,
    second_counter: int,
    third_counter: int,
    level_counter: int,
    name_counter: int,
) -> DataEntity:
    return DataEntity(
        number=counter,
        second_number=second_counter,
        third_number=third_counter,
        level=level_counter,
        name=f"level{name_counter}",
        amount=Decimal("1.00")
    )
