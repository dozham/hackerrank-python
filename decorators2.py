import operator


def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key=lambda x: int(x[2]))]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    # people = [input().split() for i in range(int(input()))]
    people = '''
    Mike Thomson 20 M
    Robert Bustle 32 M
    Andria Bustle 30 F
    '''
    # Jake Jake 42 M
    # Jake Kevin 57 M
    # Jake Michael 91 M
    # Kevin Jake 2 M
    # Kevin Kevin 44 M
    # Kevin Michael 100 M
    # Michael Jake 4 M
    # Michael Kevin 36 M
    # Michael Michael 15 M
    # Micheal Micheal 6 M'''
    people = [p.strip().split() for p in people.split(sep='\n') if len(p.strip()) > 0]

    print(*name_format(people), sep='\n')
