# .Write a Python program that receives a string of numbers (separated by spaces),
# over a network via port 24680, adds the numbers together, then returns the result
# plus a newline to the sender. If an error occurs due to an invalid number, the string
# "Error\n" must be returned to the sender instead. For example, the command
# echo "10 20 30 40" | nc localhost 24680
# returns the string '100\n' and the command
# echo "10 20 30 40 abc" | nc localhost 24680
# returns the string 'Error\n'
# Ignore networking errors. For purposes of this question, avoid handling the case
# where recv won't return the entire transmitted string.
# Hints:
# If s is '1 2 3 4', then s.split(' ') returns the list ['1', '2', '3', '4'].
# If d contains data that was received via the network, use d.decode() to convert it to
# a regular string.
# To transmit a regular string r via the network, use r.encode().

# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# from struct import unpack
# BUF_SIZE = 1024
# HOST = ''
# PORT = 24680
# QUEUE = 1

# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(QUEUE)
#     while True:
#         sc, _ = sock.accept() # establish a connection 

#         with sc:
#             buffer = b''
           
            #print('Client' , sc.getpeername()) #client ip and port
            # # receives a string of numbers (separated by spaces),
            # data = sc.recv(BUF_SIZE)
            # s = data.decode().split(' ')
            # sum = 0
           
        
            # try:
            #     for n in s:
            #         sum += int(n)  
            #     reply = str(sum).encode()
            #     sc.sendall(reply + b'\n')
                
            # except ValueError:
            #     sc.sendall(b'Error\n')






# 12.Write a Python function that takes in a socket, and reads in bytes from the socket
# connection until a newline is encountered. All bytes read so far that are even (0, 2,
# 4, 6, 8) are then returned. Do not handle exceptions; assume all parameters are
# valid.


#1
# def receive(sc:socket) -> bytes:
# #    buffer = b''

#             print('Client' , sc.getpeername()) #client ip and port
#             # # receives a string of numbers (separated by spaces),
#             # data = sc.recv(BUF_SIZE)
#             # s = data.decode().split(' ')
#             # sum = 0
#             while True:
#                 data = sc.recv(1)
#                 if data == b'\n':
#                     break
#                 else:
#                     val = int.from_bytes(data, byteorder='big') & 0b1 = 0
#                     if val % 2 == 0:
#                         buffer = buffer + data
#             sc.sendall(buffer + b'\n')


#2
#   buffer = b''

#             print('Client' , sc.getpeername()) #client ip and port
#             # # receives a string of numbers (separated by spaces),
#             # data = sc.recv(BUF_SIZE)
#             # s = data.decode().split(' ')
#             # sum = 0
#             while True:
#                 data = sc.recv(1)
#                 if data == b'\n':
#                     break
#                 else:
#                     if int.from_bytes(data, byteorder='big') & 0b1 == 0:
#                     #if val % 2 == 0:
#                         buffer = buffer + data
#             sc.sendall(buffer + b'\n')





# 13.Write a Python function that takes in a socket and a byte string, then reads in bytes
# from the socket connection until a newline is encountered. All bytes read so far that
# ARE in the byte string are then returned. Do not handle exceptions; assume all
# parameters are valid.



# def receive(sc:socket, s:[byte]) -> [byte]:
#     buffer = b''
#     while True:
#         data = sc.recv(1)
#         if data == buffer:
#             return buffer
#         if data in s:
#             buffer = buffer + data
#         sc.sendall(buffer)

# 14.Write a Python function that takes in a socket and a delimiter string in byte format,
# and reads in bytes from the socket connection until one of the delimiters is
# encountered. The bytes read so far are then returned. Do not handle exceptions;
# assume all parameters are valid.


# def receive( sc:socket, delimiter:[byte])-> bytes:
#     buffer = b''
#     while True:
#         data = sc.recv(1)
#         if data in delimiter:
#             return buffer
#         buffer = buffer + data
#         sc.sendall(buffer)
# 15.Write a Python function that takes in a socket and a number n. The function must
# then use your function in the previous question to read in n number of lines, and
# return the longest of them. Do not handle exceptions; assume all parameters are
# valid. You can break the function into two parts.

