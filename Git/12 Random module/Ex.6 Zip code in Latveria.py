def generate_index():
    from random import randrange as r
    from string import ascii_uppercase as a
    ln = len(a)
    result = a[r(ln)] + a[r(ln)] + str(r(100)) + "_" + str(r(100)) + a[r(ln)] + a[r(ln)]
    return result


print(generate_index())
