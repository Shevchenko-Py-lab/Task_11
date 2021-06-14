class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, item):
        self._dict.setdefault(item.name, []).append(item)

class Equipment:
    def __init__(self, name, qty, year):
        self.name = name
        self.qty = qty
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.qty} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, qty, year):
        super().__init__(name, qty, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.qty} {self.year}'

    @staticmethod
    def short_description():
        return 'Принтер'


class Scanner(Equipment):
    def __init__(self, name, qty, year):
        super().__init__(name, qty, year)

    @staticmethod
    def short_description():
        return 'Сканер'


class Xerox(Equipment):  # так-то Xerox это название марки, а сам прибор назвается "копир", ну да ладно
    def __init__(self, name, qty, year):
        super().__init__(name, qty, year)

    @staticmethod
    def short_description():
        return 'Копир'


if __name__ == '__main__':
    warehouse = Warehouse()
    warehouse.add_to(Printer("XP-400", "Epson", 3, 2014))
    warehouse.add_to(Scanner("OKI", 1, 2013))
    warehouse.add_to(Xerox("Xerox", 1, 2013))
    print(warehouse._dict)


