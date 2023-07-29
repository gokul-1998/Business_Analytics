![](2023-07-29-12-39-19.png)
```
import pandas as pd

data=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRDZkwZBRxDBglsORcnrTJM3JDe5lmd8o-j-J8EYmKwcTKGpWzkN70CvBKlcopd4A/pub?output=csv')

data.shape
print(data.data.skew())
print(data.data.describe())
print(data.data.hist())
```
![](2023-07-29-13-05-23.png)
![](2023-07-29-13-04-59.png)

![](2023-07-29-13-07-59.png)
![](2023-07-29-13-07-47.png)

![](2023-07-29-13-08-40.png)

![](2023-07-29-13-08-51.png)

![](2023-07-29-18-43-38.png)

![](2023-07-29-18-57-32.png)