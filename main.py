# print("Soso")

# print("inga")

# for i in range(10):
    
#     print("Saba")

    
#     if 5 > 10:
#         print("Yes")
#         else:
#          print("No")

#  normal_rate = 80
#  heart_rate = 100

#  if heart_rate > normal_rate:
#     print("Are You WorkingOut?")
#     else:
#     print("Your Heart Rate Is Normal!")


# for num in range(1, 11): # 1 დან 10 ამდე ციფრები
#     print(num)

# x = ['hi', 'hello', 'welcome'] # Dictionare
# print(x[2])

# bad_dict = {
#     ["52" : "fiftytwo"]
# }

# person = {
#     "name": "Soso",
#     "age": 15,
#     "location": "Gurjaani",
#     "interests": ["programming"],
# }

# print("Name:", person["name"])
# print("Age:", person["age"])
# print("Location:", person["location"])
# print("Interests:", person["Interests"])




# def register_user(): # Register person
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     interests = input("Enter your interests (comma-separated): ").split(',')

#     user_info = {
#         "name": name,
#         "age": age,
#         "interests": interests
#     }

#     return user_info

# def fetch_dependency(user_info, key):
#     value = user_info.get(key, "Key not found")
#     return value

# print("Welcome! Let's register you.")
# new_user_info = register_user()

# dependency_key = input("Enter the dependency you want to fetch: ")
# dependency_value = fetch_dependency(new_user_info, dependency_key)

# print(f"Dependency '{dependency_key}': {dependency_value}")


# def register_user():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     interests = input("Enter your interests")
    
#     return {
#         "name"
#         "age"
#         "interests"
#     }
    
#     user_data = register_user()
    
#     def fetch_dependency (dependencies, key):
#         return dependencies.get(key, "key not found")
    
#     dependencies = {
#         "Goa" : "Programming academy"
#         "Python" : "Programming language"
#         "Javascript" : "Programming language"
#     }
    
#     dependency_key = input("Enter the dependency: ")
#     result = fetch_dependency(dependencies, dependency_key)
#     print(result)
    
    
#                               #Homework
                              
# def merge_lists(list1, list2): #1
    
#     set1 = set(list1)
#     set2 = set(list2)
    
#     merged_set = set1.union(set2)
    
#     merged_list = sorted(merged_set)
    
#     return merged_list

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# result = merge_lists(list1, list2)
# print(result)



# input_list = [1, 2, 3, 4, 5] #2

# squared_list = [x ** 2 for x in input_list]

# print(squared_list)


# def filter_odd_numbers(numbers): #3
#     return [num for num in numbers if num % 2 != 0]

# numbers = [1, 2, 3, 4, 5]
# odd_numbers = filter_odd_numbers(numbers)
# print(odd_numbers)  



# def find_common_elements(list1, list2): #4
#     return list(set(list1) & set(list2))

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common_elements = find_common_elements(list1, list2)
# print(common_elements)  



# def remove_duplicates_preserve_order(lst): #5
#     seen = set()
#     return [x for x in lst if not (x in seen or seen.add(x))]

# lst = [1, 2, 3, 2, 4, 1]
# result = remove_duplicates_preserve_order(lst)
# print(result)



# def merge_dictionaries(dict1, dict2): #6
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# result = merge_dictionaries(dict1, dict2)
# print(result)



# input_dict = {'a': 1, 'b': 2, 'c': 3} #7
# squared_dict = {key: value ** 2 for key, value in input_dict.items()}
# print(squared_dict)



# def extract_keys_as_list(input_dict): #8
#     return list(input_dict.keys())

# input_dict = {'a': 1, 'b': 2, 'c': 3}
# keys_list = extract_keys_as_list(input_dict)
# print(keys_list) 



# def word_frequency_counter(text): #9
#     words = text.split()
#     word_freq = {}
#     for word in words:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
#     return word_freq

# text = "hello world hello"
# freq_dict = word_frequency_counter(text)
# print(freq_dict)  



# def filter_dict_by_value(input_dict, value): #10
#     return {key: val for key, val in input_dict.items() if val == value}

# input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# filtered_dict = filter_dict_by_value(input_dict, 1)
# print(filtered_dict) 



# def factorial(n): #11
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# number = 5
# fact = factorial(number)
# print(f"The factorial of {number} is {fact}") 



