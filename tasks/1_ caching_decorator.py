from functools import wraps

def cache_decorator(cache_depth=10):
    """
    Декоратор для кэширования результатов выполнения функции с ограничением на глубину кэша.
    """
    def decorator(func):
        cache = {}           # Словарь для хранения кэшированных значений
        cache_order = []     # Список для отслеживания порядка добавления элементов

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем ключ для кэша
            if len(args) == 1 and not kwargs:
                key = args[0]
            else:
                key = (*args, *kwargs.items())

            if key in cache:
                print(f"(Возвращаем из кэша результат {cache[key]} для ключа: {key})")
                return cache[key]

            result = func(*args, **kwargs)

            # Удаляем самый старый элемент, если кэш превышает допустимую глубину
            if len(cache_order) >= cache_depth:
                old_key = cache_order.pop(0)
                del cache[old_key]
                print(f"(Кэш переполнен. Удаляем элемент с ключом: {old_key})")

            cache[key] = result
            cache_order.append(key)

            return result

        return wrapper

    return decorator


if __name__ == '__main__':
    # Тест 1: Работа с функцией, принимающей один аргумент
    @cache_decorator(3)
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    print("Тест 1")
    print(factorial(5))  # Вычисляем и добавляем в кэш
    print(factorial(4))  # Берем из кэша (так как factorial(4) вычислялся в процессе factorial(5))
    print(factorial(6))  # Пересчитываем, так как кэш глубиной 3 и часть результатов может быть удалена

    # Тест 2: Работа с функцией, принимающей несколько аргументов
    @cache_decorator(4)
    def power(base, exp):
        return base ** exp

    print("\n\nТест 2")
    print(power(2, 3))  # Вычисляем 2^3 и добавляем в кэш
    print(power(2, 3))  # Берем из кэша
    print(power(3, 2))  # Вычисляем 3^2 и добавляем в кэш
    print(power(2, 5))  # Добавляем новый результат в кэш
    print(power(3, 2))  # Берем из кэша
    print(power(2, 3))  # Берем из кэша
