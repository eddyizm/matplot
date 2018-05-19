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
'''
'''
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(Cs, c_bottom)
f_bottom = np.add(Ds, d_bottom)
#create your plot here
plt.figure(figsize=(10,8))
plt.bar(range(len(As)), As)
plt.bar(range(len(Bs)), Bs, bottom=As)
plt.bar(range(len(Cs)), Cs, bottom=c_bottom)
plt.bar(range(len(Ds)), Ds, bottom=d_bottom)
plt.bar(range(len(Fs)), Fs, bottom=f_bottom)
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title('Grade Distribution')
ax.set_xlabel('Unit')   
ax.set_ylabel('Number of Students')
plt.savefig('my_stacked_bar.png')
plt.show()
'''
# Two Histograms on a Plot
from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
plt.figure(figsize=(10,8))
plt.hist(exam_scores1, bins=12, normed=True, histtype = 'step', linewidth =2)
plt.hist(exam_scores2, bins=12, normed=True,histtype = 'step', linewidth = 2)
plt.legend(['1st Yr Teaching','2nd Yr Teaching'])
plt.title('Final Exam Score Distribution')
ax = plt.subplot()
ax.set_xlabel('Percentage')
ax.set_ylabel('Frequency')
plt.savefig('my_histogram.png')
plt.show()