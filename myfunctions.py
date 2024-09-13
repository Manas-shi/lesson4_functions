def simple_separator():
    symbol = "*"
    return symbol * 10

print(simple_separator())

def long_separator(count):
    symbol = "*"
    return symbol * count

print(long_separator(3))
print(long_separator(4))

def separator(symbol, count):
    return symbol * count

print(separator('-', 10))
print(separator('#', 5))

def hello_world():
    asterisk = "*"
    line_break = "\n\n"
    string = "Hello World!"
    cleaned_string = string.lstrip()
    hash_symbol = "#"
    cleaned_hash = hash_symbol.lstrip()
    print(asterisk * 10, line_break, cleaned_string, line_break, cleaned_hash * 10)

hello_world()

def hello_who(who='World'):
    asterisk = "*"
    line_break = "\n\n"
    greeting = f"Hello {who}!"
    greeting_cleaned_case = greeting.lstrip()
    hash_symbol = "#"
    cleaned_hash = hash_symbol.lstrip()
    print(asterisk * 10, line_break, greeting_cleaned_case, line_break, cleaned_hash * 10)

hello_who("Manarbek")

def pow_many(power, *args):
    result = sum(args) ** power
    return result

print(pow_many(1, 1, 2))
print(pow_many(1, 2, 3))
print(pow_many(2, 1, 1))
print(pow_many(3, 2))
print(pow_many(2, 1, 2, 3, 4))

def print_key_val(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} --> {value}")


print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):
    new_iterable = []
    for item in iterable:
        if function(item):
            new_iterable.append(item)
    return new_iterable

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))



