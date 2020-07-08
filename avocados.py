

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset/avocado.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.head()

print(data.isnull().sum())
print(data)

albany = data[data.region == 'Albany']
print(albany)

plt.figure(figsize=(12, 5))
plt.title("Distribution Price")
# alternatively can access column using data.AveragePrice
ax = sns.distplot(data["AveragePrice"], color = 'r')
plt.show()
#sns.boxplot(y="type", x="AveragePrice", data=data, palette = 'pink')
print('ending')

