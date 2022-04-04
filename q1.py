class Calculator:
    def addition(self):
        add = a + b
        print("The value after addition is",add)
    
    def subtraction(self):
        sub =  a - b
        print("The value after subtracting is",sub)
    
    def multiplication(self):
        multiply = a * b
        print("The value after multiplying: ",multiply)

    def division(self):
        div = a/b
        print("The value after dividing is",div)

    def clear(self):
        a=0
        b=0
        print("Inputs have been cleared")
        print("first input is now: ",a)  
        print("first input is now: ",b)  



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Calculator()
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
obj.clear()