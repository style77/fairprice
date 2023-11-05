from typing import Type

from fairprice.strategy.base import Strategy
from fairprice.strategy.currency import Currency


class FairPrice(object):
    def __init__(self, strategy: Type[Strategy]):
        self.strategy = strategy()

    def balance(self, price: float, currency: str):
        try:
            currency_obj = Currency(currency.strip().lower())
        except Exception:
            raise ValueError(f"No such currency as {currency}")

        return self.strategy.calculate(price, currency_obj)
