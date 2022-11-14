import timeit


def nonequal(a, b, c, d):
    if a != b and a != c and a != d and b != c and b != d and c != d:
        return True
    else:
        return False


count = 0
for a in range(1, 33):
    for b in range(2, 33):
        for c in range(3, 33):
            for d in range(4, 33):
                if nonequal(a, b, c, d) and ((a ** 3) + (b ** 3)) == ((c ** 3) + (d ** 3)):
                    print(a, b, c, d, ((a ** 3) + (b ** 3)))
                    count += 1
                if count == 10:
                    a = 32
                    b = 32
                    c = 32
                    d = 32
