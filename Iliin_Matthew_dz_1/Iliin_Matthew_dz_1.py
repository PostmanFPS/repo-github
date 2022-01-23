def convert_time(duration: int) -> str:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 86400 % 3600 % 60

    if duration >= 86400:
        time_interval= '{} ДН {} ЧАС {} MИH {} СЕК'.format(days, hours, minutes, seconds)
    elif duration >= 3600:
        time_interval= '{} ЧАС {} MИH {} СЕК'.format(hours, minutes, seconds)
    elif duration >= 60:
        time_interval = '{} MИH {} СЕК'.format (minutes, seconds)
    else:
        time_interval = '{} СЕК'.format(seconds)

    return time_interval

duration=400153
result = convert_time(duration)
print (result)