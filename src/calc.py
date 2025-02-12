def devide(x, y):
    if y == 0:
        raise ValueError('деление на ноль невозможно')
    return x / y
def reverse_string(my_string):
    return my_string[::-1]

def hello(word):
    return f'Hello {word}'


print(hello('Vera'))

