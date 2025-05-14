Lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']


mydict = {}
for i in range(len(Lista)):
    mydict[Lista[i]] = Listb[i]

print(mydict)