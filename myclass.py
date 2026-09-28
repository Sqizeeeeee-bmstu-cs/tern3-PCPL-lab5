from typing import Any
from collections.abc import Generator


class Unique(object):


    def __init__(self, items: list[Any] | Generator[Any], **kwargs):

        self.items = iter(items)

        self.ignore_case: bool = kwargs.get('ignore_case', False)

        self.seen: set[Any] = set()


    def __next__(self):

        while True:

            item = next(self.items)

            if self.ignore_case:

                if isinstance(item, str):

                    if item.lower() not in self.seen:

                        self.seen.add(item.lower())

                        return item

                else:

                    if item not in self.seen:

                        self.seen.add(item)

                        return item

            else:

                if item not in self.seen:

                    self.seen.add(item)

                    return item


    def __iter__(self):

        return self
