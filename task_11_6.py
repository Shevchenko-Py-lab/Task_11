class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptWarehouseError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferWarehouseError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddWarehouseError = AcceptWarehouseError


class ValidateEquipmentError(AppError):
    pass


class Warehouse:
    def __init__(self):
        self.__warehouse = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddWarehouseError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__warehouse.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferWarehouseError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__warehouse[idx]

        if item.department:
            raise TransferWarehouseError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__warehouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__warehouse[key]

    def __iter__(self):
        return self.__warehouse.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__warehouse)} устройств"


class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")

    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)


if __name__ == '__main__':
    warehouse = Warehouse()
    warehouse.add(Printer.create(4, vendor="Epson", model="XP-400"))
    warehouse.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    warehouse.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    warehouse.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(warehouse)

    for idx, itm in warehouse.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"{itm} зарезвервирован за отделом маркетинга")
        warehouse.transfer(idx, 'Отдел маркетинга')

    for idx, itm in warehouse.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(warehouse)
    print("Списано 1 устройство")
    del warehouse[0]
    print(warehouse)
