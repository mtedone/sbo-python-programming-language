import csv


def read_portfolio(filename, *, errors='warn'):
    '''
    Reads a CSV file with name, date, shares, price data into a list
    :param filename: The CSV file containing the data
    :param errors: What to do with errors. Valid values are: ['warn', 'silent', 'raise']
    :return: A list of the portfolio
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    portfolio = []  # List of records
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skips the first line
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
                total += row[2] * row[3]
            except ValueError as err:
                if errors == 'warn':
                    print('Bad row: ', rowno, row)
                    print('Reason: ', rowno, err)
                elif errors == 'raise':
                    raise  # Reraises the last exception
                else:
                    pass
                continue
            #record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv', errors='warn')
print(portfolio)

total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']

print(total)
