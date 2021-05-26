def dan(num):
    for i in range(1, 10):
        print("{} * {} = {:2}".format(num, i, num*i))


def gugudan():
    for i in range(2, 10):
        dan(i)


def gugudan2():
    for i in range(2, 10):
        output = "{}단 ".format(i)
        for j in range(1, 10):
            output += "{} * {} = {:2} ".format(i, j, i * j)
        print(output)


def gugudan3():
    for i in range(1, 10):
        output = ""
        for j in range(2, 10):
            output += "{} * {} = {:2} ".format(j, i, i * j)
        print(output)


if __name__ == "__main__":
    gugudan3()