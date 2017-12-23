##############################################################################

#### CODE FOR get_grade() FUNCTION GOES HERE ####
def N(x):
    c = x *1.00
    x = int (x)
    d = c - x
    if d < .50:
        m = c
    if d == .50:
        m = c + .50
    if d>.50:
        m =c + 1
        m = int (m)
    return m

def get_grade(x):

    m = N(x)

    if m<=100.0 and m==90.0:
        return 'A+'
    elif m<90 and m>=86:
        return 'A'
    elif m<86 and m>=82:
        return 'A-'
    elif m<82 and m>=78:
        return 'B+'
    elif m<78 and m>=74:
        return 'B'
    elif m<74 and m>=70:
        return 'B-'
    elif m<70 and m>=66:
        return 'C+'
    elif m<66 and m>=62:
        return 'C'
    elif m<62 and m>=58:
        return 'C-'
    elif m<58 and m>=54:
        return 'D+'
    elif m<54 and m>=50:
        return 'D'
    elif m < 50 and m>=0:
        return 'F'
    else:
        m < 0
        return None


#### CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def GPA(g):
    if g == ("nothing"):
        return 0
    if g == ("A+"):
        return 4.00
    if g == ("A"):
        return 4.00
    if g==("A-"):
        return 3.67
    if g==("B+"):
        return 3.33
    if g==("B"):
        return 3.00
    if g==("B-"):
        return 2.67
    if g==("C+"):
        return 2.33
    if g==("C"):
        return 2.00
    if g==("C-"):
        return 1.67
    if g==("D+"):
        return 1.33
    if g==("D"):
        return 1.00
    if g==("F"):

        return 0


def calculate_sgpa(x , y , z):


    m= 0
    s= 0

    if not x == 'nothing':
        m = GPA(x) + m
        s = s + 1

    if not y == 'nothing':
        m  = m + GPA(y)
        s = s + 1

    if not z == 'nothing':
        m = m + GPA(z)
        s = s + 1

    return SGPA(m ,s)
def SGPA(a ,b):
    return abs(a/b)


calculate_sgpa('F','F' ,'nothing')



#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')

##############################################################################
