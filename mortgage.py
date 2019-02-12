principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0
extra_payment = 1000
extra_payment_start_montb = 1
extra_payment_end_month = 60
month = 0

print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'))

while principal > 0:
    month += 1
    if (month >= extra_payment_start_montb and month <= extra_payment_end_month):
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal))

print('Total paid: ', total_paid)