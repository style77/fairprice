import unittest

from fairprice import FairPrice, strategy
from fairprice.strategy.country import Country
from fairprice.strategy.currency import Currency


class TestCPI(unittest.TestCase):
    USD_PRICE = 5
    COUNTRY = Country.POL  # patriotic
    ESTIMATED_PRICE = 6  # USD

    def setUp(self):
        self.fp = FairPrice(strategy=strategy.CPI, country=self.COUNTRY)

    def test_return_type(self):
        val = self.fp.balance(self.USD_PRICE)
        self.assertIsInstance(val.price, float)
        self.assertIsInstance(val.currency, Currency)

    def test_val_in_range(self):
        val = self.fp.balance(self.USD_PRICE)
        self.assertEqual(round(val.price), self.ESTIMATED_PRICE)
        self.assertEqual(val.currency, Currency.USD)

    def test_currency_conversion_without_key(self):
        with self.assertRaises(ValueError):
            self.fp.balance(self.USD_PRICE, Currency.PLN)
