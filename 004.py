#Problem 4

#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def es_palindromo(n):
    return str(n) == str(n)[::-1]

palindromo_max = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        producto = i * j
        if es_palindromo(producto) and producto > palindromo_max:
            palindromo_max = producto

print(palindromo_max)

