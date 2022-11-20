def swap_case(s):
    def toggle_case(c):
        if c.isupper():
            return c.lower()
        else:
            return c.upper()

    return ''.join([toggle_case(c) for c in s])


if __name__ == '__main__':
    print(swap_case(input()))
