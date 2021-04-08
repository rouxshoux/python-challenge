import os
import csv
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
average_month_change = 0
greatest_increase = 0
greatest_increse_month = ""
greatest_decrease = 0
greatest_increase_month = ""

path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")
with open(path, newline="") as csvfile:
    reader = csv.reader(csvfile, delmiter=",")
    header = next(csv.reader)
    row = next(reader)
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increaase_month = row[0]
    
    for row in reader:
        total_months += 1
        net_amount += int(row[1])
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.apend(row[0])
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        if int(row[1]) < greatest_decrease:
            greatest_decrease_month = row[0]
            
    average_change = sum(monthly_change) / len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)
    
print(f"Financial Anlysis")
print(f"--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

      