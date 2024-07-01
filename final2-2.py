# # CS 5002 Final Project Matching ads and viewers
# 04/12/2023 Yunyu Guo

import pandas as pd

df = pd.read_csv('advertising.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
df.drop('Ad Topic Line', axis =1, inplace=True)
df.drop('City', axis =1, inplace=True)
df.drop('Country', axis =1, inplace=True)
df.drop('Timestamp', axis =1, inplace=True)
print(df.head())
y = df['Clicked on Ad']
# This line assigns the ‘Clicked on Ad’ column of the DataFrame to the variable y
# This is the target variable in a machine learning model
df.drop('Clicked on Ad', axis=1, inplace=True)
x = df
# assigns the modified DataFrame to the variable x.
# This is the features in a machine learning model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)
# splits the features and target variables into training and test sets
# 20% of the data is used for the test set.
from sklearn.linear_model import LogisticRegression
lm = LogisticRegression()
# creates a Logistic Regression model
lm.fit(x_train,y_train)
# trains the Logistic Regression model using the training data
print(lm.score(x_test,y_test))
# returns the mean accuracy on the given test data and labels
import matplotlib.pyplot as plt
df.hist(figsize=(10,11))
plt.show()
