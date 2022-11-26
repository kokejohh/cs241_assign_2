#Pitchakorn Thiprangsi
#6309682091

def correct(cats):
    for i in range(0, len(cats), 2):
        if (cats[i] != cats[i + 1]): return False
    return True

def remainCat(cats, size):
    return [cat for cat in cats if size != cat]

n = int(input('input n : '))
cats = []
for i in range(n): cats.append(int(input()))
setCat = set(cats)
if (correct(cats)): print(0)
else:
    for size in setCat:
        cats = remainCat(cats, size)
        if (correct(cats)):
            print(size)
            break



