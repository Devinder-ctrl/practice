# Write a Python program that prompts the user for a search string s and an interval i,
# then prints out every ith character in s, starting with the first character. All errors
# (e.g., invalid number, number not positive) must be caught; the program must not
# crash.


# def main():
#     while True:
#         s = input("enter a string ")
#         try:
#             i = int(input("enter a interval "))

#             if( i <= 0):
#                 print("enter a positive num~~~")
#                 continue
#         except ValueError:
#             print("Enter a valid number~~~")
#             continue
#         break

#     for index in range(0, len(s), i):
#         print(s[index] + "\n")

# main()

#!/usr/bin/python3.11.11
# search_string = input("Enter a string\n")
# interval_string = input("Enter an interval\n")
# try:
#     interval = int(interval_string)
#     if interval <= 0:
#         print("Interval must be posiFve")
#     else:
#         count = 0
#         for ch in search_string:
#             if count % interval == 0:
#                 print(ch)
#                 count += 1
# except ValueError as details:
#     print(details)

# 2. Write a Python program that prompts the user for a search string s and an interval i,
# then prints out all characters except every ith character in s. Counting starts with
# the first character. All errors (e.g., invalid number, number not positive) must be
# caught; the program must not crash.

# def main():
#     search_string = input("Enter a string\n")
#     interval_string = input("Enter an interval\n")
#     try:
#         interval = int(interval_string)
#         if interval <= 0:
#             print("Interval must be posiFve")
#         else:
#             count = 0
#             for ch in search_string:
#                 if count % interval != 0:
#                     print(ch)
#                 count += 1
#     except ValueError as details:
#         print(str(details))
# main()
# 3. Write a Python function that takes in a file name and a character, and then returns
# how many times the character appears in the given file. If there is an error opening
# or reading the file, -1 is returned. Don't forget to add comments.
# def read_file( file_name: str, character:str) -> int:
#     count = 0
#     try:
#         with open(file_name) as f:
#             for line in f:
#                 for ch in line:
#                     if ch == character:
#                         count += 1
                
#     except OSError:
#         return -1

#     return count



# 4. Write a Python function that takes in a list of strings and an integer n, and returns
# the list of strings, except that any string longer than n is truncated to size n. If n is
# not positive, the function returns an empty list. Don't forget to add comments. Do
# not use maps or list comprehensions.

# def limit_length(list: [str], n: int) -> [str]:
#     new_list = []
#     if n < 1:
#             return new_list
#     for i in list:
#         if n < len(i) :
#             new_list.append(i[:n])
#         else:
#             new_list.append(i)
#     return new_list
# print(limit_length(["some","somethinjjjjjjg","sndydso"], 3))
# 5. Repeat the previous question using a map.
# def limit(lst: [str], n:int) -> [str]:
   
#     if n < 1:
#         return []
#     return list(map(lambda item : item[:n],lst))
# print(limit(["some","somethinjjjjjjg","sndydso"], 7))
# 6. Repeat the previous question using a list comprehension.
# def limit(lst: [str], n:int) -> [str]:
#     return [line[:n] for line in lst if 1 <= n]
   
# print(limit(["some","somethinjjjjjjg","sndydso"], 7))


# 7. Write a function that looks at every element of a list of strings called user_input and
# then computes and prints out the sum of all nonnegative integers. For example, if
# user_input is [123, 456.7, 0, -1, "Testing", 887, "123"], the sum should be 1010.
# Don't forget to add comments.

# def user_input(lst: [any]) -> int:
#     sum = 0
#     for string in lst:
#         if type(string) == int and string > 0:
#             sum += int(string)
#     return sum
# def user_input(lst: [any]) -> int:

#     return sum([i for i in lst if type(i) == int and i > 0])
# print(user_input([123, 456.7, 0, -1, "Testing", 887, "123"]))

# 8. Write a function that, given an Integer called total and a 2D list called square,
# checks whether or not each row of the array sums up to total. The function returns
# an empty dictionary if and only if each row sums up to total. For example, assuming
# total is 15 and the 2D list is
# 8 1 6
# 3 5 7
# 4 9 2,
# each row adds up to 15, so an empty dictionary is returned. In case of one or more
# rows do not add up to total, the function returns a dictionary of errors that were
# encountered. For example, assuming a total of 15 and a 2D list of
# 8 0 6
# 3 5 7
# 5 9 2,
# the function returns {"Row 0": 14, "Row 2": 16 }. Assume the 2D list is indeed
# square. Don't forget to add comments.
# 3

# def board(total: int, square: [[int]]) :
#     result = {}
#     for i in range(len(square)):
#         row_sum = sum(square[i])
        
#         if row_sum != total:
#             result[f'Row {i} '] = row_sum
#     return result
           
# print(board(15,[[8,0,6],[3,0,7],[4,7,2]]))

