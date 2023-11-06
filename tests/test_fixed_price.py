import math
import os
import unittest

import dotenv

from fairprice import FairPrice, strategy
from fairprice.strategy.base import Price
from fairprice.strategy.currency import Currency

dotenv.load_dotenv(".env")


class TestFixedPriceStrategy(unittest.TestCase):
    USD_PRICE = 5
    CURRENCY = Currency.PLN
    ESTIMATED_PRICE = 20

    def setUp(self) -> None:
        self.fp = FairPrice(
            strategy=strategy.FixedPrice,
            freecurrency_key=os.getenv("FREECURRENCYAPI_KEY"),
        )

    def test_create_obj_without_api_key(self):
        with self.assertRaises(ValueError):
            FairPrice(strategy=strategy.FixedPrice)

    def test_return_type(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertIsInstance(val, Price)
        self.assertIsInstance(val.price, float)
        self.assertIsInstance(val.currency, Currency)

    def test_val_in_range(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertEqual(math.floor(val.price), self.ESTIMATED_PRICE)
