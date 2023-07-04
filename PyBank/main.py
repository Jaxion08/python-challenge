import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')
results_file = os.path.join('analysis', 'results.txt')

pre_row = None
total_months = 0
total = 0
changes = []
max_change = float('-inf')
min_change = float('inf')
max_month = None
min_month = None

with open(budget_csv, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    header = next(budget_data)

    for row in budget_data:
        'get totals'
        total += int(row[1])
        total_months += 1

        if pre_row is not None:
            'calculate change from previous row to current row and append to changes list'
            value = float(row[1])
            pre_value = float(pre_row[1])
            change = value - pre_value
            changes.append(change)

            'search for and store maximum change'
            if change > max_change:
                max_change = change
                max_month = row[0]

            'search for and store minimum change'
            if change < min_change:
                min_change = change
                min_month = row[0]

        pre_row = row

average_change = sum(changes) / len(changes)

results = f"Financial Analysis\n----------------------------\n"
results += f"Total Months: {total_months}\n"
results += f"Total: ${total}\n"
results += f"Average Change: ${average_change:.2f}\n"
results += f"Greatest Increase in Profits: {max_month} (${max_change})\n"
results += f"Greatest Decrease in Profits: {min_month} (${min_change})\n"

print(results)
print("The results have been saved to:", results_file)

with open(results_file, "w") as txt_file:
    txt_file.write(results)