# 9. Write a function that takes in a list of integers and returns True if the list contains all integers
# in the range of [1...size of the list), False otherwise. So [4, 3, 2, 6, 5, 1] returns True because
# 1, 2, 3, 4, 5, 6 are all present exactly once, but [4, 3, 2, 7, 5, 1] returns False because 6 is
# missing, and [4, 3, 2, 5, 1, 1] returns false because 1 is present twice.






# def take(lst:[int]) -> bool:
#     if len(lst) == 0:
#         return True
#     nums = {}
#     for i in lst:
#         nums[i] = nums.get(i,0) + 1
#         for i in range(1, )
#         if i in range(1,len(lst)):
#             return True
#         else:
#             return False

# def unique_range(lst: [int]) -> bool:
# """
# Checks to make sure only [1...len(lst)) are in 'lst'.
# :param lst: The list to check
# :return: True if list only contains 1...len(lst), False otherwise
# 8
# """
#     lst_len = len(lst)
#     if lst_len == 0:
#         return True
#     nums = {}
#     for x in lst:
#         nums[x] = nums.get(x, 0) + 1 # alternaFve: Could return False if nums[x] becomes > 1
#         for i in range(1, lst_len + 1):
#             if nums.get(i, 0) != 1:
#                 return False
#             return True





# 10. Using reduce, write a function that takes a list of integers and returns the number of even
# integers in it
# from functools import reduce
# def red(lst:[int]) -> int:

#     return reduce(lambda acc, x: acc+x if x % 2 == 0 else acc, lst, 0)



# Write a program that prompts the user for a string and a 
#positive number n, then prints every nth word of the string. 
#Include error handling for invalid input.


# def get():
#     s = input("Enter a string\n")
#     n = input("Enter a interval\n")

#     try :
#         interval = int(n)
#         if interval < 1:
#             print("Plaease enter a positive integer")
#              return 
#     except ValueError as details:
#         print(str(details))
#          return
#     for i in range(0,len(s),interval):
#             print(s[i])
    
# get()
# 2. Similar to "all except every ith character"
# Write a program that asks for a string and a positive number k, 
#then prints the string without every kth word. Handle invalid numbers gracefully.

# def get():
#     s = input("Enter a string\n")
#     n = input("Enter a interval\n")

#     try :
#         interval = int(n)
#         if interval < 1:
#             print("Plaease enter a positive integer")
#             return
#     except ValueError as details:
#         print(str(details))
#     result = ""
#     for i in range(len(s)):
#         if (i +1) % interval != 0:
#             result += s[i]
#             print(s[i])
# 3. Similar to "count character in file"
# Write a function that takes a filename and a word, and 
#returns how many times the word appears in the file. 
#Return -1 if the file cannot be read.

# def filename(file_name:str, ch:str) -> int:
#     count = 0

#     try:
#         with open(file_name) as f:
#             for line in f:
#                 for c in line:
#                     if c == ch:
#                         count += 1
#         return count
        
#     except OSError:
#         return -1





# 4. Similar to "truncate strings without map/lc"
# Write a function that takes a list of strings and an integer m, 
#and returns a new list where each string shorter than m is padded with 
#"*" to length m. Return an empty list if m is not positive.

# def some(lst:list[str], m:int) -> list[str]:
#     new_lst = []
#     if m < 1:
#         return new_lst
    
#     for string in lst:
#         if len(string) > m:
#             new_lst.append(string[:m])
#         else:
#             new_lst.append(string.ljust(m, "*"))
#     return new_lst



# 5. Similar to "truncate strings using map"
# Repeat the previous question, but implement it using map instead of a for loop.

# def some(lst:[str], m:int) -> [str]:
#     return list(map(lambda s: s[:m] if len(s) > m else s.ljust(m,"*"),lst ))
# 6. Similar to "truncate strings using list comprehension"
# Repeat the padding problem (question 4) using a list comprehension.
# def some(lst:[str], m:int) -> [str]:
#      return [s[:m] if len(s) > m else s.ljust(m,"*")for s in lst ]

# 7. Similar to "sum of all nonnegative integers"
# Write a function that takes a list of mixed types (int, float, string) and
# prints the product of all positive integers. Ignore non-integers and non-positive numbers.

# def sum(lst:list[any]) -> int:
#     sum = 1
#     found = False
#    for s in list:
#         if int(s) > 0 and isinstance(s,int):
#             sum *= s
#             found = True
#     return sum if found else 0


# 8. Similar to "check row sums in square 2D list"

# Write a function that takes a 2D square list and a total, and returns a dictionary of columns that do not sum to the total, with their sums as values. Return an empty dictionary if all columns match.




# 9. Similar to "check if list contains all integers in range"

# Write a function that checks if a list of integers contains all even numbers from 2 up to the largest even number in the list exactly once. Return True or False.

# 10. Similar to "count even integers using reduce"

# Using reduce, write a function that counts how many odd numbers greater than 10 are in a list of integers.