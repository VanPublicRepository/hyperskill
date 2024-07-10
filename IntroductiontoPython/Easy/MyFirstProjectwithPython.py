print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80')

INCOME = 202 + 118 + 2250 + 1680 + 1075 + 80
print('Income: $', INCOME)

staff_expenses = int(input('Staff expenses: '))
other_expenses = int(input('Other expenses: '))

net_income = INCOME - (staff_expenses + other_expenses)
print(f'Net income: ${net_income}')
