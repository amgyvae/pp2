import math
#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

#3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None, None

#4
def filter_prime(numbers):
    def is_prime(num):
        if num < 2: #to check 0 and 1
            return False
        for i in range(2, int(num**0.5) + 1):#**0.5 to check faster and more numbers
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

#5
from itertools import permutations
def string_permutations(input_str):
    return [''.join(perm) for perm in permutations(input_str)]

#6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#7
def has_consecutive_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def has_consecutive_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

#9
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#10
def unique_elements(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#11
def isPalindrome(s):
    return s == s[::-1]
 
#12
def histogram(numbers):
    for num in numbers:
        bar = '*' * num
        print(bar)

#13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Hello! What is your name?")
    name = input()
    print(name, "Well,", name,", I am thinking of a number between 1 and 20. Take a guess.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Good job, {name} ! You guessed my number in {attempts} guesses.")
            break

guess_the_number()

