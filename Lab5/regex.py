import re

#1
def match_ab_zero_or_more(s):
    return re.match(r'ab*', s) is not None

#2
def match_ab_two_to_three(s):
    return re.match(r'ab{2,3}', s) is not None

#3
def find_lowercase_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

#4
def find_uppercase_followed_by_lowercase(s):
    return re.findall(r'[A-Z][a-z]+', s)

#5
def match_a_anything_b(s):
    return re.match(r'a.*b$', s) is not None

#6
def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

#7
def snake_to_camel(s):
    return ''.join(word.title() if i else word for i, word in enumerate(s.split('_')))

#8
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

#9
def insert_spaces(s):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)

#10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

test_string_1 = "aabb"
test_string_2 = "abbbb"
test_string_3 = "hi_there"
test_string_4 = "HelloWorld"
test_string_5 = "aAnythingb"
test_string_6 = "hello, world. How are you?"
test_string_7 = "hello_world"
test_string_8 = "HelloWorldAgain"
test_string_9 = "helloWorld"
test_string_10 = "helloWorldTest"

(match_ab_zero_or_more(test_string_1), match_ab_two_to_three(test_string_2), 
find_lowercase_underscore(test_string_3), find_uppercase_followed_by_lowercase(test_string_4),
match_a_anything_b(test_string_5), replace_with_colon(test_string_6),
snake_to_camel(test_string_7), split_at_uppercase(test_string_8),
insert_spaces(test_string_8), camel_to_snake(test_string_9))
