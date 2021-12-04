import matplotlib.pyplot as plt
import pandas as pd


# defines variable honey_data with csv file data
read = pd.read_csv("operations.csv")
print(read['Value'])

# replaces commas in large number
# read['Value'] = read['Value'].str.replace(',', '')
# makes strings numeric values
read['Value'] = pd.to_numeric(read['Value'], errors='coerce')

print(read['Value'])

# creates empty lists
all_honey = []
all_states = []
# unique_states = read['State'].unique()

# goes through list of each state and prints values
# for state in unique_states:
#   # defines honey_data to group by both state and separates years and values
'''honey_data = sum of all sums'''
honey_data = honey_sums.sum()
#   # prints each state and the sum of their values
#   print (honey_data.sum())
#   # adds values and states to list
all_honey.append(honey_data.sum())
#  all_states.append(state)
# defines honey_sums and years
honey_sums = honey_data.sum()
years = honey_sums.keys()

# goes through list of states and values
for i in range (len(all_honey)):
  # goes through list gets honey and year paired values
  honey = all_honey[i]
  # state = all_states[i]
  years = all_honey[i].keys()
  # creates graph
  plt.plot(years, honey)
  # creates labels
  plt.ylabel('Honey Value')
  plt.xlabel('Years')
  plt.title('Honey Value over Time')
plt.show()
