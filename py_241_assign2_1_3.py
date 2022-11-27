def findIndex(arr, value):
    return (i for i in range(len(arr)) if arr[i] == value)

n = int(input('input n: '))
cats = [int(input()) for i in range(n)]
setCat = set(cats)

ans = 0
for size in setCat:
    for i in range(len(cats)):
        x, y = findIndex(cats, size)
        tmp_max = max(cats[x + 1:y], default=0)
        tmp_max = size if (tmp_max > size) else tmp_max
        ans = tmp_max if (tmp_max > ans) else ans
        break
print(ans)
