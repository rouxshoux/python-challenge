import os
import csv

pybank_path = os.path.join("Desktop/coding/01_All_My_Repos/python-challenge/PyBank/Resources/budget_data.csv")

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
        ttl_net - ttl_net + int(first_row[1])
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

output_file = os.path.join("Desktop/coding/01_All_My_Repos/python-challenge/PyBank/Resources/budget_data.csv")

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {ttl_month}\n")
    txtfile.write(f"Total: ${ttl_net}\n")
    txtfile.write(f"Average Change: ${net_month_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {great_inc}, (${great_inc[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {great_dec}, (${great_dec[1]})\n")
    
