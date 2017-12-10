#######################################################################
#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x , guess=0.0):
    X = x * 1.0000
    GUESS = guess * 1.0000
    if X<0.00000:
        return None

    if good_enough(GUESS ,X):
        return GUESS
    else:
        new_guess = improve_guess(GUESS ,X)
        return sqrt(X ,new_guess)


def good_enough(GUESS,X):
    if abs(float(GUESS * GUESS - X)) < 0.00001:
        return True
    else:
        return False

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(GUESS ,X):
    return(abs(GUESS + X)/2.00000)

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####


def improve_guess(GUESS ,X):
    G = GUESS * 1.0000
    N = X * 1.0000

    if GUESS < 1.00000:
        return GUESS  + 1.00000
    else:
        return average(G ,N/G)

def average(GUESS ,X):
    return(abs(GUESS + X)/2.00000)



#### End OF MARKER

print sqrt(54 ,7)