'''
Created on 23-Nov-2023

@author: Nomura
'''

def zipList(lst1:list, lst2:list):
    
    for i, lstitem in enumerate(lst1):
        if len(lst2) >= i+1:
            yield (lstitem, lst2[i])
        
        


for ls1ls2 in zipList([11,22,33,44], [111,222,333]):
    print(ls1ls2)

for ls1ls2 in zipList(["One", "Two", "Three", "Four", "Five"], ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]):
    print(ls1ls2)
