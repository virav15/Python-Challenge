import csv
import os


file_num = 2

file_path = os.path.join("raw_data","budget_data.csv")

months = []
profit_loss = []


with open(file_path) as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
total_months = len(months)

greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_profit_loss = 0


for r in range(len(profit_loss)):
    if profit_loss[r] >= greatest_increase:
        greatest_increase = profit_loss[r]
        great_inc_month = months[r]
    elif profit_loss[r] <= greatest_decrease:
        greatest_decrease = profit_loss[r]
        great_dec_month = months[r]
    total_profit_loss += profit_loss[r]


average_change = round(total_profit_loss/total_months, 2)


output_dest = os.path.join('output_csv','pybank_output' + str(file_num) + '.txt')


with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Profits/Losses: $' + str(total_profit_loss) + '\n')
    writefile.writelines('Average  Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Loss: ' + great_dec_month + ' ($' + str(greatest_decrease) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())