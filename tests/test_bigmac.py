import unittest

import dotenv

from fairprice import FairPrice, strategy
from fairprice.strategy.base import Price
from fairprice.strategy.currency import Currency

dotenv.load_dotenv(".env")


class TestBigMac(unittest.TestCase):
    USD_PRICE = 5
    CURRENCY = Currency.PLN  # patriotic
    ESTIMATED_PRICE = 20

    def setUp(self):
        self.fp = FairPrice(strategy=strategy.BigMac)

    def test_return_type(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertIsInstance(val, Price)
        self.assertIsInstance(val.price, float)
        self.assertIsInstance(val.currency, Currency)

    def test_val_in_range(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertEqual(round(val.price), self.ESTIMATED_PRICE)
