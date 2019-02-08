from matplotlib import pyplot
import pandas as pd
import numpy as np

# generate target line data
data_size = 1000
x = np.arange(data_size)
delta = np.random.uniform(-300000, 700000000, x.size)
y = 0.9 * x + x * x * x + delta
df_y = pd.DataFrame(y)
#df_y2 = df_y.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
df_y2 = df_y.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
y2 = df_y2.values.ravel()
y2 = y2 * y2
y2 = y2 * y2
data = np.array([x, y2]).transpose()
data_label = np.arange(data_size)
for i in range(len(data_label)):
    if i <= data_size * 0.20:
        data_label[i] = 0
    elif i <= data_size * 0.65:
        data_label[i] = 1
    elif i <= data_size * 0.85:
        data_label[i] = 2
    else:
        if y2[i] < 0.45:
            data_label[i] = 2
        else:
            data_label[i] = 0
for i in range(data_size):
    print("lot" + str(1000 + i), "NA", data[i][0], data[i][1], data_label[i], sep='\t')

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=data[:, 0], y=data[:, 1], label=data_label))
colors = {0:'red', 1:'blue', 2:'green'}
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', s=4, x='x', y='y', label=key, color=colors[key])
#pyplot.show()
pyplot.savefig(fname='02_user_defined_equation_scatter_plot.png')
pyplot.close()
