import time


a = time.perf_counter()


l = list(range(1, 100000))

for x in l:
    print(x)

b = time.perf_counter()

print(f'Execution Time for List : {b-a}')

time.sleep(3)

t = tuple(range(1, 100000))

c = time.perf_counter()

for x in t:
    print(x)

d = time.perf_counter()


print(f'Execution Time Tuple: {d-c}')
