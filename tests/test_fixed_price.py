import math
import os
import unittest

import dotenv

from fairprice import FairPrice, strategy

dotenv.load_dotenv(".env")


class TestFixedPriceStrategy(unittest.TestCase):
    USD_PRICE = 5
    CURRENCY = "PLN"
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
        self.assertIsInstance(val, float)

    def test_val_in_range(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertEqual(math.floor(val), self.ESTIMATED_PRICE)
