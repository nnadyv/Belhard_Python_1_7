"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    n: int
    sequence: list

    def __init__(self, n):
        self.n = n
        self.sequence = [random.randint(-n, n) for a in range(n)]

    def generate(self, n=5):
        self.sequence = [random.randint(-n, n) for a in range(n)]
        return self.sequence

    def print_seq(self):
        return self.sequence
