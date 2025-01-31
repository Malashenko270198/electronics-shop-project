import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) >= 10:
            self.__name = name
        else:
            name = name[:10]
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        filename = 'items.csv'
        with open(filename, newline='', encoding='windows-1251') as f:
            reader = csv.DictReader(f)
            for i in reader:
                Item(i['name'], i['price'], i['quantity'])


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


# filename = 'items.csv'
# with open(filename, newline='', encoding='windows-1251') as f:
#     reader = csv.reader(f)
#     for i in reader:



