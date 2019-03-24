from validate import Integer, Float, CsvDate, String


class Holding(object):
    shares = Integer('shares')
    price = Float('price')
    date = CsvDate('date')
    name = String('name')

    def __init__(self, name, date, shares, price):
        self.date = date
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

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
