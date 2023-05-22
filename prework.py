# 1 Print Hello_USERNAME

# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function.
def hello_name(user_name):
    """This is a function that prints hello_USERNAME!"""
    return "hello_" + user_name + "!"


print(hello_name("cOoLgUy420"))


# def hello_name2(user_name):
#     print("\nHello, " + user_name.title() + "! Have a great day!")

# hello_name2("stephen")


# def hello_name3(user_name):
#     print(f"hello_{user_name.upper()}!")


# hello_name3("username")


# def hello_name4(user_name):
#     print("hello_" + user_name + "!")

# hello_name4("megaman")

# Number 2 - Print the first odd Numbers between 1 and 100
def first_odds():
    for num in range(1, 101):
        if num % 2 == 1:
            print(num)


print(first_odds())


# def first_odd2():
#     number = 0
#     while number < 100:
#         number += 1
#         if number % 2 == 0:
#             continue

#         print(number)

# first_odd2()


# def first_odds3():
#     '''Prints odd numbers from 1-100 and
#     returns nothing.'''
#     odds = list(range(1, 100, 2))
#     print(odds)
#     return None


# print(first_odds3())


# for i in range(1, 101, 2):
#     print(i)


# Parameter	Description
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop(not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

# Write a function that returns the maximum number in a given list
def max_num_in_list(a_list):
    output = max(a_list)
    print("\nMaximum number in a list is " + str(output) + ".")


def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num


a_list = [1, 1000000, 88, 1234, 9209, 411, 9, 999999999]
print("maxboii", max_num_in_list(a_list))


def max_num_in_list(a_list):
    '''Function will print highest number 
    in a list.'''
    digits = a_list
    print(max(digits))


nums = [1, 34, 4, 3, 37, 20]
max_num_in_list(nums)


def max_num_in_list(a_list):
    """
    Get the max of some list. 
    """
    m = a_list[0]
    for n in a_list:
        if n > m:
            m = n
    return m


def max_num_in_list():
    maxnumber = max(a_list)
    print(maxnumber)


max_num_in_list()


def max_num_in_list(a_list):
    a_list.sort()
    return a_list.pop()


def max_num_in_list(b_list):
    """This function takes a list and returns the largest number"""
    return max(b_list)


print(max_num_in_list([76, 78, 999, 3677, 10]))
print("\n")


# question 4 write a function to return if the given year is a leap year.
# def is_leap_year(a_year):
#     if a_year % 4 == 0:
#         return True
#     if a_year % 100 != 0:
#         return True
#     if a_year % 400 == 0:
#         return True
#     else:
#         return False


# a_year = 1984
# if is_leap_year(a_year):
#     print("It's a leap year!?!")
# else:
#     print("Nope.")


# def is_leap_year(a_year):
#     '''Function will tell us if a given year is 
#     a leap year.'''
#     if a_year % 4 == 0 and a_year % 100 != 0:
#         return True
#     elif a_year % 400 == 0:
#         return True
#     else:
#         return False


# print(is_leap_year(2008))


# def is_leap_year(a_year):
#     """Tests if a year is a leap year"""
#     if a_year % 100 == 0 and a_year % 400 == 0:
#         return True
#     elif a_year % 4 == 0:
#         return True
#     else:
#         return False


# print(is_leap_year(2024))


def is_leap_year(a_year):
    if not (a_year % 4): 
        print(a_year % 4)
        if a_year % 100:
            print(a_year % 100)
            leapyear = True
    else:
        leapyear = False
    print(leapyear)


is_leap_year(2020)


# def is_leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     else:
#         return False


# print(is_leap_year(1996))


# def leap_year(year):
#     return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)


# 5 write a function to check if all numbesr in a list are consecutive
def is_consecutive(a_list):
    b_list = list(range((a_list[0]), (a_list[-1]), 1))
    b_list.append(a_list[-1])
    if a_list == b_list:
         return True
    else:
        return False


def is_consecutive(a_list):
    a_list.sort()
    for num in range(len(a_list) - 1):
        if a_list[num] + 1 != a_list[num + 1]:
            return False
    return True


a_list = [1, 2, 3, 4]
print(is_consecutive(a_list))


def is_consecutive(a_list):
    '''Will return True or False if a list of numbers 
    is consecutive.'''
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))


a_list = [4, 5, 6, 7, 8]
print(is_consecutive(a_list))
