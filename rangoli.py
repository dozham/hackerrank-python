# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import string

en_chars = string.ascii_lowercase


def print_rangoli(size):
    half_bottom = []
    for i in range(n):
        half_line = en_chars[i:size]
        full_line = half_line[::-1] + half_line[1:]
        half_bottom.append('-'.join(full_line).center(4 * size - 3, '-'))

    rangoli = half_bottom[::-1] + half_bottom[1:]
    print('\n'.join(rangoli))

    ## WRONG
    # def get_line_chars(n):
    #     return en_chars[1:n][::-1] + en_chars[:n]
    # for i in list(range(1, size+1)) + list(range(size-1, 0, -1)):
    #     print('-'.join(get_line_chars(i)).center(4*size-3, '-'))


if __name__ == '__main__':
    # n = int(input())
    n = 4
    print_rangoli(n)
