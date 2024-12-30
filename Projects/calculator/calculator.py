# This program is for a simple calculator

def simple_calc() :
    operators = ['+', '-', '*', '/', '%']
    try:
        num1 = int(input('Enter the first number: '))
        operator = input('Enter the operator(+,-,*,/,%): ')
        num2 = int(input("Enter the Second number: "))
        if operator not in operators :
            print('Invalid Operator!')
        
        if operator == '+' :
            solution = num1 + num2
        elif operator == '-' :
            solution = num1 - num2
        elif operator == '*' :
            solution = num1 * num2
        elif operator == '/' :
            solution = num1 - num2
        elif operator == '%' :
            solution = num1 * num2

        print('The answer is: ', solution)
    except:
        print('Please Enter a valid number.')



simple_calc()