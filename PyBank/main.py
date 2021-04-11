import os
import csv
pybank_path = "Resources/budget_data.csv"


ttl_month = 0
month_change = []
net_change_list = []
great_inc = ["", 0]
great_dec = ["", 999999999999999]
ttl_net = 0

with open(pybank_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first_row = next(csvreader)
    ttl_month = ttl_month + 1
    ttl_net = ttl_net + int(first_row[1])
    previous_net = int(first_row[1])
    
    for row in csvreader:
        ttl_month = ttl_month + 1
        ttl_net = ttl_net + int(first_row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]]
        if net_change > great_inc[1]:
            great_inc[0] = row[0]
            great_inc[1] = net_change
        if net_change < great_dec[1]:
            great_dec[0] = row[0]
            great_dec[1] = net_change
            
        net_month_average = sum(net_change_list)/len(net_change_list)
print("Financial Analysis")
print(f"Total Months: {ttl_month}")
print(f"Total: ${ttl_net}")
print(f"Average Change: ${net_month_average}")
print(f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})")
print(f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})")



output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {ttl_month}\n"
   f"Total: ${ttl_net}\n"
   f"Average  Change: ${net_month_average}\n"
   f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})\n"
   f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)