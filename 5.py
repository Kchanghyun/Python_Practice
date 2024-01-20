a='hobby'
print(a.count('y'))
print(a.find('b'))
print(" ".join(a))

b = " hi "
#공백 지우기
print(b.rstrip())
print(b.lstrip())
print(b.strip())

#대체
c = "Life is too short"
print(c.replace("Life", "Your leg"))

#토큰
print(c.split())
print(c.split('i'))