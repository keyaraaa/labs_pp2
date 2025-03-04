#task1
nums = [2, 3, 4, 5]
product = 1
for num in nums:
    product *= num 
print(product)

#task2
def count_case_letters(text):
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())

    print(uppercase_count)
    print(lowercase_count)

sample_text = "Hello KBTU!"
count_case_letters(sample_text)

#task3
def is_palindrome(string):
    cleaned_string = string.lower().replace(" ", "")  
    return cleaned_string == cleaned_string[::-1] 

word = "madam"
print(is_palindrome(word))

#task4
import time
number = 25100
delay_ms = 2123
time.sleep(delay_ms / 1000)
print(number ** 0.5)

#task5
def are_all_elements_true(tpl):
    return all(tpl)

tuple1 = (True, True, 1, "Hello")
tuple2 = (False, True, 0, "Hello")

print(are_all_elements_true(tuple1))
print(are_all_elements_true(tuple2))