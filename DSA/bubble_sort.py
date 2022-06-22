import pprint
pp = pprint.PrettyPrinter(indent=4)


def bubble_sort(arr):
    size = len(arr)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


def buble_sort_advance(arr, key):
    size = len(arr)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    # load = [
    #     [5, 7, 2, 1, 33, 3, 9, 4],
    #     [],
    #     [1, 2, 3],
    #     [99],
    #     [102, 95, 75, 44]
    # ]

    # for element in load:
    #     bubble_sort(element)
    #     print(element)

    elements = [
        {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    buble_sort_advance(elements, key="device")
    pp.pprint(elements)
