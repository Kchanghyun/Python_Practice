# string formatting

a = "I eat %d apples." % 3
print(a)

b = "I eat %s apples." %"five"
print(b)
print("I ate %d apples. so I was sick for %s days." %(10,"three"))

print("I hava %s apples." %3)
print("rate is %s" %3.234)

print("Error is %d%%" %98)

print("%10s" %"hi")
print("%-10sjane" %"hi")
print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)
# ========================================================
print("\n")
print("I eat {0} apples.".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(10, "three"))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3))
number = 20
dayday = 5
print("I ate {0} apples. so I was sick for {1} days.".format(number, dayday))
# ========================================================
print("\n")
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

d = {'name' : '홍길동', 'age' :30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

x = "python"
print(f'{x:!^12}')