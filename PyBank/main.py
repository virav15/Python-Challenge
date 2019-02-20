import csv
import os


#emply lists for month and revenue data

file_path = os.path.join("raw_data","budget_data.csv")

months = []
revenue = []

#read csv and parse data into lists
#revenue list will be list of integers
with open(file_path) as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))
        #find total months
total_months = len(months)

greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0


for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

print("Total Months")
print(total_months)

print("-------------------")
print("Greatest Increase")
print(greatest_increase)

print("-------------------")
print("Greatest Decrease")
print(greatest_decrease)
