import csv

total = 0.0

with open('Data/portfolio.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)           # Skips the first line
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        print(row)
        total +=  row[2]*row[3]

print(total)

