## CODE FOR output_prime_factors() FUNCTION GOES HERE ###

def output_prime_factors(x):
    x = round(x)
    x = int(x)
    factors = []
    if x == 0 and x==1:
        return None
    x = int(x)
    a = x+1
    for i in range(1 ,a):
        if x>0:

            f= x%i
            if f == 0:
                factors.append(i)
    return prime(factors)
def prime(x):
    for i in x:
        a = is_prime(i)
        if a == True and i != 1:
            print i
def is_prime(x):
    x = int(x)
    if x<=1:
        return None
    if x>1:

        for n in range(2, x):
            r = x%n
            while r == 0:
                return False
    return True

print output_prime_factors(10)


### CODE FOR get_nth_prime() FUNCTION GOES HERE ###


def get_nth_prime(x):
    if type(x) == float:
        return None
    nth = 0
    prime = 0
    while not nth == x:
        if is_prime(prime):
            nth  += 1
            a = prime
        prime += 1
        if nth == x:
            return a
##########################################3333

print get_nth_prime(29)

print get_nth_prime(2)

