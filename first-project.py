class Calculator:

    def __init__(self):
        pass

    
    def addition(self, x, y):
        sum = x + y
        
        print(sum)

    def subtraction(self, x, y):
        sub = x - y

        print(sub)

    def mutliply(self, x, y):
        multiply = x * y

        print(multiply)

    def divide(self, x, y):
        div = x/y

        print(div)

basic_calc = Calculator()

option = str(input("What do you want to do(add, subtract, mutliply, divide): "))

x = int(input("Enter the first number: "))

y = int(input("Enter the second number: "))

if option == "add":
    basic_calc.addition(x,y)

elif option == "subtract":
    basic_calc.subtraction(x,y)

elif option == "multiply":
    basic_calc.mutliply(x,y)

else:
    basic_calc.divide(x,y)