# def get_line(current_socket: socket) -> bytes:
#     buffer = b''
#     while True:
#         data = current_socket.recv(1)
#         if data == b'\n':
#             return buffer
#         buffer += data # can overflow

# def receive(sc:socket, n:int):

#     max_length = 0
#     max_line = b''
    
#     for i in range(n):
#         current_line = get_line(sc)
#         current_length = len(current_line)
#         if current_length > max_length:
#             max_length = current_length
#             max_line = current_line
#         return max_line

    



# 16.Write a Python function that (1) takes two parameters, namely a valid socket
# connection s and a stop character c; (2) reads a packed unsigned byte n from s; (3)
# reads in bytes from s until n copies of c have been received; (4) returns all bytes
# read from s, up to and including the n copies of c. For example, if n is 4, and the
# stop character is '*' and the stream of characters is 'AB**C*DEFG*HI*JKLM', then
# your function must return 'AB**C*DEFG*'. Ignore exceptions and assume valid
# 10
# parameters.
# If your server is listening at port 24680, you can test your program using:
# echo -n -e '\x04AB**C*DEFG*HI*JKLM' | nc localhost 24680


# def receive(sc:socket, ch:char): 
#     while True:
#         data = sc.recv(1)
#         n = unpack('!B', data)[0]
#         copies = 0
#         buf = b''
#         while copies < n:
#             data = sc.recv(1)
#             if data == ch:
#                 copies +=1
#             buffer += data
        




# 17.Write a Python function that (1) takes four parameters, namely a valid socket
# connection s, a byte string t, a number n, and a stop byte c; (2) sends n as a packed
# unsigned byte via s; (3) sends t via s in chunks separated by c, or until reaching the
# end of t . For example, if t is 'AB**C*DEFG', n is 4, and c is '*', then your function
# must first send the 4 as a packed unsigned byte, then send b'AB*', then b'*', then,
# b'C*', then finally b'DEFG'. Ignore exceptions and assume valid parameters.
# def get(s:socket, t:[byte], n:int, c:byte):
#     while True:
#         s.sendall(pack('!B', n))
#         limit = len(t)
#         last = 0
#         for i in range(limit):
#             if i != c:
#                 s.send(i)
            



#do it again


# 18.Write a Python function that takes a valid socket connection, reads in the size of the
# message as a packed unsigned long long from the socket connection, then reads in
# the message from the same socket connection, and finally returns the read-in
# message in decoded form. Do not worry about exceptions or invalid parameters.
# You can break the function into 2 parts.
# def get_buf(sc:socket, expected_size:int):
#     current_size = 0
#     buf = b''
#     if current_size < expected_size:
#         data = sc.recv(expected_size - current_size)
#         buf = current_size + buf
#         current_size = current_size + len(data)

#     return buf
# def get(s:socket ):
#     data = get_buf(s,8)
#     msg_length = unpack('!Q', data)
#     msg = get_buf(sc,msg_length)

#     return msg.decode()



# 19.Write a function that (1) takes in only a port, (2) sets up a TCP server accepting
# localhost connections arriving at that port, (3) reads in a packed, unsigned short
# called size, (4) reads in size packed unsigned short integers into a list called
# numbers, (5) reads in another packed unsigned short integer n, (6) sends to the
# connected client all integers in numbers that are divisible by n, (7) closes the
# connection. All exceptions must be caught. Do not assume that recv(2) will always
# return 2 bytes at a time. You can break the function into 2 parts.

# def get_buf(sc:socket, size: int):
#     cur = 0
#     buf = b''
#     while cur < size:
#         data = sc.recv(size - cur)
#         cur = cur + len(data)
#         if data = buf:
#             return buf
#     buf = buf + data
#     return buf



# def get(port:int):

#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     with sock:
#         try:
#             sock.bind(('localhost', PORT))
#             sock.listen(1)
#             while True:
#                 sc, _ = sock.accept() # establish a connection 

#                 with sc:
#                     numbers = []
#                     data = get_buf(sc,2)
#                     size = unpack('!H', data)[0]
#                     for i in range(size):
#                         numbers.append(size)
#                     n = unpack('!H', sc.recv(2))[0]
#                     for num in numbers:
#                         if num  % n == 0:
#                             sc.sendall(pack('!H',num))
#         except Exceptions as e:
#             print(e)


