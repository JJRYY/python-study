print("#하나만 출력1")
print()

print("#하나만 출력2", "abce", sep="\n", end="\n\n")
print("결과", end="\n\n")

print(type('홑따옴표'), type("하나만"), type(12), type(12.5), sep="\n", end="\n\n")

print("""\
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세\
""", end='\n\n')

# print('안녕하세요' + 1)

print("안녕하세요"[0])
print("안녕하세요"[0:2])
print("안녕하세요"[:3])
print("안녕하세요"[-3:-1])
print("안녕하세요"[-4:])
print()


hello = "안녕하세요"
print(type(hello), hello[0:2], hello, sep='\n', end='\n\n')

print(('안녕' + '하세요') * 3, end='\n\n')

# res = input('안녕?')
# print("입력한 답은 ", res)

a = "10 20 30 40 50".split(" ")
print(a)
print()




x, y, z = 10, 20, 30
print(x, y, z, sep='\n', end='\n\n')

x, y = y, x
print(x, y, sep='\n', end='\n\n')

