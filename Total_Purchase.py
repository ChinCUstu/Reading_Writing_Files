PERCENT = 100
SALES_TAX = 7
STORE = 5
subtotal = 0
total = 0
i = 1
while i <= STORE:
    price = float(input(f'Enter the price for item{i}: '))
    subtotal += price
    total += subtotal
    i += 1
amount_sales_tax = subtotal * SALES_TAX
print(f'The subtotal: {subtotal}')
print(f'The amount of sales tax: {amount_sales_tax}')
print(f'The total: {total}')