# 20.Write a function that (1) takes in only a port, (2) sets up a TCP server accepting
# localhost connections arriving at that port, (3) reads in a series of signed short
# integers into a list called numbers, (4) stops reading in integers as soon as -1 is
# encountered (-1 is not saved in numbers), (5) sends the list in reverse order back to
# the client, (6) closes the connection, (7) returns the list. All exceptions must be
# caught. Do not assume that recv(2) will always return 2 bytes at a time. You can
# break the function into 2 parts.

# def get_buf(sc:socket, expected_size:int):
#     buf = b''
#     current_size = 0
#     while current_size < expected_size:
#         data = sc.recv(expected_size - current_size)
#         buf = buf + data
#         current_size = current_size + len(data)

#     return buf



# def reverse_list(port:int):
#     numbers = []

#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     with sock:
#         try:
#             sock.bind(('localhost', port))
#             sock.listen(1)
#             sc,_ = sock.accept()
#             with sc:
#                 while True:
#                     data = get_buf(sc, 2)
#                     number = unpack('!H', data)[0]
                   
#                     if number == -1:
#                         break
#                     else:
#                         numbers.append(list)
                        
#                     position = len(numbers)
#                     while position > 0:
#                         position = position -1
#                     sc.sendall(pack('!H', numbers[position]))
#         except Exception as e:
#             print(e)

#     return numbers


# 21.Write a Python function called send_list that taken a list of numbers (assume they
# are all less than 255, and that there are not more than 255 of them) and a port
# number. It then listens to that port on all network interfaces and waits for a client to
# connect. Once the client connects, the function first sends out the length of the
# array, followed by each list element, all as packed unsigned bytes. Exceptions are
# caught and the corresponding error message is printed on the screen



# def send_list(numbers:[int], port:int):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     with sock:
#         try:
#             sock.bind(('', port))
#             sock.listen(1)
#             sc,_ = sock.accept()
#             with sc:
              
#                 length_array = len(numbers)
#                 sc.sendall(pack('!B', length_array))
#                 for n in numbers:
#                     sc.sendall(pack('!B', n))

#         except exception as e:
#             print(e)
# 22.Write a Python function called receive_list that takes in a host IP (or URL) and a
# port, and then connects to the host at the given port. The function then receives the
# length of the list n and reads in n numbers via the network connection, all sent as
# packed bytes. The list is then returned to the caller. Assume the length and each
# number in the list are all less than 255. Exceptions are caught and the
# corresponding error message is printed on the screen
#
#def receive_list( host:str, port:int):
    # n = []
    # sock = socket(AF_INET, SOCK_STREAM)
    # sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    # with sock:
    #     try:
    #         sock.bind((host, port))
    #         sock.listen(1)
    #         sc,_ = sock.accept()
    #         with sc:
    #             data = sc.recv(1)
    #             if data == b'':
    #                 return n
    #             length = unpack('!B', data)[0]
    #             for i in range(n):
    #                 data = sc.recv(1)
    #                 if data == b'':
    #                     return n
    #                 n.append(unpack('!B', data)[0])
    #         sc.sendall(pack('!B', n))
    #     except Exception as e:
    #         print(e)
    # return n

# 23.Write a Python function called expedite(socket). socket is a socket connection,
# which may or may not be valid. Using socket, the function must first receive a byte
# (call it n) from the network, followed by another 4-byte number (call it payload_size),
# followed by the number of bytes indicated in payload_size. The function must then
# return (to the caller, not over the network) the nth byte in the payload. If that is not
# possible, False is returned. For example [10][20][ABCDEFGHIJKLMNOPQRST]
# returns the value 'K' because the 1-byte field contains 10 and 'K' is the 10th byte
# (counting from 0) in the 20-byte long payload; but [100][10][ABCDEFGHIJ] returns
# False because the 100 is out of range. You can assume no more than 1024 bytes
# are transmitted. Here are some tests you can run from the command line to see if
# your server works:
# echo -n '00000000144142434445464748494A4B4C4D4E4F5051525354' | xxd -r -p | nc -N 127.0.0.1 12345 # Input: 0 20 ABCDEFGHIJKLMNOPQRST
# Output: A
# echo -n 'FF000000144142434445464748494A4B4C4D4E4F5051525354' | xxd -r
# -p | nc -N 127.0.0.1 12345 # Input: 255 20 ABCDEFGHIJKLMNOPQRST
# Output: False
# echo -n '0a000000144142434445464748494A4B4C4D4E4F5051525354' | xxd -r
# -p | nc -N 127.0.0.1 12345 # Input: 10 20 ABCDEFGHIJKLMNOPQRST
# Output: K
# echo -n '00000000FF4142434445464748494A4B4C4D4E4F5051525354' | xxd -r -p | nc -N 127.0.0.1 12345 # Input: 0 255 ABCDEFGHIJKLMNOPQRST
# Output: False
# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# from struct import unpack


