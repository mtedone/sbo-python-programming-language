import datetime


class Holding(object):
    def __init__(self, name, date, shares, price):
        if Holding.check_date(date):
            self._date = date
        self.name = name
        self.shares = shares
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected Float')
        self._price = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, newvalue):
        if Holding.check_date(newvalue):
            self._date = newvalue

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    # Internal methods
    @staticmethod
    def check_date(datevalue):
        try:
            do = datetime.datetime.strptime(datevalue, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError('Expected date string in format "yyyy-mm-dd" but was {}'.format(datevalue))

    # Meant for developers
    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)


import csv


class Portfolio(object):

    def __init__(self):
        self.holdings = []

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                self.holdings.append(h)
        return self

    def total_cost(self):
        return sum(h.shares * h.price for h in self.holdings)

    # These methods allow Portfolio to be used with some friendly list methods
    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, item):
        return self.holdings[item]

    def __iter__(self):
        return self.holdings.__iter__()


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)
    return portfolio
