import numpy as np

def read_array(input):

    f = open(input, 'r')
    matrix = []
    for line in f.read().split('\n'):
        matrix.append(line.split(" "))
    f.close()

    return matrix


def solve_axb(filename):
    
    matrix = read_array(filename)
    items = []
    for i in matrix:
        for j in i:
            items.append(j.split(','))
    
    a = []
    b = []
    for i in items:
        a.append(i[0:3])
        b.append(i[3])
    
    A = np.matrix(a).astype(int)
    B = np.matrix(b).astype(int)

    return np.linalg.solve(A, B.transpose())    


print solve_axb('file')