listt = [1, 2, 3, (1, 2), None]

print(listt)
print(type(listt))
l = []
for i in listt:
    l.append(i)
l[1] = 0
print(l)