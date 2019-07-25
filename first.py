import pandas as pd
import numpy as np
data = pd.read_csv('./data.csv')
print data.keys()
import matplotlib.pyplot as plt
data['TotalRevenue'] = data['Quantity']*data['UnitPrice']
