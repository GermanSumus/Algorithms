"""
return the wanted value from a collection.
"""
def find_from(collection, find):
    for k, v in collection.items():
        if k == find or v == find:
            print(f'{k} ==> {v}')

c = {'root':'German', 'os':'Mac', 'German':22}
find_from(c, 'German')
