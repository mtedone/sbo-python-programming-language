import csv

total = 0.0

with open('Data/portfolio.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)           # Skips the first line
    for rowno, row in enumerate(rows, start=1):
        try:
            row[2] = int(row[2])
            row[3] = float(row[3])
            print(row)
            total +=  row[2]*row[3]
        except ValueError as err:
            print('Bad row: ', rowno, row)
            print('Reason: ', rowno, err)

print(total)

