#Task1
def ounces(n):
    print(n * 28.3495231)
a = int(input())
b = ounces(a)

#Task2
def cels(n):
    print(((n-32)*5)/9)
c = int(input())
b = cels(c)

#Task3
def solve(heads, legs):
    a = (4*heads-legs)/2
    x = heads - a
    print(x, "rabbits and ",  a, "chickens")
b = solve(35, 94)

#Task4
import math
def filter_prime(args):
    
    for i in args:
        prime = True
        if i < 2:
            prime = False
        else:
           for j in range(2, int(math.sqrt(i))+1):
               if i%j==0:
                   prime = False 
        if prime:
            print (i)

number = list(map(int, input(). split()))

c = filter_prime(number)

#Task5
def permute(data, i, length): 
    if i==length: 
        print(''.join(data) )
    else: 
        for j in range(i,length): 
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i]  
  

string = input()
n = len(string) 
data = list(string) 
permute(data, 0, n)

#Task6
def revers(st):
    words = st.split()
    revwords = words[::-1]
    revsentence = ' '.join(revwords)
    print(revsentence)
sentence = input()
revers(sentence)

#Task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


n = map(int,input().split())
m = list(n)
print(has_33(m))

#Task8
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == code[idx]:
            idx += 1
        if idx == 3:
            return True
    return False


a = map(int,input().split())
n = list(a)
print(spy_game(n))

#Task9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

n = int(input())
print(sphere_volume(n)) 

#Task10
def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

a = map(int,input().split())
n = list(a)
print(unique_elements(n))  

#Task11
def is_palindrome(word):
    word = word.replace(" ", "").lower() 
    return word == word[::-1]

a = input()
print(is_palindrome(a))

#Task12
def histogram(nums):
    for num in nums:
        print('*' * num)

a = map(int,input().split())
n = list(a)
histogram(n)  

#Task13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()