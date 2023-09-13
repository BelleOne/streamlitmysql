class Person:
    # property
    __name = ''
    __age = 0

    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    # Create object  + 'is ' + str(self.__age)

    def get_profile(self):
        return self.__name + 'is ' + str(self.__age)

    def __del__(self):
        return True

# Create object


person1 = Person('john', 25)

print(person1.get_name())
print(person1.get_age())
print(person1.get_profile())

person2 = Person('Bell', 55)

print(person2.get_name())
print(person2.get_age())
print(person2.get_profile())


person3 = Person('Bells', 55)

print(person3.get_name())
print(person3.get_age())
print(person3.get_profile())
