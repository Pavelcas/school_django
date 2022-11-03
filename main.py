def validate(n):
    n = [int(i) for i in str(n)]
    for i in range(len(list(reversed(n)))):
        if i % 2 == 1 and n[i]<9:
            n[i] = n[i]*2
    return sum(n)%10 == 0
print(validate(2121))