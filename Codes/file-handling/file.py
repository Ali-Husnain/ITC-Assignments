### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
import os
def line_count(directory ,file_name,bol=0):
    filename = os.path.join(directory,file_name)
    with open(filename,'r') as file1:
        if bol != True:
            return len(file1.read().split('\n'))
        else:
            return len([i for i in file1.read().split('\n') if not i== ''])
#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
import os
def character_count(directory , file_name, bol=0):
    filename = os.path.join(directory,file_name)
    with open(filename,'r') as file1:
        if bol != True:
            sum0 =  0
            for i in file1.read():
                sum0 += len(i)
            return sum0
        else:
            sum0 = 0
            for i in file1.read().strip():
                sum0 += len(i.strip())
            return sum0
#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
import os
def move_lines(first,second,lines):
    with open(first,'r') as f1:
        with open(second,'w') as f2:
            for i in range(lines):
               f2.write(i)
#### End OF MARKER



if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass

###########################################################################

### CODE FOR move_lines() FUNCTION GOES HERE ###
""" alternative
import os
def move_lines(first,second,lines):
    with open(first,'r') as f1:
        a = f1.read().split('\n')
        with open(second,'w') as f2:
            for i in range(lines):
                if i == lines-1:
                    f2.write(a[i])
                else:
                    f2.write(a[i]+'\n')"""

#############################################################################