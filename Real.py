class Real:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return f"{self.x} + {self.y} = {self.x + self.y}"

    def __sub__(self):
        return f"{self.x} - {self.y} = {self.x - self.y}"

    def __mul__(self):
        return f"{self.x} * {self.y} = {self.x * self.y}"

    def __truediv__(self):
        if self.y != 0:
            return f"{self.x} / {self.y} = {self.x / self.y}"
        else:
            return "Деление на ноль"



