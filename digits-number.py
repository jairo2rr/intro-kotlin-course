num1 = int(input("Enter first number:"))

num2 = int(input("Enter second number:"))

print("Numbers inserted:\n", num1, "\n", num2)

def countDigits(num):
    count = 0
    while num > 0:
        num //= 10
        count +=1
    return count

print("Mayor #digitos:", num1 if countDigits(num1)>countDigits(num2) else num2)





