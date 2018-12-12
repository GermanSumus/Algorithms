# return true if given string wnds with target letter
def end_letter(string, target):
    print(string.endswith(target))
    print(f'{string} ends with {target}\n')

end_letter('yes', 's')
end_letter('maybe?', 'e')
end_letter('hello', 'o')

