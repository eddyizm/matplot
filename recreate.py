# recreate exercises
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
plt.bar(range(len(past_years_averages)), past_years_averages, yerr=error, capsize=5)
ax = plt.subplot()
# set limits
ax.set_xlim(-0.5,6.5)
ax.set_ylim(70, 95)
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
# set titles/labels
plt.title('Final Exam Averages')
ax.set_xlabel('Year')
ax.set_ylabel('Test Average')
plt.savefig('my_bar_chart.png')
plt.show()

# side by side bars