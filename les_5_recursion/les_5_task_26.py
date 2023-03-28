# степень числа
def func1_pow(m, n):
    counter = abs(n)
    if n == 0:
        return 1
    elif n == 1:
        return m
    elif n == -1:
        return 1 / m
    else:
        if n < -1:
            return 1 / (m * func1_pow(m, counter - 1))  #отриц. показатель ст.
        else:
            return m * func1_pow(m, counter - 1)  #положительный показатель ст.


m = int(input("Введите основание степени "))
n = int(input("Введите показатель степени "))
print(func1_pow(m, n))
