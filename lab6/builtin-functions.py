from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [2, 3, 4, 5]
print("Multiplication of numbers:", multiply_list(numbers))


def count_case_letters(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    
    return upper_count, lower_count

input_str = "Hello World, it's Moldabek Argyn"
upper, lower = count_case_letters(input_str)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")


def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

palindrome_str = "anna annA"

if is_palindrome(palindrome_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


import time
import math

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result


number_to_sqrt = 25100
delay_milliseconds = 2123

result = square_root(number_to_sqrt, delay_milliseconds)
print(f"Square root of {number_to_sqrt} after {delay_milliseconds} milliseconds is {result}")


def all_true_elements(input_tuple):
    return all(input_tuple)

bool_tuple = (True, True, False, True)

if all_true_elements(bool_tuple):
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")