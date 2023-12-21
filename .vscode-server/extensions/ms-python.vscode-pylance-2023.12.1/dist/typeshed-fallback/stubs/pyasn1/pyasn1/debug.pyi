import logging
from typing import TextIO

__all__ = ["Debug", "setLogger", "hexdump"]

class Printer:
    def __init__(
        self,
        logger: logging.Logger | None = None,
        handler: logging.StreamHandler[TextIO] | None = None,
        formatter: logging.Formatter | None = None,
    ) -> None: ...
    def __call__(self, msg) -> None: ...

class Debug:
    defaultPrinter: Printer
    def __init__(self, *flags, **options) -> None: ...
    def __call__(self, msg) -> None: ...
    def __and__(self, flag): ...
    def __rand__(self, flag): ...

def setLogger(userLogger) -> None: ...
def hexdump(octets): ...

class Scope:
    def __init__(self) -> None: ...
    def push(self, token) -> None: ...
    def pop(self): ...