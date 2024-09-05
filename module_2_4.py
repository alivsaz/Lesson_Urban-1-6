# Цикл for. Элементы списка. Полезные функции в цикле
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'\nИсходный код: \nnumbers = {numbers}')
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    if numbers[i] == 1:
        continue
    else:
        for j in range(2, numbers[i]-1):
            if numbers[i] % j == 0:
                is_prime = False
                break
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(f'\nВывод на консоль: \nPrimes: {primes} \nNot Primes: {not_primes}')
