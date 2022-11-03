def validate(n):
    n = list(reversed([int(i) for i in str(n)]))
    for i in range(len(n)):
        if i % 2 == 1 and n[i]<5:
            n[i] = n[i]*2
        elif i % 2 == 1 and n[i]>=5:
            n[i] = n[i]*2-9
    return sum(n)%10 == 0
print(validate(44116824277224))