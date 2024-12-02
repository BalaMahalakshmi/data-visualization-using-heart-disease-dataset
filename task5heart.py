import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C://Users//Mathivathanan//Downloads//heart.csv")
print (df.head())
print (df.tail())
print(df.columns.values)
print(df.isna().sum())
print(df.info())
print(df.hist(bins=50, grid=False, figsize=(20,15)));
print(df.describe())
questions= ["1.how many people have heart diseases and how many peoples doesn't have heart disease?",
            "2. people of which sex has most heart disease?",
            "3. people of which sex has which type of chest pain most?",
            "4. people with which chest pain are most pron to have heart disease?"]
print(df.target.value_counts())
print(df.target.value_counts().plot(kind= 'bar',color=["orchid","salmon"]))
plt.title("Heart Disease Values")
plt.xlabel("1= Heart Disease ,0= no heart disease")
plt.ylabel("amount");
print(df.target.value_counts().plot(kind= "pie", figsize=(8,6)))
plt.legend(["Disease", "No Disease"])
print(pd.crosstab(df.target, df.sex))
print (sns.countplot(x='target', data= df, hue='sex'))
plt.title("Heart Disease Frequency for sex")
plt.xlabel("0= No Heart Disease, 1= Heart Disease")
print(pd.crosstab(df.cp, df.target))
