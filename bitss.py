
# Given a 3-bit number stored in x, a 2-bit number stored in y, and an 11-bit number stored in z,
#  how can we combine that into a single integer using Python. 
#  Your answer MUST preserve the order x-y-z and be a one-liner; multiple lines are not allowed.
#x = 3, y = 2 , z = 11 #we need 2 bits for y and 11 for z so x must be highest 3 bits of final number
# if x = 0b101 number = 1,10,11,100,101,110,111,1000 , so ob101 is 5

# 0b101 << 13 = 0b1010000000000000

# we shift y to 11 bits to left so it sits right below x and 11 lowest for z
#y = 0b11, so 0b11 is 3
#0b11 << 11 = 0b1100000000000
#no shift to 11

# using bitwise or because it keeps the position of bits as they are
#i = (x << (2+11)) | (y << 11) | z


# 1. Packing multiple numbers into one integer
# You have:
# a (4-bit)
# b (3-bit)
# c (5-bit)

# Task: Combine them into a single integer so the order is a-b-c. Write a one-liner.

i = (a << (3 + 5)) | (b << 5) | c
# 2. Extracting numbers from a packed integer
# Given an integer combined that stores x-y-z in a 3-2-11 bit format:

# Write Python code to extract x, y, and z back from combined.
x = (combined >> 13) & 0b111      # 3 bits
y = (combined >> 11) & 0b11       # 2 bits
z = combined & 0b11111111111      # 11 bits

# 3. Swapping bits
# Write a function swap_bits(n, i, j) that swaps the i-th and j-th bits of n and returns the new integer.

def swap_bits(n:int, i:bit, j:bit) -> int:
    if ((n>>i) & 1) != ((n >> j) & 1):
        n ^= (1 << i) | (1 << j)
    return n
    
# 4. Counting set bits
# Write a Python function that counts the number of 1s in the binary representation of a number n without using bin() or str().
def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >> =1
    return count
# 5. Checking if a number is a power of 2 using bits
# Write a one-liner to check if a number n is a power of 2 using bit manipulation.
is_power_of_2 = n > 0 and (n & (n - 1)) == 0
# 6. Bit masking
# Given a 16-bit integer, extract the middle 8 bits using a bit mask and shift.

middle8 = (n >> 4) & 0xFF

# 7. Left rotate bits
# Write a function that performs a circular left rotation of n by k bits (for a fixed 8-bit number).
def left_rotate(n, k):
    return ((n << k) | (n >> (8 - k))) & 0xFF

# 8. Toggle specific bits
# Given n and a list of positions [1,3,5], toggle the bits at those positions and return the new number.
def toggle_bits(n, positions):
    for p in positions:
        n ^= (1 << p)
    return n

# 9. Set the N-th bit to 1
# Write a one-liner to set the 5th bit of an integer n to 1 without changing other bits.
n |= (1 << 5)  # sets 5th bit

# 10. Bitwise packing with negative numbers
# Given a signed 4-bit number x and unsigned 4-bit number y, combine them into a single byte while preserving the sign of x.
combined = ((x & 0b1111) << 4) | (y & 0b1111)




#bit operators

# 1. and (&)

#     return 1 if both bits are 1 ,else 0 
#     a = 10, b = 5
#     a in binary os 1010
#     b in binary is 0101
#       1010
#     & 0101
#     --------
#       0000  = 0 (in decimal)

#       bin(a & b) = '0b0' in binary
#       a & b = 0 in decimal


# 2. or(|)

# return 1 if any of bits is 1; else it retursn 0
#     a in binary os 1010
#     b in binary is 0101
#       1010
#     & 0101
#     --------
#       1111  = 15 (in decimal)

#       bin(a|b) = '0b1111'

# 3. not(~)

    # returns one compliment of a number

    # a = 10 in bin 1010 
    # ~a = ~1010
    #    = 0101 (5)
    # ~a = 5

    # wrong = put signed bit 0 in front of 01010
    # a = 10 in bin 01010 
    # ~a = ~01010
    #    = 10101 (11)
    # ~a = -11

