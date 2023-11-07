def add(a, b):
    """
    Повертає результат додавання аргументів: a + b


    >>> add(1, 2)
    3
    >>> add(-1, 10)
    9
    >>> add('a', 'b')
    'ab'
    >>> add(1, '2')
    Traceback (most recent call last):
      File "test.py", line 17, in <module>
        add(1, '2')
      File "test.py", line 14, in add
        return a + b
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


def subtract(a, b):
    """
    Повертає результат віднімання b від a

    >>> subtract(2, 1)
    1
    >>> subtract(10, 10)
    0
    >>> subtract(7, 10)
    -3
    """
    return a - b