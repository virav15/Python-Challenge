import csv


import os
file_num = 2

file_path = os.path.join("raw_data","budget_data.csv")

###########
with open(file_path, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(reader)

    dates = []
    money = []
    change =[]
    change_alt = []
    previous = 0
##
    for row in reader:
        dates.append(row[0])
        money.append(row[1])
        
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)

zipped = zip(dates, change)
zipped_lst = list(zipped)
change.remove(change[0])
zipped_lst.remove(zipped_lst[0])

   

total_months = len(dates)
total = sum(map(int, money))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

month_dec = 0
month_inc = 0

for row in zipped_lst:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})\n')

output_dest = os.path.join('output_csv','pybank_output' + str(file_num) + '.txt')

with open(output_dest, 'w') as writefile:
    print(f'Financial Analysis\n')
    print(f'___________________________\n')
    print(f'Total Months: {total_months}\n')
    print(f'Total: ${total}\n')
    print(f'Average Change: ${average_change:.2f}\n')
    print(f'Greatest Increase in Profits: {month_inc} ({increase})\n')
    print(f'Greatest Decrease in Profits: {month_dec} ({decrease})\n')