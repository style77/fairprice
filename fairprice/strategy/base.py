import typing
from abc import ABC, abstractmethod
from enum import Enum

from fairprice.strategy.currency import Currency


class DataType(Enum):
    JSON: str = "json"
    FILE: str = "file"


class Strategy(ABC):
    DATA_TYPE: typing.Optional[DataType] = None
    DATA: typing.Optional[str] = None

    @abstractmethod
    def calculate(self, price: float, currency: Currency):
        raise NotImplementedError