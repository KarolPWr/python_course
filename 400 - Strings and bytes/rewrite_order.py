def display_enumerated_lines(filename):
    """Display lines of files with line number as prefix
    use `enumerate` function"""
    with open(filename, 'r') as f:
        lines = f.readlines()
        for index,line in enumerate(lines):
            print(index, line)


def reverse_lines_y(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed_y'
    e.g.
    a b  >  b a
    c d     d c
    """
    with open(filename, 'r') as f, open('./data/matrix_reversed_y', 'w') as reversed:
        for line in f.readlines():
            reversed_line = line[::-1].strip() + '\n'
            reversed.write(reversed_line)


def reverse_lines_x(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed_x'
    e.g.
    a b  >  c d
    c d     a b
    """
    with open(filename, 'r') as f, open('./data/matrix_reversed_x', 'w') as reversed:
        for line in f.readlines():
            reversed.write(line)



def reverse_lines(filename):
    """Reads data from `<filename>` and writes reversed lines to file `<filename>_reversed'
    e.g.
    a b  >  d c
    c d     b a
    """
    with open(filename, 'r') as f, open('./data/matrix_reversed', 'w') as reversed:
        content = f.read()
        reversed.write(content[::-1])


if __name__ == '__main__':
    filename = './data/matrix'

    display_enumerated_lines(filename)
    reverse_lines_x(filename)
    reverse_lines_y(filename)
    reverse_lines(filename)
