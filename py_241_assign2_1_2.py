def correct(cats):
    for i in range(0, len(cats), 2):
        if (cats[i] != cats[i + 1]): return False
    return True

def remainCat(cats, size):
    return [cat for cat in cats if size != cat]

n = int(input('input n : '))
cats = [int(input()) for i in range(n)]
setCat = set(cats)

ans = 0
for size in setCat:
    if correct(cats):
        print(ans)
        break
    cats = remainCat(cats, size)
    ans = size
