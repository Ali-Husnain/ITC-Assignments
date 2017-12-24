### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(lst):
    if lst is None:
        return None
    lst.sort(reverse=True)
    total = []
    for e in lst:
        if e == None:
            return None
        else:
            a = list(e)
            l= []
            n = len(a)
            while 2< n:
                if not a[2] == None:
                    l.append(a[2])
                    a.pop(2)
                    n-=1
                else:
                    l.append(0)
                    a.pop(2)
                    n-=1
        
            l =sum(l)
            a.append(l)
            a = tuple(a)
            total.append(a)
            total.sort()
    return total

### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(t):
    y = find_cumulative_marks(t)
    a = []
    for i in y:
        b =i[2]
        a.append(b)
    marks = max(a)

    students = 0
    a = []
    for topper in y:
        
        if topper[2] == marks:
            students +=1
            topper = list(topper)
            topper.pop(2)
            topper = tuple(topper)
            a.append(topper)
            
    if students >1:

        return a
    
    if students == 1:
                
        return a[0]





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]
