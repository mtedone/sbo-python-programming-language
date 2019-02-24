import csv


def read_csv(filename, types, *, errors='warn'):
    '''
    Reads a CSV file with type conversion into a list of dicts
    :param filename: The CSV file containing the data
    :param types: A list of types to convert tuple elements to
    :param errors: What to do with errors. Valid values are: ['warn', 'silent', 'raise']
    :return: A list of the portfolio
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    clean_headers = []
    records = []  # List of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skips the first line
        for rowno, row in enumerate(rows, start=1):
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if errors == 'warn':
                    print('Bad row: ', rowno, row)
                    print('Reason: ', rowno, err)
                elif errors == 'raise':
                    raise  # Reraises the last exception
                else:
                    pass
                continue
            # record = tuple(row)
            record = dict(zip(headers, row))
            records.append(record)
    return records
