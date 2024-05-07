def fibo(i):
    if i<=1:
        return i
    else:
        return fibo(i-1)+fibo(i-2)
n=int(input("Enter A number here : "))
if n<=0:
    print("Enter a positive number : ")
else:
    for i in range(n):
        print(fibo(i))
    
    
