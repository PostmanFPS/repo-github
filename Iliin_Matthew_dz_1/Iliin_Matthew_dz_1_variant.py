'''вводим переменную time и делаем запрос пользователю на ввод данных'''
time = int(input("Введите время в секундах "))

'''разбиваем от большего к меньшему дни, часы, минуты, секунды'''
days = time // 86400
hours = (time - days * 86400) // 3600
minutes = (time - (days * 86400 + hours * 3600)) // 60
seconds = time - (days * 86400 + hours * 3600 + minutes * 60)

'''выводим полученные данные'''
print(f"{days} ДН: {hours} ЧАС: {minutes} МИН: {seconds} СЕК")