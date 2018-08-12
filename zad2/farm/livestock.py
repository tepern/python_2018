def fib(n):
    """Вычисления числа Фибоначчи."""
    a = 2
    b = 3
    for __ in range(n):
        a, b = b, a + b
    return a


def bunnies(day):
    """
    Подсчёт выводка кроликов.
    Кролики размножаются раз в 10 дней в соответствии с числами Фибоначчи.
    """
    how_many_times = day // 10
    return fib(how_many_times)


def progression(k):
    """ Убывающая арифметическая прогрессия """
    y = 500
    x = 50
    for __ in range(k):
        y = y - x
    return y

def cow(day):
    milk = 0
    how_many_times = (day // 3) % 10
    if day % 3 == 0:
        milk = progression(how_many_times)
    return milk