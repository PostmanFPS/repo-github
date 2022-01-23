def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    a = ("Процент")
    b = ("Процента")
    c = ("Процентов")
    i = input("Введите сколько у вас процентов: ")
    numbs = {11, 12, 13, 14}
    for i in range(100):
        i = i + 1
        if i in numbs:
            print(i, c)
        elif i % 10 == 1:
            print(i, a)
        elif i % 10 > 1 and i % 10 < 5:
            print(i, b)
        else:
            print(i, c)
    return 'верните отформатированную строку'


for n in range(1, 100):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))