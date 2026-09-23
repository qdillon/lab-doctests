def is_even(n):
  print(n)
  return n % 2 == 0


def is_odd(n):
    print(n)
    return not is_even(n)


colors = ["red", "green", "blue", "teal"]
for color in colors:
    print(color)

def factorial(n):
    '''
    Return n!
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    '''
    result = 1
    for i in range(n):
        result = result * i
    return result

print(factorial(10))

for i in range(0, 1001):
    print(i)