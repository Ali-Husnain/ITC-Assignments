## CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def grades(x):

    if x == 'A+' or x== 'A':
        return 4.00
    elif x == 'A-':
        return 3.67
    elif x == 'B+':
        return 3.33
    elif x == 'B':
        return 3.00
    elif x== 'B-':
        return 2.67
    elif x== 'C+':
        return 2.33
    elif x== 'C':
        return 2.00
    elif x == 'C-':
        return 1.67
    elif x == 'D+':
        return 1.33
    elif x == 'D':
        return 1.00
    elif x == 'F':
        return 0.00
    else:
        return None




def calculate_sgpa(l):
    if type(l) == str:
        g = grades(l)
        return g
    if l == None:
        return None
    elif l == []:
        return 0.0
    else:


        G = []
        for e in l:
            if not type(e) == str:
                return None
            else:
                type(e) == str
                g = grades(e)
                G.append(g);
        if None in G:
            return None
        else:
            S = sum(G)
            L = len(G)
            sgpa = S/L
            return sgpa



print calculate_sgpa(['A+', 'C-','A+', 'C-','A+', 'B-','A', 'C','A+', 'C-'])


### CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(g ,w):
    if type(g) == list and type(w) ==list:
        if not len(g) == len(w):
            return None
    if not type(g)==list and type(w) != list:
        g = grades(g)
        a = (g*w)/w
        return a

    if type(g) == list and w == float or int:
        if len(g) == 1:
            for i in g:
                i = grades(i)
                a = (i*w)/w
                return a
        else:
            if type(g) != list and type(w) ==list:
                if len(w) == 1:
                    for i in w:

                        g = grades(g)
                        a = (g*i)/i
                        return a
    if g== None or w == None:
        return None

    G=[]
    for e in g:
        g = grades(e)
        G.append(g);
    Z = []
    if len(G) == len(w):
        if None in G or None in w:
            return None
        elif None in G and None in w:
            return None
        else:

            for a , b in zip(G ,w):
                z =(a * b)
                Z.append(z)

    Z = sum(Z)
    w = sum(w)


    SGPA = Z/w
    return SGPA
print calculate_sgpa_weighted(['A'] ,[2 ,1 ])