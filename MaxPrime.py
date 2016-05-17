def is_prime(x):
    if x<=1:
        return False
    if x>=2:
        i=2
        while i*i<=x:
            if x%i==0:
                return False
            i+=1
        return x

def findMaxPrime():
    num=1
    while num>=1:
        if is_prime(num)==num:
            print(num)
        num+=2

print(findMaxPrime())