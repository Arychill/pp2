def gr_to_onc(grams):
    ounces = 28.3495231 * grams
    return ounces
print(gr_to_onc(10))

def far_to_cel(far):
    cel = (5 / 9) * (far - 32)
    return cel
print(far_to_cel(10))

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None
print(solve(14,60))

def is_prime(num):
    if(num < 2):
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if(is_prime(num))]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))

from itertools import permutations
def string_permutations(input_str):
    return [''.join(perm) for perm in permutations(input_str)]
print(string_permutations('abcd'))

def reverse_words(input_str):
    words = input_str.split()
    reversed_str = ' '.join(reversed(words))
    return reversed_str
print(reverse_words("We are ready"))

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 2, 3]))

def spy_game(num):
    sum = 0
    for i in range(len(num) - 1):
        if ((num[i] == 0) and (num[i+1] == 0) and (num[i+2] == 7)):
            sum+=1
    if sum == 0:
        return False
    else :return True
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))

import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume
print(sphere_volume(5))

def unique_elements(input_list):
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list
print(unique_elements([1,1,2,2,3,4,5,5,6,6,7,8,8,9,9,0,10]))

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('abba'))
print(is_palindrome('argyn'))

def histogram(nums):
    for num in nums:
        print('*' * num)
print(histogram([4, 7, 9, 6]))

import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    guesses = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        
        if guess == secret_number:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
guess_the_number()