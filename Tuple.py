import sys
import platform
import time

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

t = tuple(zip(a, b))

print(t)
print(type(t))
print(t[0])
print(t[0][1])

a_list = []
a_Tuples = ()

a_list = ["test", "For", "Memory"]
a_Tuples = ("test", "For", "Memory")

print(sys.getsizeof(a_list), 'bty')
print(sys.getsizeof(a_Tuples), 'bty')

v_list = list(range(100000001))
v_Tuple = tuple(range(100000001))

start = time.time_ns()
for i in range(len(v_list)):
    a = v_list[i]
end = time.time_ns()
print('total memory list:', end - start)

start = time.time_ns()

for i in range(len(v_Tuple)):
    a = v_Tuple[i]
end = time.time_ns()
print('total memory Tuple:', end - start)