# def get_buf(sc:socket, expected_size:int):
#     buf = b''
#     current_size = 0
#     while current_size < expected_size:
#         data = sc.recv(expected_size - current_size)
#         if data == b'':      # client closed connection
#             break
#         buf = buf + data
#         current_size = current_size + len(data)

#     return buf
    
# def expedite(sc:socket):
#     try:
#         n = unpack('!B',get_buf(sc,1))[0]
#         payload_size = unpack('!I',get_buf(sc,4))[0]
#         payload = get_buf(sc, payload_size)
#         if payload_size != len(payload):
#             return False
#         if n >= payload_size:
#             return False
#         return payload[n]
#         print(payload[n])

#     except Exception as e:
#         print(e)
                




# BUF_SIZE = 1024
# HOST = ''
# PORT = 12345
# QUEUE = 1

# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(QUEUE)
#     while True:
#         sc, _ = sock.accept() # establish a connection 

#         with sc:
#             result = expedite(sc)
#         if not result:
#             print('False')
#         else:
#             print('data '+ chr(result))    









# 24.Write a Python function called check(socket). socket is a socket connection, which
# may or may not be valid. Using socket, the function must first receive an unsigned
# 4-byte length field (call it payload_size), followed by the number of bytes indicated in
# payload_size (call it payload), followed by another unsigned byte (call it
# actual_checksum). The function must then add all the bytes in the payload, mod
# (%) by 255, and compare the result to the actual_checksum. If the checksums
# match, True is returned. In all other cases, False is returned. For example [2]]65 66]
# [131] returns True because (65 + 66) % 255 = 131; but [20][65 + 66 + ... + 84][1]
# returns False because (65 + 66 + ... + 84) % 255 is 215, but the actual_checksum is
# 1. You can assume no more than 1024 bytes are transmitted. Here are some tests
# you can run from the command line to see if your server works:
# echo -n '00000002414283' | xxd -r -p | nc -N 127.0.0.1 12345
# Input: 2 65+66 131
# Output: True
# echo -n '000000144142434445464748494A4B4C4D4E4F5051525354AB' | xxd -r
# 12
# -p | nc -N 127.0.0.1 12345
# Input: 20 65+66+...+84 171
# Output: False
# echo -n '000000144142434445464748494A4B4C4D4E4F5051525354D7' | xxd -r
# -p | nc -N 127.0.0.1 12345
# Input: 20 65+66+...+84 150
# Output: True
# echo -n '000000FF4142434445464748494A4B4C4D4E4F5051525354D7' | xxd -r
# -p | nc -N 127.0.0.1 12345
# Input: 255 65+66+...+84 150
# Output: False



#something is wrong 


# def get_buf(sc:socket, expected_size:int):
#     buf = b''
#     cur = 0
#     data = sc.recv(expected_size - cur)
#     while cur < expected_size:
#         if data = buf:
#             return buf
#         cur += len(data)
#         buf += data
#     return buf
# # The function must then add all the bytes in the payload, mod
# # (%) by 255, and compare the result to the actual_checksum. If the checksums
# # match, True is returned. In all other cases, False is returned. For example [2]]65 66]
# # [131] returns True because (65 + 66) % 255 = 131; but [20][65 + 66 + ... + 84][1]
# # returns False because (65 + 66 + ... + 84) % 255 is 215, but the actual_checksum is
# # 1. You can assume no more than 1024 bytes are transmitted. Here a









