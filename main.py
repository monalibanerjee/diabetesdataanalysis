# import all necessary libraries
import matplotlib.style as style
style.available
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.show()
#plt.savefig( 'myfig.png' )
from matplotlib import pylab

plt.style.use('ggplot')
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')
#Loading the dataset
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head(10))
#p = diabetes_data.hist(figsize = (20,20))
#plt.savefig('histogram.png')
colsToModify = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',]
val = []
#Modifying 0 entries
for col in colsToModify:
  val.append(len(diabetes_data[diabetes_data[col] == 0]))
zeroCount = pd.DataFrame(val, index = colsToModify, columns = ['zeroCount'])
# Replacing zero value with respective mean vale
for col in colsToModify:
    diabetes_data[col] = diabetes_data[col].replace(0,np.NaN)
    mean = int(diabetes_data[col].mean(skipna = True))
    diabetes_data[col] = diabetes_data[col].replace(np.NaN, mean)
print(diabetes_data.duplicated().sum())
print(diabetes_data.isnull().sum())

style.use('seaborn-pastel')
labels = ["Healthy", "Diabetic"]
diabetes_data['Outcome'].value_counts().plot(kind='pie',labels=labels, subplots=True,autopct='%1.0f%%', labeldistance=1.2, figsize=(9,9))
#plt.savefig('piechart.png')
plt.figure()
ax = sns.distplot(diabetes_data['Glucose'][diabetes_data.Outcome == 1], color ="darkturquoise", rug = True)
sns.distplot(diabetes_data['Glucose'][diabetes_data.Outcome == 0], color ="lightcoral", rug = True)
plt.legend(['Diabetes', 'No Diabetes'])
plt.savefig('bargraph.png')
#to check for diabetes and blood pressure
plt.figure()
ax = sns.distplot(diabetes_data['BloodPressure'][diabetes_data.Outcome == 1], color ="darkturquoise", rug=True)
sns.distplot(diabetes_data['BloodPressure'][diabetes_data.Outcome == 0], color ="lightcoral", rug=True)
plt.legend(['Diabetes', 'No Diabetes'])
plt.savefig('bloodpressure_and_diabetes.png')
