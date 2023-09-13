numbers = {1: 'one', 2: 'two', 3: 'three'}
print(numbers)
print(type(numbers))
print(numbers[3])

people = {
    1: {
        "name": "John",
        "age": 19,
        "city": "bankok"
    },
    2: {
        "name": "Mary",
        "age": 20,
        "city": "bankok"
    }
}

print(people[1]["name"])
print(people[2]["name"])

print(numbers.keys())
print(numbers.values())

print(people.keys())
print(people.values())

for key, value in numbers.items():
    print(key, value)
    # people.keys(key, value)
row = 1
for key, value in people.items():
    print('row', row)
    for k, v in value.items():
        print(k, v)
        print("=============================")
        row += 1
    # print(key, value)
    # numbers.keys(key, value)
