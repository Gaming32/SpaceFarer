"""
Heavily updated from sayamqazi's planet-name-generator
https://github.com/sayamqazi/planet-name-generator
"""


import random


__all__ = ['PLANETS', 'SYLLABLES', 'DIV_INDEX', 'FREQ', 'generate_planet_name']


PLANETS = []
total_syllables = 0
SYLLABLES = []

with open('planet-names.txt', 'r') as fp:
    for p in fp:
        p = p.strip()
        if not p:
            continue
        PLANETS.append(p)
        lex = p.split('-')
        total_syllables += len(lex)
        for l in lex:
            if l not in SYLLABLES:
                SYLLABLES.append(l)

DIV_INDEX = len(SYLLABLES) / total_syllables

size = len(SYLLABLES) + 1
FREQ = [[0] * size for i in range(size)]

for p in PLANETS:
    lex = p.split('-')
    i = 0
    while i < len(lex) - 1:
        FREQ[SYLLABLES.index(lex[i])][SYLLABLES.index(lex[i+1])] += 1
        i += 1
    FREQ[SYLLABLES.index(lex[len(lex) - 1])][size-1] += 1

suffixes = ['prime', '',
            'B', '',
            'alpha', '',
            'proxima', '',
            'IV', '',
            'V', '',
            'C', '',
            'VI', '',
            'VII', '',
            'VIII', '',
            'X', '',
            'IX', '',
            'D', '',
            '', '']


def generate_planet_name(random: random.Random = random) -> str:
    planet_name = ''
    length = random.randint(2, 3)
    initial = random.randint(0, size - 2)
    while length > 0:
        while 1 not in FREQ[initial]:
            initial = random.randint(0, size - 2)
        planet_name += SYLLABLES[initial]
        initial = FREQ[initial].index(1)
        length -= 1
    suffix_index = random.randint(0, len(suffixes) - 1)
    planet_name += ' '
    planet_name += suffixes[suffix_index]
    return planet_name


def main():
    div_index_str = str(DIV_INDEX)[:4]

    print('planets:', len(PLANETS))
    print('syllables:', len(SYLLABLES))
    print('diversity analysis:', div_index_str)

    print()
    for _ in range(20):
        print(generate_planet_name())


if __name__ == '__main__':
    main()