# 25.Write a Python function called sum_bytes(socket). socket is a socket connection,
# which may or may not be valid. Using socket, the function must first receive an
# unsigned byte (call it n), followed by an unsigned 4-byte number (call it
# payload_size), followed by the number of bytes indicated in payload_size (call it
# payload). The function must then add up every nth byte in the payload and return
# the result to the calling function. For all errors, False is returned. For example [1][2]
# [65 66] returns 131 because 65 + 66 = 131; similarly, [2][20][65 66 ... 84] returns 740
# because 65 + 67 + 69 + ... + 83 = 740. However, [80][20][65 66 ... 84][1] returns
# False because 80 is larger than the number of bytes in the payload. Here are some
# tests you can run from the command line to see if your server works:
# echo -n '01000000024142' | xxd -r -p | nc -N 127.0.0.1 12345
# Input: 1 2 65 66
# Output: 131
# echo -n '02000000144142434445464748494A4B4C4D4E4F5051525354' | xxd -r -p | nc -N 127.0.0.1 12345
# Input: 2 20 65 66 ... 84
# Output: 740
# echo -n '50000000144142434445464748494A4B4C4D4E4F5051525354' | xxd -r -p | nc -N 127.0.0.1 12345
# Input: 80 20 65 66 ... 84
# Output: False
# echo -n '01000000FF4142434445464748494A4B4C4D4E4F5051525354' | xxd -r -p | nc -N 127.0.0.1 12345
# Input: 1 255 65 66 ... 84
# Output: False
# 13

# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# from struct import unpack
# def get_buf(sc:socket, expected_size:int):
#     buf = b''
#     cur = 0
#     while cur < expected_size:
#         data = sc.recv(expected_size - cur)
#         if not data:
#             break
#         cur += len(data)
#         buf += data
#     return buf


# def sum_bytes(sc:socket) :
   
#     try:
#         data = get_buf(sc,1)
#         n = unpack('!B',data)[0]
#         data2 = get_buf(sc,4)
#         payload_size = unpack('!I', data2)[0]
#         payload = get_buf(sc, payload_size)
#         if payload_size != len(payload):
#                 return False
#         if n > payload_size or n == 0:
#             return False
#         total = sum(payload[i] for i in range(0,payload_size,n))
#         return total

#     except Exception as e:
#         print(e)
#         return False




# BUF_SIZE = 1024
# HOST = ''
# PORT = 12345
# QUEUE = 1

# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(QUEUE)
#     while True:
#         sc, _ = sock.accept() # establish a connection 

#         with sc:
#             result = sum_bytes(sc)
#         if not result:
#             print('False')
#         else:
#             print(result)    


# 26.Write a Python program that:
# (1) Expects a single positive integer passed as a command line argument. If no
# argument, more than 1 argument, or a non-positive-integer argument is passed, the
# program must print out an error message and terminate. The program must not
# crash. For example, entering: ./client.py Hello results in the error message: ./
# client.py <positive integer>
# from socket import socket, AF_INET, SOCK_STREAM
# from math import ceil, floor, log2
# from sys import argv
# from struct import pack

# BUF_SIZE = 1024
# HOST = '127.0.0.1'
# PORT = 65432

# if len(argv) != 2:
#     print("Error\n")
#     exit()
# num = 0
# (2) The program must only take a command line argument. Do not use the input()
# function. Do not read from file.
# (3) Other than an error message (if applicable), the program must not print anything
# to screen.

# try:
#     num = int(argv[1])
# except ValueError:
#     print(argv[0] + '<positive integer>') 
#     exit()
# if num <= 0:
#     print(argv[0] + '<no negative integer>')
#     exit()
# if num > (2 ** 64 -1):
#     print("too big")
#     exit()
# with socket(AF_INET, SOCK_STREAM) as sock: # TCP socket
#     sock.connect((HOST, PORT)) # Initiates 3-way handshake
#     print('Client:', sock.getsockname())


