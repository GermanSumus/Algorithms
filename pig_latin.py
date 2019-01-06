"""
Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word,
moves it to the end of the word and suffixes an "ay".

If a word begins with a vowel you just add "yay" to the end.

Input strings are guaranteed to be English words in all lowercase.

"""


def pig_latin(string):
    split_string = string.split(' ')
    pig_string = ''
    for word in split_string:
        cluster = ''
        if word[0] in 'aeiou':
            pig = word + 'yay '
            pig_string += pig
        else:
            for letter in word:
                if letter.lower() not in 'aeiou':
                    cluster += letter
                else:
                    break
            pig = word[len(cluster):] + cluster + 'ay '
            pig_string += pig

    print(pig_string)

    
pig_latin('air')
pig_latin('a test')
pig_latin('how are you')
pig_latin('german')
pig_latin('passes')
pig_latin('failed')
