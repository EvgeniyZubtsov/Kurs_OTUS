# -*- coding: utf-8 -*-
from OTUS.Kurs_OTUS.Home2.src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, side):
        if type(side) not in [int, float]:
            raise ValueError("Некорректные данные")
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4
