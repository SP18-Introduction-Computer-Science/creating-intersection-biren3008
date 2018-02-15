a = [1,4,5,7,8,12]
b = [4,5,9,12,15,2]

def intersect(set1, set2):
    sets = []    
    for element in set1:
        if element in set2:
            sets.append(element)        
    return sets

c = intersect(a,b)

print(c)

