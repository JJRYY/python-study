def test():
    return (10, 20)

print(test(), type(test()))
a, b = test()
print("a:", a, "b:", b, end='\n\n')
