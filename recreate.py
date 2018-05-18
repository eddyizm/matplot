# recreate exercises
'''
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
'''
# side by side bars
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
# Make your chart here
plt.figure(figsize=(10,8))
ax = plt.subplot()
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
middle_x =[(a + b) / 2.0 for a,b in zip(school_a_x, school_b_x) ]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend(['Middle School A', 'Middle School B'])
plt.title('Test Averages on Different Units')
ax.set_xlabel('Unit')
ax.set_ylabel('Test Average')
plt.savefig('my_side_by_side.png')
plt.show()