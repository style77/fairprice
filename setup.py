import pathlib

from setuptools import setup

cur = pathlib.Path(__file__).parent

README = (cur / "README.txt").read_text()

with (cur / "requirements.txt").open() as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='fairprice',
    version='0.1.0',
    description="Balance the price of your products",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Style77/fairprice",
    author="Joachim Hodana",
    author_email="stylek777@gmail.com",
    license="MIT",
    packages=['fairprice'],
    install_requires=REQUIREMENTS,
    python_requires='>=3.8',
)