import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

# total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_births = names.pivot_table('births', index='name', columns='sex', aggfunc=sum)
# print(names)
print(total_births)

