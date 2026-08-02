# Regular Expressions re Module
# 1. import the re module
import re
# re.search()
# text="my age is 24"
# match=re.search(r"\d+",text)
# if match:
#     print(match.group())

# re.findall
# text="Marks : 40 30 23"
# numbers = re.findall(r"\d+",text)
# print(numbers)

# re.sub()

# text="python is easy"
# new_text=re.sub("easy","powerfull",text)
# print(new_text)

# Quetsion

# text="ali 23 ahmad 45 sara 19"
# new_text=re.findall(r"\d+",text)
# print(new_text)

# q2
text="the cat is sleeping"
new_text=re.sub("cat","dog",text)
print(new_text)