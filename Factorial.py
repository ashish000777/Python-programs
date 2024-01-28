def factorial(num):
    if(num<0):
        return "Factorial is not calculated for negative numbers"
    
    elif(num==0):
        return 1
    
    else:
        product = 1
        for i in range(1, num+1):
            product *= i
        return product
number = int(input("Enter the number: "))
factorialResult = factorial(number)
print(f"{number} factorial is: ", factorialResult)
