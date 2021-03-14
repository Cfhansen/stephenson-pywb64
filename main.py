###Solution to exercise 64 in ben stephenson's "the python workbook".

import math

def get_more_values():
  print('Enter a value:')
  return input()

results = []

print('Enter a value:')
val_ = input()
if val_ != '':
  results.append(float(val_))

while val_ != '':
  val_ = get_more_values()
  if val_ != '':
    results.append(float(val_))

total_cost = round(sum(results),2)
pennies = int(str(total_cost)[-1])
if pennies < 2.5:
  rounded_cost = round(total_cost,1)
elif pennies < 7.5:
  rounded_cost = (math.floor(total_cost * 10) / 10) + .05
else:
  rounded_cost = math.ceil(total_cost * 10) / 10


print(f'Total cost: {total_cost:.2f}.')
print(f'Rounded cost: {rounded_cost:.2f}.')
