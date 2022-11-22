PERCENT = .05
total_amount = 0
amount = float(input("Enter the amount of a purchase: "))
payment_instalment = int(input("Enter desired number of payment instalments: "))
i = 1
while i <= payment_instalment:
    amount += PERCENT
    i += 1
total_amount = amount
total_amount /= payment_instalment

print(f"The total amount of the purchase is: {format(total_amount, ',.2f')} and it will cost {payment_instalment}")
