#task1
import re 

txt    = input("Enter : ")
result = re.search(r"ab*", txt)
print(result)
#task2
import re

txt    = input("Enter : ")
result = re.search(r"ab{2,3}", txt)
print(result)
#task3
import re

txt    = input("Enter : ")
result = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", txt)
print(result)
#task4
import re

txt    = input("Enter : ")
result = re.findall(r"\b[A-Z][a-z]+\b", txt)
print(result)
#task5
import re

txt    = input("Enter : ")
result = re.search(r"\ba.*b$\b", txt)
print(result)
#task6
import re

txt    = input("Enter : ")
result = re.sub("[ ,.]", ":", txt)
print(result)
#task7
import re

txt    = input("Enter : ")
result = re.sub("_([a-z])", lambda x : x.group(1).upper(), txt)
print(result)
#task8
import re

txt    = input("Enter : ")
result = re.split(r"(?<!^)(?=[A-Z])",txt)
print(result)
#task9
import re

txt    = input("Enter : ")
result = re.sub(r"(?<!^)(?=[A-Z])", lambda x : " " + x.group(0), txt)
print(result)
#task10
import re

txt    = input("Enter : ")
result = re.sub(r"[A-Z]", lambda x : "_" + x.group(0).lower(), txt)
print(result)