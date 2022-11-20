VOWELS = 'AEIOU'


def minion_game(string):
    scores = {'Stuart': 0, 'Kevin': 0}
    n = len(string)
    for i in range(n):
        if string[i] in VOWELS:
            scores['Kevin'] += n - i
        else:
            scores['Stuart'] += n - i

    if scores['Kevin'] > scores['Stuart']:
        print(f"Kevin {scores['Kevin']}")
    elif scores['Kevin'] < scores['Stuart']:
        print(f"Stuart {scores['Stuart']}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
