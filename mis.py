
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
worktype = ["Trying to understand Wayne Johns Code", "Discussing Deadlines", "Writing Code", "Discussing Politics"]
timespent = [270, 77, 32, 11]

#make your pie chart here
plt.pie(timespent, autopct='%0.1f%%')
plt.axis('equal')
plt.title('Typical week at AMM')
plt.legend(worktype, bbox_to_anchor=(1,0), loc="lower right", 
                          bbox_transform=plt.gcf().transFigure)
plt.show()