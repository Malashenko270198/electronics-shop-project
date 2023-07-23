import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

assert 10000 * Item.pay_rate == item1.price
assert item1.price == 10000

assert 20000 * Item.pay_rate == item2.price
assert item2.price == 20000
