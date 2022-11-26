#Pitchakorn Thiprangsi
#6309682091

def correct(cats):
    for i in range(0, len(cats), 2):
        if (cats[i] != cats[i + 1]):
            return False
    return True

def remainCat(cats):
    tmp = cats[:]
    for cat in tmp:
        if (size == cat):
            tmp.remove(cat)
            tmp.remove(cat)
            break
    return tmp


n = int(input('input n : '))

cats = []
for i in range(n):
    cats.append(int(input()))
    
setCat = set(cats)
for size in setCat:
    cats = remainCat(cats)
    if (correct(cats)):
        print(size)
        break



