
from matplotlib import pyplot as plt
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
plt.show()

# 4/12 double bars side by side
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]
# plot first data set.
plt.bar(store1_x, sales1)             

# added second set of x values
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store2_x, sales2)

plt.show()

# 5/12 Stacked Bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(sales1)), sales1)
plt.bar(range(len(sales2)), sales2, bottom=sales1)
legend_labels = ['Location 1', 'Location 2']
plt.legend(legend_labels)
plt.show()

# 6/12 Error Bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(ounces_of_milk)), ounces_of_milk, yerr=error, capsize=5)
plt.show()

# 7/12 Fill Between
from matplotlib import pyplot as plt
# x_values = range(10)
# y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
# y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
# y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]
# y_lower = [i - 2 for i in y_values]

# plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
# plt.plot(x_values, y_values) #this is the line itself

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [i - 0.1 * i for i in revenue]  
y_upper = [i + 0.1 * i for i in revenue]

#your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
plt.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.plot(months, revenue)
plt.show()

# 8/12 Pie Chart & 9/12 Pie Chart Labeling
from matplotlib import pyplot as plt
import numpy as np
# budget_data = [500, 1000, 750, 300, 100]
# budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']
# plt.legend(budget_categories)

# option 2 - This puts the category names into labels next to each corresponding slice:
# plt.pie(budget_data, labels=budget_categories)
# option 3 - add percentage
# plt.pie(budget_data,
#         labels=budget_categories,
#         autopct='%0.1f%%')
# plt.pie(budget_data)
# plt.axis('equal')
# plt.show()
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs, autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()

# 10/12 Histogram 11/12 Multiple Histograms
from matplotlib import pyplot as plt
from script import sales_times
# plt.hist(dataset, range=(66,69), bins=40)
#create the histogram here
plt.hist(sales_times, bins=20)
plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha=0.4,normed=True)
plt.show()

'''
Review
In helping MatplotSip visualize their data, you’ve learned a bunch of new plot types that you can use in Matplotlib. Congratulations on adding these new plotting abilities to your repertoire:

How to compare categories of data with bar graphs
Add error bars to graphs
Use fill_between to display shaded error on line graphs
Create stacked bar graphs for easier comparisons
Create side-by-side bar graphs
Create and format pie charts to compare proportional datasets
Analyze frequency data using histograms, including multiple histograms on the same plot
Normalize histograms
In the upcoming project, you will experiment with these different plot types and how to best use them to find patterns or trends in a new data set.
'''