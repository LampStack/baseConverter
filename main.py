class InvalidBaseRange(Exception):
    pass

class BaseConverter():
    def __init__(self) -> None:
        pass
    def convert(self, number, BaseIs, toBase):
        if BaseIs not in range(2, 31) or toBase not in range(2, 21):
            raise InvalidBaseRange('You should choose a number bitween 1-30 !')
        else:
            if BaseIs == 10:
                return self.toAnyBase(number, toBase)
            else:
                number = self.toBaseTen(number, BaseIs)
                return self.toAnyBase(number, toBase)

    def toBaseTen(self, number, BaseIs):
        baseTen = 0
        num = str(number)
        for i in range(len(num)):
            baseTen += BaseIs ** (len(num) - 1 - i)  * int(num[i], 36)
        return baseTen
    def toAnyBase(self, number, toBase):
        __bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if number < toBase:
            return __bases[number]
        else:
            return self.toAnyBase(number // toBase, toBase) + __bases[number % toBase]

app = BaseConverter()
result = app.convert(1519, 10, 2)
print(result)
