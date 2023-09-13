number = [-1, 2, 3, 5, 6]

print(number)
print(number[3])
print(number[-1])
print(number[1:3])
print(number[:3])
print(number[1:])
print(number[:])
print(number[::2])
print(number[::-1])

persons = ['bell', 'john', 'fred', 'jack']

for person in persons:

    print(persons)

# add data in person
persons.append('jim')
print(persons)

persons[0] = 'johny'
print(persons)

persons.remove('johny')
persons.pop(1)
print(persons)

print(len(persons))
