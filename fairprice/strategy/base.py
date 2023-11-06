import typing
from abc import ABC, abstractmethod
from enum import Enum

from fairprice.strategy.currency import Currency


class DataType(Enum):
    JSON: str = "json"
    FILE: str = "file"


class Price(object):
    def __init__(self, price: float, currency: Currency):
        self.price = price
        self.currency = currency

    def __repr__(self) -> str:
        return f"{self.price} {self.currency.value.upper()}"


class Strategy(ABC):
    DATA_TYPE: typing.Optional[DataType] = None
    DATA: typing.Optional[str] = None

    @abstractmethod
    def calculate(self, price: float, currency: typing.Optional[Currency]) -> Price:
        raise NotImplementedError
