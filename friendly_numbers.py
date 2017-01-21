""" the goal of this algorithm is to identify all friendly number groups
        in a specific range of numbers
    the index is going to be the abundancy of the numbers, which is the
        of the numbers divisors divided by the number itself
    for example:
        divisors of 12 are: 1, 2, 3, 4, 6, 12
        the sum of those divisors is: 1 + 2 + 3 + 4 + 6 + 12 = 26
        the abundancy of 12 is: 28/12 = 7/3 or 2.333 repeating"""


def friendly_numbers(start, end):

    f_numbers = {}  # result dictionary to store friendly numbers
    abndncy_dict = {}  # intermediate dictionary to store abundancies

    for i in range(start, end):
        div_list = []  # create set containing all divisors for the iterator
        for k in range(1, (i/2)+1):  # check every number up to half of the iterator
            if i % k == 0:  # if the remainder is zero the number is a divisor
                div_list.append(k)  # add all divisors to a list
            else:
                continue  # continue through the loop if remainder isn't zero
        abundancy = sum(div_list)/i  # calculate abundancy for current iterator
        abndncy_dict.setdefault(abundancy, [])  # set default to abundancy if it is missing
        abndncy_dict[abundancy].append(i)  # add the iterator to the list for each abundancy

    for abundancy in abndncy_dict.keys():  # iterate through each abundancy value
        if len(abndncy_dict[abundancy]) > 1:  # check if each abundancy has more than one number
            f_numbers.setdefault(abundancy, [])  # set default key for dictionary
            f_numbers[abundancy].append(abndncy_dict[abundancy])  # add friendly groups to dict

    return f_numbers

results = friendly_numbers(1, 10001)

print(results)
