
from typing import Any


class Node():
    def __init__(self, data : Any = None,  next : 'Node' = None) -> None:
        self._data = None
        self._next = None

    @property
    def data(self):
        return self._data


    @data.setter
    def data(self, value : Any) -> None:
        self._data = value


    @property
    def next(self):
        return self._next


    @next.setter
    def data(self, node : 'Node') -> None:
        self._next = node

    def __str__(self) -> str:
        print(f"I have data : {self._data}")
        print(f"I have next node : {self._next}")