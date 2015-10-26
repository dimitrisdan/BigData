def read_array(input):

    f = open(input, 'r')
    matrix = []
    for line in f.read().split('\n'):
        matrix.append(line.split(" "))
    f.close()

    return matrix


def write_array(arr, output):

    f = open(output, 'w')
    for i in arr:
        for j in i:
            f.write(str(j) + ' ')
        f.write('\n')
    f.close()

array_ = read_array('2_1')
write_array(array_, '2_1_out')