d={'a':5,'g':3,'t':8}
print(d)
for key in d:
    d[key]=0
print(d)
d['g']=d.get('g')+1
print(d)