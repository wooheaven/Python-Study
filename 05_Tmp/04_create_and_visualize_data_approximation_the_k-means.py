from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot
from pandas import DataFrame
import numpy as np

# generate 2d classification data
data, data_label = make_blobs(n_samples=1000, centers=3, n_features=2)

# scatter plot, dots colored by class value
df = DataFrame(dict(x=data[:, 0], y=data[:, 1], label=data_label))
colors = {0:'red', 1:'blue', 2:'green'}
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', s=4, x='x', y='y', label=key, color=colors[key])
pyplot.show()
