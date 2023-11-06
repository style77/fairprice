from typing import Type

from fairprice.strategy.base import Price, Strategy


class FairPrice:
    def __init__(self, strategy: Type[Strategy], **kwargs):
        self.strategy = strategy(**kwargs)

    def balance(self, *args, **kwargs) -> Price:
        return self.strategy.calculate(*args, **kwargs)
