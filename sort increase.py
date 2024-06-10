b= [0, 6, 10, 1, 3, 9]
for k in range(len(b)):
    for j in range(k):
        if b[k] < b[j]:
            tmp = b[k]
            b[k] = b[j]
            b[j] = tmp
print(b)            
