


from typing import Any, Callable
from .manager import RequestManagerServer


class SyncBoxMeta(type):

    def __new__(cls, classname: str, bases: tuple, maindict: dict[str, Any]):
        for attrname, attr in maindict.items():
            if isinstance(attr, type(lambda: 0)) and not attrname.startswith("_"):
                ...
        return type(classname, bases, maindict)


class SyncBox(metaclass=SyncBoxMeta):

    def __init__(self, a, b):
        print(a, b)
        self.a, self.b = a, b

    def sync_function(self, a, b, c):
        print(a, b, c)


sb = SyncBox("Sync Box Instantiated", "0")

sb.sync_function("Sync Function called", "", "")