import csv 
import os

path_to_open = os.path.join("Resources", "budget_data.csv")
NumofMonths = 0
with open(path_to_open) as budget_datacsv:
    Buggetreader = csv.reader(budget_datacsv)
    # skip header
    header = next(Buggetreader)
    #find the total amount of months 
    for row in Buggetreader:
        NumofMonths = NumofMonths+1  # NumsMonths += 1
    print("total Months: " + str(NumofMonths))
    #finding the The net total amount of "Profit/Losses" over the entire period
    Net_Profit_Lossess = sum(Buggetreader(1))
    print(Net_Profit_Lossess)

