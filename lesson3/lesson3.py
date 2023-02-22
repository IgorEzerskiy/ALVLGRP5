"""
1. Lowercase single letter: a, b
2. Lowercase/with underscores: some_func, database_name, counter
3. UPPERCASE SINGLE LETTER
4. UPPERCASE/with underscores
5. CamelCase
6. mixedCase
7. Camel_Case_With_Underscores

1, 2 Застосовується для назв змінних, методів, функцій.
АЛЕ!
Назви змінних, методів - min 3 символи. for i in range(10): ...
                                        for customer in cust_list: ...
Уникайте l, O, I.

3, 4 Використовуються для констант.

5 Назви класів. Якщо є абревіатура - пишеться вся великими літерами CustomHttpClient -> CustomHTTPClient

6 то про жаваскрипт - не використовуйте
7 жах, мєрхость - не використовуйте
"""
# from lesson2.dunders import Employee
from datetime import date
from datetime import timedelta


class IWillNotWork:
    pass


if __name__ == '__main__':
    kek = IWillNotWork()
