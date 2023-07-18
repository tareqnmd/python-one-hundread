number = int(input("Check this number : "))


def prime_number(num):
    if num == 2:
        return True
    elif num % 2 == 0 or num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True


if prime_number(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
