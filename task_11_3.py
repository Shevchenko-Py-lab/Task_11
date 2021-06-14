class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(txt)


numbers_list = []
user_input = 0
while user_input != "stop":
    user_input = input("Введите число ")
    if not user_input.isdigit():
        OwnError("Вы ввели не число")
    else:
        numbers_list.append(user_input)
print(numbers_list)
