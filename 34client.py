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

