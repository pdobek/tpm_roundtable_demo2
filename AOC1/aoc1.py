from itertools import combinations
import operator

def sums_to_2020(values):
    return sum(values) == 2020

# Open the file and read in the values as strings
f = open("expenses.txt", "r")
expense = []
o = []

for x in f:
    #print('The value of x is:', x)
    expense.append(x)

# Convert the strings to integers 
expense = list(map(int, expense))

# Create the array paired list
all_expense_pairs = list(combinations(expense, 2))

# Filter the list to those values that sum to 2020
result = list(filter(sums_to_2020, all_expense_pairs))

print('The pairs that add up to 2020 are: ' + str(result))
print(len(result))

#get the values into a string
values = list(map(int, result[0]))
print(values[0])
print(values[1])
print(values[0] * values[1])

# Close the file
f.close()