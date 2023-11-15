import typing

import httpx

from fairprice.strategy.base import DataType, Price, Strategy
from fairprice.strategy.currency import Currency


class FixedPrice(Strategy):
    DATA_TYPE = DataType.JSON
    DATA = "https://api.freecurrencyapi.com/v1/latest"

    def __init__(self, **kwargs):
        if freecurrency_key := kwargs.get("freecurrency_key"):
            self.api_key = freecurrency_key
        else:
            raise ValueError("API key is required")

    def __get_fixed_rate(self, currency: Currency):
        response = httpx.get(
            self.DATA,
            params={
                "apikey": self.api_key,
                "base_currency": "USD",
                "currencies": currency.value.upper(),
            },
        )
        return response.json()["data"][currency.value.upper()]

    def calculate(self, price: float, currency: typing.Optional[Currency]):
        if not currency:
            raise ValueError("Currency not specified")

        value = price * self.__get_fixed_rate(currency)
        return Price(value, currency)
