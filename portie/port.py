from . import reader


def read_portfolio(filename, *, errors='warn'):
    return reader.read_csv(filename, [str, str, int, float])


if __name__ == '__main__':
    portfolio = read_portfolio('../Data/portfolio.csv', errors='warn')
    print(portfolio)
    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']

    print(total)
