# class to emulate floats and float-calculations with low precision
# (four significant digits) to demonstrate numeric effects
#
# see the file 'lpf_example.py' for concrete examples to use the class

prec = 4             # number of decimal digits (must be under 15)

class LPF(object):
    def __init__(self, value, full=None):
        if isinstance(value, LPF):
            self.value = value.value
            self.full = value.full
        else:
            self.value = float('%.*e' % (prec - 1, value))

            if full is None:
                full = self.value
            self.full = full

    def __str__(self):
        return str(self.value)

    def __format__(self, format_spec=''):
        x = float(self.value)
        return x.__format__(format_spec)

    def __repr__(self):
        return "LPF(%s, %r)" % (self, self.full)

    def error(self):
        ulp = float('1' + ('%.4e' % self.value)[-5:]) * 10 ** (1 - prec)
        return int(abs(self.value - self.full) / ulp)

    def __add__(self, other):
        other = LPF(other)
        return LPF(self.value + other.value, self.full + other.full)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = LPF(other)
        return LPF(self.value - other.value, self.full - other.full)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __mul__(self, other):
        other = LPF(other)
        return LPF(self.value * other.value, self.full * other.full)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = LPF(other)
        return LPF(self.value / other.value, self.full / other.full)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __neg__(self):
        return LPF(-self.value, -self.full)

    def __abs__(self):
        return LPF(abs(self.value), abs(self.full))

    def __pow__(self, other):
        other = LPF(other)
        return LPF(pow(self.value, other.value), pow(self.full, other.full))

    def __eq__(self, other):
        other = LPF(other)
        return self.value == other.value

    def __gt__(self, other):
        other = LPF(other)
        return self.value > other.value

    def __lt__(self, other):
        pther = LPF(other)
        return self.value < other.value

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)
