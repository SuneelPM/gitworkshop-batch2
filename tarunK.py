def getNFactorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * getNFactorial(number - 1)
    
print(getNFactorial(6))