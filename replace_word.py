"""
Perform a search and replace on the sentence using the arguments provided and
return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with (after).

Note
Preserve the case of the first character in the original word when you are
replacing it. For example if you mean to replace the word "Book" with the word
"dog", it should be replaced as "Dog". 
"""

def replace_this(string, find_this, insert_this):
    split_string = string.split(' ')
    new_string = ''
    for word in split_string:
        if word == find_this:
            if word[0].isupper():
                repl = insert_this.title()
                new_string += repl + ' '
            else:
                repl = insert_this
                new_string += insert_this + ' '
        else:
            new_string += word + ' '
    print(new_string)


replace_this('in here replace this', 'this', 'that')
replace_this('Rick is my name', 'Rick', 'german')
