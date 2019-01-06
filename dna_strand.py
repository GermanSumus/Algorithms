"""
The DNA strand is missing the pairing element. Take each character, get its
pair, and return the results as a 2d array.

Base pairs are a pair of AT and CG. Match the missing element to the provided
character.

Return the provided character as the first element in each array.

For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]

The character and its pair are paired up in an array, and all the arrays are
grouped into one encapsulating array.
"""

def dna(dna_string):
    # DNA string will be only AT or GC
    dna = []
    for letter in dna_string:
        if letter == 'a':
            dna.append(['a', 't'])
        elif letter == 't':
            dna.append(['t', 'a'])
        elif letter == 'g':
            dna.append(['g', 'c'])
        else:
            dna.append(['c', 'g'])

    print(dna)


dna('gcg')