# (4) The program must then determine the least number of bytes required to transmit
# the number received in step 1. For example, 255 can be represented in 1 byte
# (binary 11111111), but 256 requires 2 bytes (binary 00000001 00000000). To get the
# number of bytes required to represent the number in variable num, you can use the
# formula: math.ceil(math.floor(math.log2(num) + 1) / 8). You must import math for
# this to work.

    
#     bytes = math.ceil(math.floor(math.log2(num) + 1) / 8)
#     flag = '!'
#     if bytes == 1:
#         flag += 'B'
#         bytes = 1
#     elif bytes >= 1:
#         flag += 'H'
#         bytes = 2
#     sock.sendall(pack('!b', bytes))# (6) The program then transmits the number received in step 1 to the server, prefaced
# # by the number of required bytes.
#     sock.sendall(pack(flag,num))
# (5) The smallest supported number is 1, the largest supported number is 2 ** 64 - 1.
# (6) The program then transmits the number received in step 1 to the server, prefaced
# by the number of required bytes. So for example, when transmitting 255, the client
# actually transmits: 1 255. In binary, this is 00000001 11111111. When transmitting
# 256, the client actually transmits: 2 256. In binary this is 00000010 00000001
# 00000000.




# 27.Write a TCP server listening on port 12345 that expects an unsigned byte x,
# followed by a 1-byte operator '+' or '*', followed by another packed byte y. The
# server must then compute x + y (if the operator was a +) or x * y (if the operator was
# a y) and return the result as an unsigned short, followed by a newline. For example,
# sending 1+2 returns 3 and sending 3*4 returns 12. You can use the following to test
# your program:



# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# import struct
# BUF_SIZE = 1024
# HOST = ''
# PORT = 12345
# QUEUE = 1

# def get_buf(sc:socket, expected_size:int):
#     buf = b''
#     cur = 0
#     while cur < expected_size:
#         data = sc.recv(expected_size - cur)
#         if not data:
#             break
#         cur += len(data)
#         buf += data
#     return buf

# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(QUEUE)
#     while True:
#         sc, _ = sock.accept() # establish a connection 

#         with sc:
#             buffer = b''
#             x = struct.unpack("!B", get_buf(sc,1))[0]
#             op = get_buf(sc,1)
#             y = struct.unpack("!B", get_buf(sc,1))[0]
#             operator = op.decode()
#             if operator == '+':
#                 result =  x + y 
#             else:
#                 result = x * y 

#             sc.send((struct.pack('!H',result)) )
#             sc.sendall(b'\n')

# echo '012b02' | xxd -r -p | nc 127.0.0.1 12345 | xxd -p
# This sends over byte 01, the + character (represented by ASCII 2b), and byte 02.
# The result should be 00030a (0a here is the newline)
# echo '032a04' | xxd -r -p | nc 127.0.0.1 12345 | xxd -p
# This sends over byte 03, the * character (represented by ASCII 2a), and byte 04.
# The result should be 000c0a (the c is hexadecimal for 12, and the 0a is the newline)
# echo 'ff2aff' | xxd -r -p | nc 127.0.0.1 12345 | xxd -p
# This computes 255*255 and should result in fe010a (which is hexadecimal for
# 65025)

#!/usr/bin/python3.11
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET,SO_REUSEADDR
from struct import pack, unpack
from threading import Thread

def receive(sc, size):
    data = b''
    while len(data) < size:
        curr_data = sc.recv(size - len(data))
        if curr_data == b'':
            return data
        data += curr_data
    return data

def process_request(sc):
    print(f'Client {sc.getpeername()} ')
    with sc:
        while True:
            data = receive(sc, BYTE)
            if len(data) != BYTE:
                print('Data rejected due to size')
                return
            number = unpack('!B', data)[0]
            op = number >> OP_POSITION
            num1 = (number >> NUM1_POSITION) & NUM_BITMASK
            num2 = number & NUM_BITMASK
            result = 0
            print(f'Op: {bin(op)} Num1: {num1} Num2: {num2}')
            if op == ADD:
                result = num1 + num2
            elif op == SUB:
                result = num1 - num2
            elif op == MUL:
                result = num1 * num2
            elif op == DIV:
                result = num1 // num2
            print(f'Transmit: {result}')
            sc.sendall(pack('!H', result))

BYTE = 1
HOST = ''
PORT = 12345
OP_POSITION = 6
NUM1_POSITION = 3
NUM_BITMASK = 0b111
ADD = 0b00
SUB = 0b01
MUL = 0b10
DIV = 0b11
with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    while True:
        sc, _ = sock.accept()
        Thread(target=process_request, args=(sc, )).start()