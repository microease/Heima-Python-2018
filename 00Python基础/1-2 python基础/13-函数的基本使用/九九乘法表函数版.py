def multiple_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d*%d=%d" % (j, i, i * j), end="\t")
            j += 1
        print("")
        i += 1