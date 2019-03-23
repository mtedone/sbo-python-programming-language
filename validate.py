import datetime


class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        instance.__dict__[self.name] = value


class Float(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        instance.__dict__[self.name] = value


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
