# 34.Using asyncio, write a Python server that sets a global num to a random value,
# accepts connections from local and external clients on port 12345, repeatedly reads
# in one line at a time from one or more clients, converts that line to an int, checks
# whether or not that int is lower, higher, or equal to num, depending on the
# comparison, sends the client the message "Too High", "Too Low", or "Correct",
# respectively. If correct, the client connection is closed. All exceptions must be
# caught.
echo "# practice" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Devinder-ctrl/practice.git
git push -u origin main

# from asyncio import run,start_server, StreamReader, StreamWriter 
# from random import randint
# random = randint(1,100)

# async def read_input(reader:StreamReader, writer:StreamWriter) -> None:
#     global random 
#     print(random)
#     try:
#         while True:
#             data = await reader.readline()
#             if data == b'':
#                 break
#             num = int(data.decode())
            
            
#             if num > random:
#                 writer.write(b"Too High\n")
#                 await writer.drain()
#             elif num < random:
#                 writer.write(b"Too Low\n")
#                 await writer.drain()
#             else:
#                 writer.write(b"Correct\n")
#                 await writer.drain()

#                 break
#     except Exception as e:
#         print(e)
#     writer.close()
#     await writer.wait_closed()


# async def main() -> None:
#     server = await start_server(read_input, '', 22222)
#     await server.serve_forever()


# run(main())

# 35.Using asyncio, write a Python client that connects to the server in the previous
# question; sends the server a UTF-8 encoded number that is midpoint between
# HIGH and LOW (both constants are based on the range you used in the previous
# question); and waits for a server to reply with a line of encoded text. If the server
# says "Too High", the client sets the new high point to the current mid point, if the
# server says "Too Low", the client sets the new low point to the current mid point,
# and if the server says "Correct", closes the connection. If the reply was not correct,
# the client calculates a new mid point and sends that to the server, until the correct
# number is guessed. All exceptions must be caught.
# For example, assuming the server's number is 12, and HIGH = 100 and LOW = 0,
# the client would first send 50. Getting back the reply "Too high", it will then send
# 25. Getting back the reply "Too high", it will then send 12, upon which "Correct" is
# returned and the client quits.
 

# from asyncio import open_connection, run
# from sys import argv

# async def client() -> None:
#     MAX = 100
#     MIN = 0
#     try:
#         reader,writer = await open_connection('127.0.0.1', 22222)

#         while True:

            
#             midpoint = (MIN+MAX)//2
            
#             writer.write(str(midpoint).encode() + b'\n')
#             data  = await reader.readline()
#             decode = data.decode().strip()
#             print(decode)
#             if decode == 'Too High':
#                 print(midpoint)

#                 MAX = midpoint
                
#             elif decode == 'Too Low':
#                 print(midpoint)

#                 MIN = midpoint
                
#             else:
#                 break
            
#     except Exception as e:
#         print(e)
#     if writer is None:
#         writer.close()
#         await writer.wait_closed()

# run(client())



# 36.Using asyncio, write a server that listens on port 11111 and accepts a string of text,
# followed by a newline, then returns 'OK' to the client if the string contains only
# lower-case vowels, 'NO' otherwise. For example:
# echo "abcde" | nc localhost 11111
# NO
# echo "aeiou" | nc localhost 11111
# OK
# echo "Aeiou" | nc localhost 11111
# NO
# Use only asyncio; do not use any other libraries.




# from asyncio import run,start_server, StreamReader, StreamWriter 
# vowels = {'a':True, 'e':True, 'i':True, 'o':True,'u':True}
# HOST = ''
# PORT = 11111
# OK = b'OK\n'
# NO = b'NO\n'
# async def read_input(reader:StreamReader, writer:StreamWriter) -> None:
#     try:
        
#         data = await reader.readline()
       
#         text = data.decode().strip()
#         msg = OK
#         for letter in text:
#             if letter not in vowels:
#                 msg = NO
                
#         writer.write(msg)
#         await writer.drain()
            

#     except Exception as e:
#         print(e)
#     writer.close()
#     await writer.wait_closed()


# async def main() -> None:
#     server = await start_server(read_input, HOST, PORT)
#     await server.serve_forever()

# run(main())

# 37.Using asyncio, write a server that listens on port 22222 and accepts a string of text,
# followed by a newline, then returns the number of digits found in that string to the
# client. For example:
# echo "abcde" | nc localhost 22222
# 0
# echo "ics226" | nc localhost 22222
# 3
# Do not pack any numbers; use only strings. Use only asyncio; do not use any other
# libraries.
# 36



# 38.Using asyncio, write a server that listens on port 33333 and accepts a string of text,
# followed by a newline, then returns the number of punctuation symbols (specifically:
# .,:;? ) that were found, to the client. For example:
# echo "a. bc, defgh" | nc localhost 33333
# 2
# echo "...???" | nc localhost 33333
# 6
# echo "Aeiou" | nc localhost 33333
# 0
# Use only asyncio; do not use any other libraries.



# 39.Using asyncio, write a server in python3 that repeatedly waits for a newline-
# terminated string from its client. It then converts the string to an integer, and adds it
# to a global variable sum. Should the string be a newline-terminated asterisk, the
# current value of sum is sent to the client, and the connection is closed. You can test
# the server using the command nc 127.0.0.1 12345



