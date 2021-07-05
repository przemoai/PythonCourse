ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


gen = ((start,stop) for start in ports for stop in ports if start<stop)
counter = 0;
while True:
    try:
        print(next(gen))
        
        counter+=1
    except StopIteration:
        print("I've been printed all combinations")
        break

print("Generated {} pairs".format(counter))