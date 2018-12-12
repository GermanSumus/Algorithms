# Reverse the given string and print it out
def reverse_me(string):
    temp = list(string)
    temp.reverse()
    reverse = ''
    for _ in temp:
        reverse += _

    print(reverse)

reverse_me('Hello')
reverse_me('This is a long string to reverse')
reverse_me('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
