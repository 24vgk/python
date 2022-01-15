

def convert_time(duration: int) -> str:
    if duration < 60:
       s = duration
       return (f'{s} сек')
    elif duration < 3600:
       m = duration // 60
       s = duration % 60
       return (f'{m} мин {s} сек')
    elif duration < 86400:
       h = duration // 60 ** 2
       m = duration % 3600 // 60
       s = duration % 60
       return (f'{h} час {m} мин {s} сек')
    else:
       d = duration // 86400
       h = duration % 86400 // 3600
       m = duration % 86400 % 3600 // 60
       s = duration % 60
       return (f'{d} дн {h} час {m} мин {s} сек')


if __name__ == '__main__':
    duration = 400153
    result = convert_time(duration)
    print(result)
