"""Febonacci Series using recursion """

def fun(i):
    if i<=1:
        return i
    else:
        return fun(i-1)+fun(i-2)  
n=5
if n<=0:
    print("Enter a positive number : ")
else:
    print("Febonacci sequence ")
    for i in range(1,n+1):
        print(fun(i))


"""Febonacci Series using for loop """

def febo(n ) :
      if n<=0:
            print("Enter a positive no : ")
            return
      else:
            a=0
            b=1
            if n==1:
                  print(a)
            else:
                  print(a)
                  print(b)
                  for i in range(2,n):
                        c=a+b
                        a=b
                        b=c
                        print(c)




n=int(input("Enter the no : "))
febo(n)
      




 
    
