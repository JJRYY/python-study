def mul(*values):
    a = 1
    for value in values:
        a *= value
    return a

print(mul(5, 7, 9, 10))