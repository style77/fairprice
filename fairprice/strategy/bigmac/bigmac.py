# BigMac Inde is a strategy invented by The Economist to compare prices of
# Big Macs in different countries. It is based on the theory of
# purchasing-power parity (PPP) like all of the strategies included
# I just thought it would be fun to include it in this library.
import pathlib

import pandas as pd

from fairprice.strategy.base import DataType, Strategy
from fairprice.strategy.currency import Currency


# Dataset is updated till 2020, so data may be unaccurate.
# Feel free to contribute and update big mac prices in your country
class BigMac(Strategy):
    DATA_TYPE = DataType.FILE
    DATA = (pathlib.Path(__file__).parent / "big_mac_index.csv").__str__()

    def calculate(self, price: float, currency: Currency):
        df = pd.read_csv(self.DATA)
        df["date"] = pd.to_datetime(df["date"])
        latest_data = df[df["date"] == df["date"].max()]
        latest_data = latest_data[
            latest_data["currency_code"] == currency.value.upper()
        ]

        big_mac_idx = (
            latest_data["local_price"].values[0] /
            latest_data["dollar_price"].values[0]
        )
        return big_mac_idx * price
