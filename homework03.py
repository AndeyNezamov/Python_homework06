from math import gcd
def Task3():
    print("\nЗадача 3:")
    max_denominator = 11
    fractions = simple_fractions(max_denominator)
    print("Несократимые дроби между 0 и 1 с знаменателем не больше", max_denominator)
    for fraction in fractions:
        print(f"{fraction[0]}/{fraction[1]}")

def is_coprime(a, b):
    return gcd(a, b) == 1

def simple_fractions(max_denominator):
    fractions = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(1, denominator):
            if is_coprime(numerator, denominator):
                fractions.append((numerator, denominator))
    return fractions

Task3()