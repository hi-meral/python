with open("text.txt", "rt") as f:

    # print(f.seekable())
    f.seek(105)

    print(f.tell())
    # f.truncate(50)

    for c in f:
        print(c)
