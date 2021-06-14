class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(txt)


x = int(input("Введите делимое "))
y = int(input("Введите делитель "))
try:
    div = x / y
    if y == 0:
        raise OwnError("Some text")
except ZeroDivisionError:
    OwnError("Проверка собственного класса-исключения")

else:
    print(div)


