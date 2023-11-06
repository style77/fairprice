# fairprice

> python module to balance prices

[![PyPI](https://img.shields.io/pypi/v/fairprice.svg)](https://pypi.org/project/fairprice/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python module for balancing product prices. It takes USD price and uses various strategies of your choice to calculate fair price in other currencies.

## Installation

Pip is required to install the module. If you don't have pip installed, you can follow the instructions [here](https://pip.pypa.io/en/stable/installing/).

```sh
pip install fairprice
```

## Usage example

```python
from fairprice import FairPrice
from fairprice.strategy import BigMac

fp = FairPrice(strategy=BigMac)
fp.calculate(10, "PLN")
```

## Development setup

Clone the repository and install the requirements.

```sh
git clone https://github.com/Style77/fairprice.git
cd fairprice
pip install -r requirements.txt
```

## Contributing

1. Fork it (<https://github.com/Style77/fairprice/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new pull request
