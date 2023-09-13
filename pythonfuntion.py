def hello():
    print("Hello World!")


hello()


def area(width=0, height=0):  # default parameters
    total = height * width
    return total


print('Area is', area(10, 20))
