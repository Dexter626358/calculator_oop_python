class Complex1:
    def __init__(self, real, imag):
        self.re = real
        self.im = imag

    def __add__(self, o):
        return Complex1(self.re+o.re, self.im+o.im)

    def __sub__(self, o):
        return Complex1(self.re-o.re, self.im-o.im)

    def __mul__(self, o):
        return Complex1(self.re*o.re-self.im*o.im, self.re * o.im + self.im * o.re)

    def __truediv__(self, o):
        m = o.re * o.re + o.im * o.im
        return Complex1((self.re * o.re + self.im * o.im)/m, (self.im * o.re - self.re * o.im)/m)

    def __str__(self):
        if self.im == 0:
            return '%.2f' % self.re
        if self.re == 0:
            return '%.2fi' % self.im
        if self.im < 0:
            return '%.2f - %.2fi' % (self.re, -self.im)
        else:
            return '%.2f + %.2fi' % (self.re, self.im)


def solve(comp1, comp2):
   print(comp1 + comp2)
   print(comp1 - comp2)
   print(comp1 * comp2)
   print(comp1 / comp2)


