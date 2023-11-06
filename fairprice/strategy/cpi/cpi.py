import pathlib
import typing

import httpx
import pandas as pd

from fairprice.strategy.base import DataType, Price, Strategy
from fairprice.strategy.country import Country
from fairprice.strategy.currency import Currency


class CPI(Strategy):
    DATA_TYPE = DataType.FILE
    DATA = (pathlib.Path(__file__).parent / "cpidata.csv").__str__()
    __LATEST_YEAR = 2020

    def __init__(self, **kwargs):
        self.api_key = kwargs.get("freecurrencyapi_key", None)
        country = kwargs.get("country", None)
        if not country:
            raise ValueError("Country not specified")
        self.country = Country(country)

    def __get_fixed_rate(self, currency: Currency):
        if currency == Currency.USD:
            return 1
        url = f"https://freecurrencyapi.net/api/v2/latest?apikey={self.api_key}"
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()["data"][currency.value.upper()]
        raise ValueError("Invalid freecurrencyapi key")

    def __convert_currency(self, price: float, currency: Currency) -> float:
        rate = self.__get_fixed_rate(currency)
        return price * rate

    def calculate(self, price: float, currency: typing.Optional[Currency] = None):
        df = pd.read_csv(self.DATA)
        df = df[df["Country Code"] == self.country.name.upper()]
        cpi = None
        for year in range(self.__LATEST_YEAR, 1960, -1):
            cpi = df[str(year)].values[0]
            if cpi:
                break

        if not cpi:
            raise ValueError("CPI not found. Check if country is valid")

        value = (price * cpi) / 100
        if currency:
            value = self.__convert_currency(value, currency)
            return Price(value, currency)
        return Price(value, Currency("usd"))
