import csv
import os

# get the path to the current directory
current_dir = os.path.dirname(__file__)

# the path to the CSV file
budget_csv = os.path.join(current_dir , 'Resources' , 'budget_data.csv')

# list to store data
Date = []
PL = []
Change = []

# Open and read the CSV file 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Store header row
    header = next(csvreader)

# Start to read from the 2nd row and store the variables
    for row in csvreader:
        # Add date
        Date.append(str(row[0]))

        # Add profile/loss and make it as integer
        PL.append(int(row[1]))
    
    # Count total month and calculate total amount
    Total_month = len(Date)
    Total_amount = sum(PL)

    # Define variable for greatest value
    GreatestIncrease = 0
    GreatestDecrease = 0

    # Use for loop to store the change of each month and store the change to the greatest value after comparison
    for i in range((Total_month-1)):
        Change.append(PL[i+1] - PL[(i)])
        if Change[i] > GreatestIncrease:
            GreatestIncrease = Change [i]
            GreatestIncreaseMonth = Date[i+1]
        elif Change[i] < GreatestDecrease:
            GreatestDecrease = Change[i]
            GreatestDecreaseMonth = Date[i+1]
    # Calculate the average change
    Average_change = round((sum(Change)/(Total_month-1)),2)
 
 # Store the result to a list for printing
    analysis = [
        f"Financial Analysis",
        f"----------------------------",
        f"Total Months: {Total_month}",
        f"Total: ${Total_amount}",
        f"Average Change: ${Average_change}",
        f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease})",
        f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})"
        ]

 
    
   
# print result to a new txt file    
analysis_path = os.path.join(current_dir , 'analysis' , 'analysis.txt')

with open(analysis_path, "w") as file:

# add "enter" after printing each line and print to terminal
    for line in analysis:    
        file.write(line + "\n")
        print(line)
        


