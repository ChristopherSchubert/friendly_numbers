""" the goal of this algorithm is to identify all friendly number groups
        in a specific range of numbers
    the index is going to be the abundancy of the numbers, which is the
        of the numbers divisors divided by the number itself
    for example:
        divisors of 12 are: 1, 2, 3, 4, 6, 12
        the sum of those divisors is: 1 + 2 + 3 + 4 + 6 + 12 = 28
        the abundancy of 12 is: 28/12 = 7/3 or 2.333 repeating"""
import time


def friendly_numbers(start, end):

    friends = {}  # result dictionary to store friendly numbers
    abundancies = {}  # intermediate dictionary to store abundancies

    for number in range(start, end + 1):

        divisors = []  # create set containing all divisors for the iterator

        for potential_divisor in range(1, int(number / 2) + 1):  # check every number up to half of the iterator
            if number % potential_divisor == 0:  # if the remainder is zero the number is a divisor
                divisors.append(potential_divisor)  # add all divisors to a list

        abundancy = sum(divisors) / number  # calculate abundancy for current iterator

        if abundancy not in abundancies:
            abundancies[abundancy] = []  # prepare if abundancy is new

        abundancies[abundancy].append(number)  # add the iterator to the list for each abundancy

    for abundancyKey in abundancies.keys():  # iterate through each abundancy value

        if len(abundancies[abundancyKey]) > 1:  # check if each abundancy has more than one number

            if abundancyKey not in friends:
                friends[abundancyKey] = []  # set default key for dictionary

            friends[abundancyKey].append(abundancies[abundancyKey])  # add friendly groups to dict

    return friends

iterations = 10
start_limit = 100
multiplier = 2

limits = []

for iteration in range(0, iterations):

    if len(limits) == 0:
        limits.append(start_limit)
    else:
        limits.append(limits[iteration - 1] * 2)


for limit in limits:

    start_time = time.time()

    results = friendly_numbers(1, limit)

    end_time = time.time()
    print("Limit: " + str(limit).rjust(8) + ";  Friends#: " + str(len(results)).rjust(5) + ";  Time(s): " +
          str(end_time - start_time).rjust(25) + ";  Friends: " + str(results))

