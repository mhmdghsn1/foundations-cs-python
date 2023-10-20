# Ex 1 :
'''
n=int(input("Enter a random number : "))
def factorial(n):
    res=[]
    
    if n<=0:
        return ("Error")
    if n==1:
        return [1]
    else :
        res.append(1)
        for i in range(2, n + 1):
            res.append(i)
        mul=1
        for num in res:
            mul *= num
        return mul , res

print(factorial(n))
'''

#Ex 2 :
'''
n=int(input("Enter a random number : "))
def divisors0(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def divisors1(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0 and divisors0(i):
            div.append(i)
    return div
div =divisors1(n)
print(div)

'''

#Ex 3 :
'''
string =input("Enter anything : ")
def reverseString(string):
    reverse=""
    for i in range(len(string)-1,-1,-1):
        reverse+=string[i]
    return reverse
reverse=reverseString(string)
print(reverse)

'''

#Ex 4 :
'''
integers0 =input("Enter a list of integers with spaces : ").split()
integers1=[int(num) for num in integers0]
def inputIntegers(integers):
    even=[]
    for num in integers :
        if num % 2 == 0 :
            even.append(num)
    return even

even=inputIntegers(integers1)
print(even)
'''

#Ex 5 :
'''
password =input("Enter new password : ")
def check_password(password):
    if len(password)<8 :
        return "“Weak password”"
    
    dig=False
    uper=False
    lower=False
    special=False
    for i in password:
        if i.isupper():
            uper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            dig=True
        elif i in ['!','#','$','?']:
            special =True
    if dig and uper and lower and special :
        return "“Strong password”"
    else:
        return "“Weak password”"
new_password=check_password(password)
print(new_password)

'''