def shell_sort(arr):
    size = len(arr)
    gap = size//2
    duplicate_ele_key = []
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i

            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = anchor

            if gap == 1 and arr[j-gap] == anchor:
                duplicate_ele_key.append(j-gap)

        gap = gap // 2

    print(duplicate_ele_key)


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    # for elements in tests:
    shell_sort(elements)
    print(elements)
