import csv 
import os

path_to_open = os.path.join("Resources", "budget_data.csv")
NumofMonths = 0
Total_rev = 0
sum_of_changes = 0 
list_of_changes = []
months = []
last = None 
with open(path_to_open) as budget_datacsv:
    Buggetreader = csv.reader(budget_datacsv)
    # skip header
    header = next(Buggetreader)
    #find the total amount of months 
    for row in Buggetreader:
        months.append(row[0])
        Total_rev += int(row[1])
        NumofMonths = NumofMonths+1  # NumsMonths += 1
        if last :
            temp = int(row[1])-last
            sum_of_changes += temp
            list_of_changes.append(temp)
        last = int(row[1])
    print("total Months: " + str(NumofMonths))
    #finding the The net total amount of "Profit/Losses" over the entire period
    print(f'Total: ${Total_rev}')
    print(f'Average Change: ${sum_of_changes/(NumofMonths-1)}')
    max_value = max(list_of_changes)
    last_index = list_of_changes.index(max_value)+1
    print(f'Greatest Increase in Profits: {months[last_index]} (${max_value})')

    min_value = min(list_of_changes)
    last_index = list_of_changes.index(min_value)+1
    print(f'Greatest Decrease in Profits: {months[last_index]} (${min_value})')

