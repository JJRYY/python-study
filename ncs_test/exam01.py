def gugudan():
    for i in range(1, 10):
        output = ""
        for j in range(2, 10):
            output += "{} * {} = {:2}   ".format(j, i, i * j)
        print(output)


if __name__ == "__main__":
    gugudan()