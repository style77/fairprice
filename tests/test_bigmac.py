import os
import unittest

import dotenv

from fairprice import FairPrice, strategy

dotenv.load_dotenv(".env")


class TestBigMac(unittest.TestCase):
    USD_PRICE = 5
    CURRENCY = "PLN"  # patriotic
    ESTIMATED_PRICE = 20

    def setUp(self):
        self.fp = FairPrice(strategy=strategy.BigMac)

    def test_return_type(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertIsInstance(val, float)

    def test_val_in_range(self):
        val = self.fp.balance(self.USD_PRICE, self.CURRENCY)
        self.assertEqual(round(val), self.ESTIMATED_PRICE)
