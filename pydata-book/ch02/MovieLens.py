import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('')