# 40.For this server, you must use Python's asyncio. The server starts out by picking a
# random number in the range from 0 to 9, inclusive. The server then waits for
# connections on localhost port 12345. The server enforces turns among its clients; it
# lets a client know its turn by transmitting the string "GO!\n". The server then expects
# a newline-terminated guess from that client. If the guess matches the random
# number, the client is informed of the win using the string "WIN\n" and the
# connection is closed. All other clients are informed of their loss using the string "NO.
# \n"and the connection is closed. Your server must not crash. You can test the server
# using the command nc 127.0.0.1 12345




# 41.Create a server that complies with all of the following specifications: Use asyncio.
# On startup, the server creates an empty 4x4 game board. It then randomly selects
# one of these 16 cells and marks it with a '1'. Be sure to print out the board on the
# screen! The server then waits for a client connection on localhost port 12345. The
# server prompts the client to make a guess by transmitting the string "GO\n". The
# server then expects a position from the client in the format "_ _\n", where the first
# blank represents the row and the second blank represents the column. Values must
# be in the range of 0 - 3, so the server validates the client input. Any invalid input
# means that the input is ignored. If the position matches that of the '1' on the board,
# the client is sent the message "OK\n". Otherwise, including in the case of invalid
# input, the client is sent the message "NO\n". On OK, the connection is then closed.
# On "NO\n", the cycle repeats from Step 4 by prompting the client for another guess.
# The server must not crash. You can test the server using the command nc
# 127.0.0.1 12345



# 42.Modify your answer to the previous question so that the following conditions hold:
# Instead of 1 client, the server supports 2 clients. Specifically: At startup, a '2' is also
# placed randomly in a blank cell. Both clients can make a guess anytime they wish;
# turns are not enforced. A client must guess the other client's cell to get an OK back.
# So, client 1 will get only an OK if it guesses the location of the '2' and client 2 will
# only get an OK if is guesses the location of the '1'. (Client 1 is the first client to
# connect, client 2 is the second client to connect. Any other clients are
# disconnected.)




#exam question
# /2) Using Python's asyncio, write a server that listens on localhost port 12345, 
# and upon successful connection by a client, repeatedly waits for a newline-terminated string 
# from that client, then prints out that string.  The connection is closed thereafter, but the 
# server keeps running, waiting for other clients to connect.  You can test this step by running 
# your server in one terminal, opening another terminal, and there entering the command echo 'Test' | nc localhost 12345
# and making sure that Test is printed out by your server.  Try this repeatedly. 
#  The server should keep running without any error messages.  Do not proceed to the next step until this step is working.



# Modify the server by using the string received from the client (without the newline) 
# as a filename, attempting to open a file by that name, and printing out all integers 
# in that file that are in range [0, 15] and ignoring integers that are out of range. 
#  If the file does not exist, or contains non-integers, an error message is printed,
#   and the connection is closed. You can test this step by creating a file called nums1 with the following contents:


# 6) Write another function that takes in a writer and 
# a collection of 8 numbers at a time read from the file 
# (adding 0s if there are fewer than 8 numbers), then sends 
# those numbers to the client, one unsigned byte at a time. 
#  Just before sending a number, print out the number you are about to send. 
#   Print out DONE when you are about to leave the function. You can test this 
#   step by creating a file called nums2 with the following contents:


# 10
# 8
# 7
# 15
# 6
# 1
# 2
# 4
# 0
# 9
# 14
# 12

# from asyncio import run,start_server, StreamReader, StreamWriter 

# from struct import pack
# PORT = 12345

# async def read_input(reader:StreamReader, writer:StreamWriter) -> None:
    
#     try:
#         data = await reader.readline()
#         file = data.decode().strip()
#         print(file)
#         try:
#             with open(file) as f:
#                 for line in f:
                    
#                     num = line.strip()
#                     if 0<= int(num) <= 15 :
#                         print(num)
#         except OSError as details:
#             print('Error', details)
#     except Exception as e:
#         print(e)
#     writer.close()
#     await writer.wait_closed()

# async def send_num(reader:StreamReader, writer:StreamWriter) :
   
#     try:
#         data = await reader.readline()
#         file = data.decode().strip()
#         print(file)
#         try:
#             with open(file) as f:
#                 numbers = list(map(int, f.read().split()))
#             for i in range(0,len(numbers),8):
#                 chunk = numbers[i:i+8]
                
                
#                 while len(chunk) < 8:
#                     chunk.append(0) 
                    
                 
#                 for n in chunk:
#                     print(n)
                
#                 # for i in range(0,8,2):
#                 #     first = chunk[i]

#                 #     second = chunk[i+1]
#                 #     send = ((first <<  4 )| second)
#                 #     writer.write(pack('!B',send))
                  
#                 for bit in range(3,-1,-1):
#                     byte = 0
#                     for n in chunk:
#                         bit_value = (n >> bit) & 1
#                         byte = (byte << 1) | bit_value
                        
#                     writer.write(pack('!B',byte))
#                 await writer.drain()
#                 print('Done')
                    
#         except OSError as details:
#             print('Error', details)
#     except Exception as e:
#         print(e)
#     writer.close()
#     await writer.wait_closed()
    

# async def main() -> None:
#     server = await start_server(send_num, '', PORT)
#     await server.serve_forever()


# run(main())
