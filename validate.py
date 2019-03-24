import datetime


class Typed(object):
    expected_type = object

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class CsvDate(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not check_date(value):
            raise ValueError('Expected date string in format "yyyy-mm-dd" but was {}'.format(value))
        instance.__dict__[self.name] = value


def check_date(datevalue):
    try:
        datetime.datetime.strptime(datevalue, '%Y-%m-%d')
        return True
    except ValueError:
        pass
