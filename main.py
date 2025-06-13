import os
import sys
import argparse
import logging
from typing import List, Optional
import dataclasses
from decimal import Decimal
import time
from dataEntity import DataEntity, OutPutEntity
import createFirstData
import random


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--counter", type=int, default=1, help="number of times to run the loop"
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="output.log",
    )
    first_list = []
    logging.info("Start make dto")
    for i in range(args.counter):
        first_list.append(
            createFirstData.create_first_data(
                counter=random.randint(1, 3),
                second_counter=random.randint(1, 5),
                third_counter=random.randint(1, 10),
                level_counter=random.randint(1, 3),
                name_counter=i,
            )
        )
    logging.info("Entity created")
    logging.info("Start processing entities")

    end_map = {}
    for entity in first_list:
        key = composit_key(entity)
        if key in end_map:
            end_map[key].amount += entity.amount
        else:
            end_map[key] = set_data(entity)
    logging.info("Entities processed")
    logging.info(end_map)
    try:
        import psutil

        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / 1024 / 1024
        logging.info(f"Memory usage: {mem:.2f} MB")
    except ImportError:
        logging.warning(
            "psutilがインストールされていません。メモリ使用量は出力されません。"
        )


def composit_key(entity: DataEntity) -> str:
    if entity.level == 1:
        return f"{entity.number}"
    elif entity.level == 2:
        return f"{entity.number}-{entity.second_number}"
    else:
        return f"{entity.number}-{entity.second_number}-{entity.third_number}"


def set_data(entity: DataEntity) -> OutPutEntity:
    return OutPutEntity(
        number=entity.number,
        second_number=entity.second_number if entity.level > 1 else 0,
        third_number=entity.third_number if entity.level > 2 else 0,
        level=entity.level,
        amount=entity.amount,
    )


if __name__ == "__main__":
    main()
