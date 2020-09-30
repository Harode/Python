import re

text = "This person's phone number is 800-830-2987 and my other number is 909-661-9287"

pattern = r'\d{3}-\d{3}-\d{4}'

match = re.findall(pattern,text)
match2 = re.search(pattern,text)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

match3 = re.search(phone_pattern,text)

print (match)
print (match2.group())
print (match3.group(1))

