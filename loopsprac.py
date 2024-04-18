for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print(a, "is a multiple of both 3 and 5")
    elif a % 3 == 0:
        print(a, "is a multiple of 3")
    elif a % 5 == 0:
        print(a, "is a multiple of 5")
    else:
        print(a)

