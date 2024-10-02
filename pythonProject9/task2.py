# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
# Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

from functools import wraps
from time import sleep
from typing import Callable, Any

def slowdown_2s(func:Callable[..., Any])-> Callable[...,Any]:
    @wraps(func)
    def wrapper(*args:Any, **kwargs:Any)-> Any:
        sleep(2)
        result = func(*args, **kwargs)  # Вызов  функции
        return result
    return wrapper

@slowdown_2s
def slowdown_test()-> None:
    print('<Тут что-то происходит...>')

@slowdown_2s
def another_function() -> None:
    print('Еще один тестовый вывод.')

if __name__ == "__main__":
    slowdown_test()
    another_function()













