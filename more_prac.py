# Write a function that takes in a number and 
#prints out the first two bits of that number

num = 10 bin = 1010
first two bits = 10

# def func(num:int) -> bits:
#     bits = (num) >> 2 & 0b11
#     print(bits)
#     return bits


def first(num:int):
    n = num
    total_bits = 0
    while n > 0:
        n = n >> 1 # 1010 >> 1 = 0101 >> 1 = 0010 >> 1 = 0001
        total_bits += 1 # bits = 4
    top_two = num >> (total_bits -2) # 1010 >> (4-2) , 1010 >> 2 == 0010
    top_two = top_two & 0b11
# Write a function that takes in a number and 
#prints out the number of non-zero bits in that number
def func(num:int) -> bits:

    # count = bin(num).count('1')
    # print(count)
    # return count


    #my
   def count_nonzero_bits(num: int) -> int:
    count = 0
    while num > 0:
        if num & 1:       # check if the LSB is 1
            count += 1    # increment counter
        num = num >> 1    # shift number right by 1
    print(count)
    return count

# Write a function that takes in a number 
#and prints out how often the pattern "10" appears in that number

def func(num:int) -> int:
    bits = bin(num)[2:] #remove '0b'
    count = 0
    for i in range(len(bits) -1):
        if bits[i:i+2] == '10':
            count += 1
    print(count)
    return count



def count_10_pattern(num: int) -> int:
    count = 0
    prev_bit = None  # No previous bit initially

    while num > 0:
        curr_bit = num & 1        # Get LSB
        if prev_bit == 1 and curr_bit == 0:  # pattern "10"
            count += 1
        prev_bit = curr_bit       # Update previous bit
        num = num >> 1            # Shift number right

    print(count)
    return count

# Write a function that takes in a list of numbers and prints out the number with the most 1s

def func(lst:[int]) -> int:
    max_num = max(lst, key=lambda x:bin(x).count('1'))
    return max_num

# Write a function that takes in an integer n and returns a number with bits 1, 2, 3, 5, 8, 13, 21, ..., n set

def fib_bits(n: int) -> int:
    a, b = 1, 2
    result = 0
    while a <= n:
        result |= 1 << (a - 1)  # set bit at position a (0-indexed)
        a, b = b, a + b
    print(result)
    return result

def max_ones(lst: list[int]) -> int:
    max_count = -1
    max_num = None

    for num in lst:
        ones = count_nonzero_bits(num)  # use helper function
        if ones > max_count:
            max_count = ones
            max_num = num

    return max_num
# =====

# (1)    write a server (threaded-sockets) that doubles vowels (a -> aa, e -> ee, etc.)
#     write a client that reads a sentence from command line and transmits it to the server and verifies the result
#     use echo as test scaffolding
import socket
import threading

HOST = '127.0.0.1'  # localhost
PORT = 12345

VOWELS = 'aeiouAEIOU'

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode()
            result = ''.join([c*2 if c in VOWELS else c for c in text])
            conn.sendall(result.encode())
     except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed: {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
# (2)    ...and returns the result to the next connection (hint: use queues); first time, response is OK
import socket
import threading
from queue import Queue

HOST = '127.0.0.1'
PORT = 12345

VOWELS = 'aeiouAEIOU'

# Queue to hold previous results
result_queue = Queue()

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    try:
        data = conn.recv(1024)
        if not data:
            conn.close()
            return

        text = data.decode()

        # Double vowels
        processed = ''.join([c*2 if c in VOWELS else c for c in text])

        # Determine what to send back
        if result_queue.empty():
            # First client, nothing in queue
            response = "OK"
        else:
            # Pop previous result for this client
            response = result_queue.get()

        # Put current processed text into the queue
        result_queue.put(processed)

        # Send response to client
        conn.sendall(response.encode())

    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        conn.close()
        print(f"Connection closed: {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()

# (3)    repeat using asyncio

import asyncio

HOST = '127.0.0.1'
PORT = 12345
VOWELS = 'aeiouAEIOU'

# Asyncio queue
result_queue = asyncio.Queue()

# Function to double vowels
def double_vowels(text: str) -> str:
    #return ''.join([c*2 if c in VOWELS else c for c in text])
    result = ""                 # start with empty string
    for c in text:              # loop over each character
        if c in VOWELS:         # if it's a vowel
            result += c * 2     # double it
        else:
            result += c         # otherwise, keep it as is
    return result
# Async function to handle each client
async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"Connected by {addr}")

    try:
        data = await reader.read(1024)
        if not data:
            writer.close()
            await writer.wait_closed()
            return

        text = data.decode()
        processed = double_vowels(text)

        # Determine response
        if result_queue.empty():
            response = "OK"
        else:
            response = await result_queue.get()

        # Put current processed text into queue
        await result_queue.put(processed)

        # Send response
        writer.write(response.encode())
        await writer.drain()

    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed: {addr}")

# Start asyncio server
async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Server listening on {addrs}")

    async with server:
        await server.serve_forever()

# Run server
asyncio.run(main())



#lock condition


import asyncio

shared_list = []
lock = asyncio.Lock()

async def add_item(item):
    async with lock:   # ensure only one coroutine modifies the list at a time
        shared_list.append(item)
        await asyncio.sleep(0.1)  # simulate some work


#run two funcs same

async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())

    # Wait for both to complete
    result1 = await task1
    result2 = await task2

    print(result1, result2)

asyncio.run(main())