import pandas as pd
import statsmodels.api as sm
import matplotlib as pyplot

data=sm.datasets.co2.load_pandas()
co2=data.data

print(co2.head(5))
print(co2.index)

y=co2['co2'].resample('MS').mean()

print(y.head(5))

