def BOH(num):
    binary = bin(num)
    octo = oct(num)
    hexa = hex(num)
    print(binary[2:])
    print(octo[2:])
    print(hexa[2:].upper())


num = int(input())
BOH(num)
