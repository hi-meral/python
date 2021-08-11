ls = [10, 9, 8, 7, 6, 5,  4, 3, 2, 1, 11]

#x = ls[start:end:steps]

l = len(ls)
print(l)
print("for all index", ls[:l])
# for all index [3, 5, 8, 9, 2, 4, 1, 10, 22, 11]
print("got to 8 index only:", ls[2:9])  # got to 8 index only
# got to 8 index only: [8, 9, 2, 4, 1, 10, 22]
print("all print", ls[:])  # all print
# all print [3, 5, 8, 9, 2, 4, 1, 10, 22, 11]
print("all print", ls[::])  # all print
# all print [3, 5, 8, 9, 2, 4, 1, 10, 22, 11]
# print with three step start to end
print("print with three step start to end:", ls[::3])
# print with three step start to end: [3, 9, 1, 11]
# from minus indexing with two step
print("from minus indexing with two step:", ls[::-2])
# from minus indexing with two step: [11, 10, 4, 9, 5]
print("-1 to -7 with 2 step:", ls[-1:-7:-2])  # -1 to -7 with 2 step
# -1 to -7 with 2 step: [11, 10, 4]
