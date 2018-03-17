def divisors(integer):
    arr = []
    for x in range(2, round(integer ** 0.5+1)): #if integer is 12
        if integer % x == 0:
            arr.append(x)
            arr.append(int(integer / x))
    if len(arr) == 0:
        return str(integer) + ' is prime'
    else:
        return sorted(arr)

print(divisors(12))