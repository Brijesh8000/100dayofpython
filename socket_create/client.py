# # import socket
# # c = socket.socket()
# # c.connect(('localhost',9999))
# # name=input('Enter your name')
# # c.send(bytes(name, 'utf-8'))
# # print(c.recv(1024).decode())
# # # c.send('client')
# no=(1,10,4,5 )
# # no=tuple(no)
# # no[0]=2
# s=sorted(no)
# print(no)
# def thrive(n):
#     if n % 15 == 0:
#        print("thrive", end = “ ”)
#     elif n % 3 != 0 and n % 5 != 0:
#        print("neither", end = “ ”)
#     elif n % 3 == 0:
#        print("three", end = “ ”)
#     elif n % 5 == 0:
#        print("five", end = “ ”)

# e="Python programming"
# n=len(e)
# w1=e.upper()
# w2=e.lower()
# c_w=""
# for i in range(n):
#     if i%2==0:
#         c_w+=w2[i]
#     else:
#         c_w+=w1[i]
# print(c_w)
# # print(e[-3:-1])
#
# d={"f":"s","g":"r"}
# d1={2:3,4:5}
# d.update(d1)
# print(d)
#
# a=[1,3]
# print(a*3)
# print(type(5/2))
# print(type(5//2))
numbers = (4, 7, 19, 2, 89, 45, 72, 22)

sorted_numbers = sorted(numbers)

even = lambda a: a % 2 == 0

even_numbers = filter(even, sorted_numbers)

print(type(even_numbers))
