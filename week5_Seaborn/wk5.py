import pandas as pd
from matplotlib import pyplot as plt

# Paste import here:
import seaborn as sns

df = pd.read_csv('survey.csv')
print (df.head())
# sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
# plt.show()


# direct to seaborn
df = pd.read_csv('results.csv')
print(df)
sns.barplot(
 data= df ,
 x='Gender' ,
 y='Mean Satisfaction'
)

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)

plt.show()