# 4. xor(^)

# returns 1 if one of bits is 1; else 0
#     a = 10 , b = 9
#       1010
#     ^ 1001
#     --------
#       0011 = 3 in decimal


# bitwise shift operator

# 1. right shift = >> mans divide num by 2^ n
# 2. left shift = <<

# a = 12 = 01100 = 12  divide by 2
# a >> 1 = 00110 = 6   divide by 2
# a >> 2 = 00011 = 3

# a = -12 
# ~a = 10011
# add 1
# 10011 + 1 =  10100 = -12
# so now -12 = 10100
# a >> 1 = 11010 = -6
# a >> 2 = 11101 = -3


# 2. left shift , multiply by 2

# a = 3 = 011
# a << 1 = 0110 = 6
# a << 2 = 01100 = 12

# a = -3 = 101 
# a << 1 = 1010 = -6
# a << 2 = 10100 = -12


# lambda functions , 1 line functions
# def doubel(x): return x*2 =  lambda x: 2*x
# def add(x,y) : return x + y = lambda x,y: x + y
# def max(x,y): if x> y: , (mx = lambda x,y: x if x > y else y)
#     return x
#     else:
#         return y

# lst1 = [4,3,2,1]            using lambda
# def square(lst1):           print(list(map(lambda x:x**2, lst1)))
#     lst2 = []
#     for num in lst1:
#         lst2.append(num ** 2)
#     return lst2


# list comprehension:
# print([x**2 for x in lst1])



# filter...
# lst1 = [4,3,2,1]                        using lambda:
# def over_two(lst1):                     print(list(filter(lambda x: x > 2,lst1)))
#     lst2 = [x for x in lst1 if x > 2]
#     return lst2

# list comprehension:
# ([x for x in lst1 if x > 2])
# ------- prints [4,3]


# -----reduce-----

# lst1 = [4,3,2,1]                    first it goes over 4 and 3 which is 12 than 12 and 2 which is 24 then 24 and 1 which is 24
# def multi(lst1):                    print(reduce(lambda x,y: x*y, lst1))
#     prod = lst1[0]
#     for i in range(1,len(lst1)):
#         prod = prod*lst1[i]
#     return prod

# prints (24)

# dictionary---------comprehension

# dict1 = {x: 2*x for x in [0,2,4,6]}  here x is the key and value will be 2 * x

# example2 = {x: 2*x for x in range[0,7,2]}

# x  = "python"
# dict3 = {i: 3*i.upper() for i in x}
# print(dict5)
# we get {'p': 'PPP', 'y':'YYY' ...}



# ----slice------

# sequence[start:stop:step]
# lst = [1,2,3,4]
# print(lst[2:])  means 3,4 go till end

# s = "abndef"
# print(s[3:]) #"def"

# lst = [0,1,2,3,4,5,6]
# s[:i] means from start up to index i -1
# lst[:4] [0,1,2,3]
# [i:j] means from i to j -1
# lst[2:5] [2,3,4]
# lst[3:] [3,4,5,6]
# [::2] every second element from start to end
# lst[::2] [0,2,4,6]
# lst[:] whole list
# [i:j:k] from i to j-1 stepping by k

# lst[::-1] reverse list [6,5,4,3,2,1,0]

# lst[5:1:-1] [5,4,3,2] start at 5 go -1 till 1


# print(lst[1::3])  # [1, 4]
# # Start at index 1, take every 3rd element

# print(lst[:6:2])  # [0, 2, 4]
# # Start at beginning, go up to index 6 (exclusive), step 2

# s = "abcdefg"
# print(s[2:5])   # "cde"
# print(s[:4])    # "abcd"
# print(s[3:])    # "defg"
# print(s[::-1])  # "gfedcba"
