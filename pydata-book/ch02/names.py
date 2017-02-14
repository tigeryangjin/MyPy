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


# print(total_births.tail())
# total_births.plot(title='Total births by sex and year')
# plt.show()

def add_prop(group):
    births = group.births
    group['prop'] = births / births.sum()
    return group


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
# print(top1000)

# names = names.groupby(['year', 'sex']).apply(add_prop)
# print(names)
# print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
plt.show()
print(subset)
