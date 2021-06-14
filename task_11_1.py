# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_numb(cls, date_num):
        date_num = date_num.split("-")
        dat_list = []
        for date in date_num:
            dat_list.append(int(date))
        return dat_list

    @staticmethod
    def date_valid(date):
        date = date.split("-")
        date_list = []
        for da in date:
            date_list.append(int(da))
        for i in date_list:
            if date_list[0] < 0 or 31 < date_list[0]:
                # тут ещё можно было бы дописать условие на 30-31 дня и 28-29 для февраля
                return "wrong date"
            elif date_list[1] < 0 or 12 < date_list[1]:
                return "wrong date"
            elif date_list[2] < 0:
                return "wrong date"
            else:
                pass
        return date


if __name__ == '__main__':
    d = Date.date_numb('13-06-2021')
    print(d)
    v = Date.date_valid('32-06-2021')
    print(v)
    v2 = Date.date_valid('31-06-2021')
    print(v2)
