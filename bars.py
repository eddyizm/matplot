'''
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
plt.show()
'''
# 4/12 
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = ?  # This is our first dataset (out of 2)
t = ? # Number of datasets
d = ? # Number of sets of bars
w = ? # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.show()