# def is_palindrome(s): #12
#     s = s.lower()
#     return s == s[::-1]

# string = "radar"
# print(is_palindrome(string))



# def is_anagram(str1, str2): #13
#     str1 = str1.lower().replace(" ", "")
#     str2 = str2.lower().replace(" ", "")
#     return sorted(str1) == sorted(str2)

# word1 = "listen"
# word2 = "silent"
# print(is_anagram(word1, word2)) 



# import re #14

# def reverse_sentence(sentence):
#     words = re.findall(r"[\w']+|[.,!?;]", sentence)
#     reversed_words = words[::-1]
#     return ''.join(reversed_words)

# sentence = "Hello, world! How are you?"
# print(reverse_sentence(sentence)) 



# class TodoList: #15
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print(f"{item} is not in the list.")

#     def view_list(self):
#         return self.items

# my_list = TodoList()
# my_list.add_item("Task 1")
# my_list.add_item("Task 2")
# my_list.add_item("Task 3")
# print(my_list.view_list()) 
# my_list.remove_item("Task 2")
# print(my_list.view_list())  



# def lists_to_dictionary(keys, values): #16
#     return dict(zip(keys, values))

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# result_dict = lists_to_dictionary(keys, values)
# print(result_dict)



# def is_key_present(dictionary, key): #17
#     return key in dictionary

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(is_key_present(my_dict, 'b')) 



# def aggregate_values(dictionary): #18
#     result_dict = {}
#     for key, values in dictionary.items():
#         result_dict[key] = sum(values)
#     return result_dict

# my_dict = {'a': [1, 2, 3], 'b': [4, 5]}
# result = aggregate_values(my_dict)
# print(result) 



# def split_list_by_value(lst, value): #19
#     return [x for x in lst if x < value], [x for x in lst if x >= value]

# my_list = [3, 1, 5, 2, 4, 6]
# lower, greater_equal = split_list_by_value(my_list, 4)
# print("Elements less than 4:", lower)
# print("Elements greater than or equal to 4:", greater_equal)  



# def count_common_elements(list1, list2): #20
#     set1 = set(list1)
#     set2 = set(list2)
#     return len(set1 & set2)

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# count = count_common_elements(list1, list2)
# print(count) 


    #DAY 82 CW 
    
#   accounts = [ 
#     {
#         "fullname": "Soso Valishvili",
#         "mail": "uchavalishvili01@gmail.com",
#         "address": "Kakheti, Gurjaani, Kotekhi Str N10",
#         "password": "Goaeli124"
#     },
#     {
#         "fullname": "Nino Nadiradze",
#         "mail": "nucanadiradze1987@gmail.com",
#         "address": "Kakheti, Gurjaani, Kotekhi Str N10",
#         "password": "Nino345"
#     }
# ]

# for account in accounts:
  
#     print("Full Name:", account["fullname"])
#     print("Email:", account["mail"])
#     print("Address:", account["address"])
#     print("Password:", account["password"])

  
  
# def manual_items(input_dict): 
   
#     items_list = []
#     for key in input_dict:
#         value = input_dict[key]
#         items_list.append((key, value))
#     return items_list


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# result = manual_items(my_dict)
# print(result)


 
 
  #DAY 82 HW

def find_duplicates(d): #1
    keys = list(d.keys())
    keys.sort()
    duplicates = []
    for i in range(len(keys) - 1):
        if keys[i] == keys[i + 1]:
            duplicates.append(keys[i])
    return duplicates



def find_max_value(d): #2
    if not d:
        return None
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return key

def find_min_value(d):
    if not d:
        return None
    min_value = min(d.values())
    for key, value in d.items():
        if value == min_value:
            return key



def combine_dicts(*dicts): #3
    combined = {}
    for d in dicts:
        combined.update(d)
    return combined

def combine_dicts_tuples(*dicts):
    combined = []
    for d in dicts:
        combined.extend(d.items())
    return combined



def key_exists(d, key): #4
    return d.get(key) is not None



def remove_and_return(d, key): #5
    return d.pop(key, None)



def manual_keys(d): #6
    return list(d.keys())



def manual_values(d): #7
    return list(d.values())



def manual_items(d): #8
    return list(d.items())



def manual_get(d, key, default=None): #9
    return d.get(key, default)



def manual_pop(d, key, default=None): #10
    return d.pop(key, default)
