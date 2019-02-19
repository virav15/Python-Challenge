import csv
import os

file_num = 2


#file_to_load = "raw_data/budget_data.csv"
#file_to_output = "analysis/budget_analysis.txt"
#emply lists for month and revenue data
file_path = os.path.join("..", "raw_data","budget_data.csv")

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

print("Total Months")
print(total_months)

