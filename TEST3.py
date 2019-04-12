a = ['who', 'am', 'I']
b = ['hello', 'my', 'am']
sa = set(a)
sb = set(b)
sc = sa | sb
l = list(sc)
l = l.sort()
print(l)
