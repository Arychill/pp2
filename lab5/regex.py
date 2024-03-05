import re

pattern = re.compile(r'ab*')
string = 'abbbb'
if pattern.fullmatch(string):
    print("Match!")
else:
    print("No match.")


pattern = re.compile(r'ab{2,3}')
string = 'abb'
if pattern.fullmatch(string):
    print("Match!")
else:
    print("No match.")



pattern = re.compile(r'[a-z]+_[a-z]+')
string = 'example_text'
matches = pattern.findall(string)
print(matches)


pattern = re.compile(r'[A-Z][a-z]+')
string = 'CamelCaseExample'
matches = pattern.findall(string)
print(matches)


pattern = re.compile(r'a.*b$')
string = 'aanythingb'
if pattern.fullmatch(string):
    print("Match!")
else:
    print("No match.")

pattern = re.compile(r'[ ,.]+')
string = 'This is, a sample. String'
result = pattern.sub(':', string)
print(result)

def snake_to_camel(snake_case):
    words = snake_case.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

snake_case_string = 'snake_case_example'
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)


pattern = re.compile(r'[A-Z][a-z]*')
string = 'SplitThisString'
result = pattern.findall(string)
print(result)


pattern = re.compile(r'([a-z])([A-Z])')
string = 'InsertThisString'
result = pattern.sub(r'\1 \2', string)
print(result)


def camel_to_snake(camel_case):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case).lower()

camel_case_string = 'CamelCaseExample'
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)