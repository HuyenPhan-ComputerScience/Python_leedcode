def addBinary(a, b):
    number1 = int(a, 2)
    number2 = int(b, 2)
    sum_result = number1 + number2
    result = bin(sum_result)[2:]
    return result

a = "11"
b = "1"
result = addBinary(a, b)
print(type(result))
print(result)
