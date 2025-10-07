
class DataInvestigator:

    def __init__(self, df):
        self.df = df

    def baseline(self, col):
        column_values = self.df.iloc[:, col].values
        return max(set(column_values.tolist()), key=column_values.tolist().count)
        

    def corr(self, col1, col2):
        correlation = self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        return correlation

    def zeroR(self, col):
        column_values = self.df.iloc[:, col].values
        most_common = max(set(column_values.tolist()), key=column_values.tolist().count)
        return most_common

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)

sns.displot(data=df, x='Glucose', kind='hist', kde=True)
plt.show()

print(df.groupby("Gender")[["Height","Weight","Body Mass Index (BMI)",
                            "Total Body Fat Ratio (TBFR) (%)",
                            "Hemoglobin (HGB)"]].mean())
print(df.groupby("Gender")["Hemoglobin (HGB)"].describe())
print(df.groupby("Gender")["Total Body Fat Ratio (TBFR) (%)"].describe())


print(di.baseline(1))