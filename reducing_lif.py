
# from functools import reduce

# #
# # Use reduce to complete the function below.  Do not use any loops.
# # Hint: Using a tuple, this problem can be solved in a single line of code
# #
# def add_every(n: int, lst: [int]) -> int:
#     """
#     :param n: Add every nth integer; n is assumed to be less than len(lst)
#     :param lst: A list of integers
#     :return: The sum of every nth integer in lst
#     """
#     for n in lst:
#         if n < len(lst):
#             sum += n
#     return reduce(lambda n,lst: list.append(n) if n < len(lst) else [], lst)
#     # return reduce(lambda n,y: n if n< len(lst), lst )


# print(add_every(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30)
# print(add_every(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15)

# # #
# # # Use reduce to complete the function below.  Do not use any loops.
# # # Hint: Using a tuple, this problem can be solved in a single line of code
# # #
# # def multiple_centre(n: int, lst: [int]) -> int:
# #     """
# #     :param n: How far an element is allowed to be away from the midpoint, to be included in the
# #      product calculation
# #     :param lst: The list of integers
# #     :return: The product (multiplication) of all integers that are located within n positions of the midpoint of the list
# #     """
# #     mid = len(lst)//2
# #     start = max(0,mid-n)
# #     end = min(len(lst), mid + n + 1)
# #     reduce(lambda x, y: operation, dictionary, initial_value)
# #     return reduce(lambda )

# # print(multiple_centre(1, [1, 2, 3, 4, 5]) == 24) # 3 is the middle, and 2 and 4 are each <= 1 away from the midpoint, so 2 * 3 * 4 = 24
# # print(multiple_centre(2, [1, 2, 3, 4, 5, 6]) == 720) # 4 is the middle, and 2, 3, 4, 5, 6 are each <= 2 away from the midpoint, so 2 * 3 * 4 * 5 * 6 = 720
# # print(multiple_centre(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6720)

# # def add(x,y):
# #     return x + y
# # prices = [19.99,1.00, 5.57, 12.99, 10.22]

# # total = reduce(add, prices)
# # total = reduce(lambda x,y: x + y, prices)

# # prices = [19.99,1.00, 5.57, 12.99, 10.22]


# # print(f"${total}")