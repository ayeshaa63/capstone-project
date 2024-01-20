# mind reader game
# User thinks of a number between 1 and 20 and the programme guesses it through a series of questions

# narrowing down where the mystery number is

def sectioning():
    numbers = []
    for i in range(20):
        numbers.append(i + 1)

    is_greater_than_10 = input(
        'Think of a number between 1 and 20 then answer the following questions. Is your number greater than 10? (yes/no)')
    if is_greater_than_10.lower() == "yes":
        numbers = numbers[10:]

        is_greater_than_15 = input("Is your number greater than 15? (yes/no)")
        if is_greater_than_15.lower() == "yes":
            numbers = numbers[5:]
        elif is_greater_than_15.lower() == "no":
            numbers = numbers[:5]
        else:
            print("Invalid input")

    elif is_greater_than_10.lower() == "no":
        numbers = numbers[:10]

        is_greater_than_5 = input("Is your number greater than 5? (yes/no)")
        if is_greater_than_5.lower() == "yes":
            numbers = numbers[5:]
        elif is_greater_than_5.lower() == "no":
            numbers = numbers[:5]
        else:
            print("Invalid input")

    else:
        print("Invalid input")
    return numbers

# using divisors to eliminate numbers


def divisors(numbers):

    mod_3_is_0 = [n for n in numbers if n % 3 == 0]
    mod_3_is_1 = [n for n in numbers if n % 3 == 1]
    mod_3_is_2 = [n for n in numbers if n % 3 == 2]

    is_even = input("Is your number even? (yes/no)")
    if is_even.lower() == "yes":
        for num in numbers:
            if num % 2 == 1:
                numbers.remove(num)
    elif is_even.lower() == "no":
        for num in numbers:
            if num % 2 == 0:
                numbers.remove(num)
    else:
        print('Invalid input')

    mod_3 = input(
        "What is the remainder when your number is divided by 3? (0/1/2)")
    if int(mod_3) == 0:
        numbers = list(set(numbers).intersection(mod_3_is_0))
    elif int(mod_3) == 1:
        numbers = list(set(numbers).intersection(mod_3_is_1))
    elif int(mod_3) == 2:
        numbers = list(set(numbers).intersection(mod_3_is_2))
    else:
        print("Sorry it needs to be an integer from [0, 1, 2]")
    guess = f'Your number is {numbers[0]}!'
    return guess


print(divisors(sectioning()))
