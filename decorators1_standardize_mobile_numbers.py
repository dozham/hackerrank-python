import re


def wrapper(func):
    def fun(l):
        # func(['+91 ' + ' '.join(re.search(r"^(?:0|\+?91)?(\d{5})(\d+)", phone).groups()) for phone in l])
        func(f'+91 {phone[-10:-5]} {phone[-5:]}' for phone in l)  # This is different!

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    # l = [input() for _ in range(int(input()))]
    l = ["07895462130", "919875641230", "9195969878"]
    sort_phone(l)
