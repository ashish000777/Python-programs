def primeNumber(num):
    if num<=1:
        return False
    
    if num<=3:
        return True
    
    if num%2==0 or num%3==0:
        return False
    
    i = 5
    while i*i <= num:
        if num%i==0 or num%(i+1)==0:
            return False
        i+=6
    
    return True

number = int(input("Enter a number: "))
primeResult = primeNumber(number)
print(f"{number} is prime: ", primeResult)
