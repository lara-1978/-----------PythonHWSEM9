# Задача 4. Кэширование для ускорения вычислений
# Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
# результаты вызова функции и, при повторном вызове с теми же аргументами, возвращает сохранённый результат.
# Примените его к рекурсивной функции вычисления чисел Фибоначчи.
# В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
# если такие аргументы уже использовались, должен вернуть сохранённый результат вместо запуска расчёта.

import csv
from functools import  cache


def cache_decorator(func):
    cache = {}

    def wrapper(number):
        if number in cache:
            return cache[number]

        result = func(number)
        cache[number] = result
        return result

    return wrapper

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
print(fibonacci(10))  # результат будет вычислен и закэширован
print(fibonacci(10))  # результат будет возвращен из кэша
print(fibonacci(5))   # результат будет вычислен и закэширован


## пример по решению таких задач
"""def cache_decorator(function): 
    cache = {} 
    def wrapper(*args, **kwargs): 
        if args in cache: 
            return cache[args] 
        else: 
            result = function(*args, **kwargs) 
            cache[args] = result 
            return result 
    return wrapper """