def squares_generator(N):
    for i in range(N):
        yield i ** 2

N = int(input("input num: "))
for square in squares_generator(N):
    print(square)



def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a value for n: "))
even_numbers = list(even_numbers_generator(n))
print("Even numbers between 0 and", n, ":", ', '.join(map(str, even_numbers)))



def div_by_3_and_4_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a value for n: "))
for number in div_by_3_and_4_generator(n):
    print(number)


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("input a: "))
b  =int(input("input b: "))
for square in squares(a, b):
    print(square)


def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter n for countdown: "))
for number in countdown_generator(n):
    print(number)