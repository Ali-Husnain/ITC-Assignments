#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
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

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    if x == 0 and x==1:
        return None
    x = int(x)
    a = x+1
    for i in range(1 ,a):
        if x>0:

            f= x%i
            if f == 0:
                print i

#### CODE FOR get_largest_prime() FUNCTION GOES HERE ####


def get_largest_prime(x):
    x = round (x)
    x = int(x)
    if x>0:


        for n in range(x,1,-1):

            if is_prime(n) == True:
                return n
    else:
        return None

print get_largest_prime(82.9)
