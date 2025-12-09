# 28.Write a multithreaded Python server that guesses a random number between 1 and
# 100 (you can use random.randint(1, 100) from the random library); listens on port
# 12345; accepts an arbitrary number of clients; let's them know their ID; repeatedly
# reads in the guesses from the clients, who send the number as a newline-
# terminated string; lets the clients know whether or not they correctly guessed the
# number, and if so, if they were the first. The server should not crash. You can use
# nc localhost 12345 to mimic a client connecting to a server on local port 12345.

# from threading import Thread, Semaphore
# from random import randint
# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# import struct

# HOST = ''
# NUM_CLIENTS = 1
# PORT = 12345
# MIN = 1
# MAX = 100
# r = randint(MIN,MAX)

# lock = Semaphore()
# winner = 0

# def get_line(current_sock:socket)->bytes:
#     buffer = b''
#     while True:
#         data = current_sock.recv(1)
#         if data == b'' or data == b'\n':
#             return buffer
#         buffer += data

# def contact_player(client:socket, player_id:int):
#     global r,lock,winner

#     with client:
#         client.sendall(f'Hellp Player {player_id} \n'.encode())
#         while True:
#             try:
#                 found = False
#                 found_first = False
#                 number = int(get_line(client))
#                 print(r)
#                 with lock:
#                     if number == r:
#                         if winner == 0:
#                             found = True
#                             found_first = True
#                             winner = 1
                


#                 if found_first == True:
#                     client.sendall(b'winner\n')
#                 elif found == True:
#                     client.sendall(b'you got it\n')
#                 else:
#                     client.sendall(b'loser\n')

#             except Exception as e:
#                 continue



# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(NUM_CLIENTS)
#     num_players = 1
#     while True:
#         sc, _ = sock.accept() # establish a connection 
#         Thread(target=contact_player,args=(sc,num_players)).start()









# 29.Write a multithreaded messaging server that accepts 2 connections. The first client
# to connect to the server is prompted for a message. The server then sends that
# message to the second client. The second client is then prompted for a message,
# which is sent back to the server, which in turn sends that message to the first client.
# This repeats ad infinitum. Your answer must be multithreaded, using one thread per
# client. The server should not crash.




# from threading import Thread, Semaphore
# from random import randint
# from socket import socket, AF_INET, SOL_SOCKET, SOCK_STREAM, SO_REUSEADDR
# import struct

# HOST = ''
# NUM_CLIENTS = 2
# PORT = 12345

# input_queue = Queue()
# out_queue = Queue()
# lock = Semaphore()

# def get_line(current_sock:socket)->bytes:
#     buffer = b''
#     while True:
#         data = current_sock.recv(1)
#         if data == b'' or data == b'\n':
#             return buffer
#         buffer += data

# def client_one(client:socket, client_id:int):
#     while True:
#         if client_id == 1:
#             client.send(f'hello {client_id} please enter a msg'.encode())
#             client.send(b'\n')
#             msg = client.recv(1).decode()
#             output_queue.put(msg)
#             msg2 = output_queue.get()
#             client.send(msg2)

# def client_Two(client:socket, client_id:int):
#     while True:
#         if client_id == 0:
#             msg = output_queue.get()
#             client.send(msg)
#             client.send(f'hello {client_id} please enter a msg'.encode())
#             msg2 = client.recv(1).decode()
#             output_queue.put(msg2)


# with socket(AF_INET, SOCK_STREAM) as sock:
#     sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
#     sock.bind((HOST, PORT))
#     sock.listen(NUM_CLIENTS)
#     num_players = 1
#     while True:
#         sc, _ = sock.accept() # establish a connection 
#         Thread(target=client_one,args=(sc,num_players)).start()
#         Thread(target=client_Two,args=(sc,num_players)).start()

#         num_players +=1




# 30.Write a multithreaded server that monitors sensors. Specifically, using a b'?', the
# server prompts the first sensor client whether or not an alert condition is present.
# The 1-byte reply is sent to the server. If an alert is present (b'!'), the alert counter is
# incremented and the counter value is printed on the server. The server, using a b'?',
# then prompts the second sensor client whether or not an alert condition is present.
# The reply is sent to the server. If an alert is present (b'!'), the alert counter is
# incremented and a message is printed on the server. This repeats indefinitely. Your
# answer must be multithreaded, using one thread per client.






# 31.Write a Python server that creates a new thread for every client that connects. Each
# thread waits for a newline-terminated message from its client, then prints the
# message to the server screen, then waits for the next message from its client. Be
# sure to use locks so that a print command is not interrupted by another thread's
# print command. The server must not crash.






# 32.Write a Python server that creates a new thread for every client that connects. Each
# thread waits for a newline-terminated string from its client. It then converts the
# string to an integer (or 0, if that is not possible), and adds it to a global sum. It then
# returns the latest global sum to the client. Be sure to use locks so that a race
# condition is avoided. Numbers of more than 4 digits are ignored.
# For a simple test, echo "123" | nc 127.0.0.1 12345 returns 123 and then echo
# "877" | nc 127.0.0.1 12345 returns 1000 and then echo "1 error" | nc 127.0.0.1
# 12345 returns nothing. Sending echo "12345678" | nc 127.0.0.1 12345 also returns
# nothing, but then sending echo "111" | nc 127.0.0.1 12345 returns 1111