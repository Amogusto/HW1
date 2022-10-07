n = int(input("Введите число"))
res = 0
while (n // 10) > 0:
    num1 = n % 10
    n = n // 10
    num2 = n % 10

    if num1 > num2:
        if num1 > res:
            res = num1
    else:
        if num2 > res:
            res = num2

print(res)