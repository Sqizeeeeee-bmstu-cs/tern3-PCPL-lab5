import random
from collections.abc import Generator
from typing import Any

from myclass import Unique

def gen_random(num_count: int, begin: int, end: int) -> Generator[int, None, None]:

    for _ in range(num_count):

        yield random.randint(begin, end)


def f1(data: list[dict[str, Any]]) -> list[str]:

    return sorted(list(Unique((job['job-name'] for job in data), ignore_case=True)), key=str.lower)

def f2(data: list[str]) -> list[str]:

    return list(filter(lambda f: str(f).lower().startswith('программист'), data))

def f3(data: list[str]) -> list[str]:

    return list(map(lambda f: f + ' с опытом Python', data))
