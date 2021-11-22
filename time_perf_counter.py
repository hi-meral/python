import time


a = time.perf_counter()


l = list(range(1, 100000))

for x in l:
    print(x)

b = time.perf_counter()


print(f'Execution Time : {b-a}')
