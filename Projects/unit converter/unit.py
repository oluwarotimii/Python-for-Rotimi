

def converter():
    print('Welcome to the Unit Converter. what you want to convert?')
    options = {
        1 : 'Meters to Killometers',
        2 : 'Celsius to Fahrenheit',
        3 : 'Meters to Miles',
        4 : 'Miles to Meters',
        5 :  'Meters to Killometers',
        6 :  'Celsius to Kelvin'
    }
    # prompt = input('What do you want to convert? : ') 
    for key,  value in options.items():
        print(key,":", value)
   
    try: 
        choice = int(input('Enter number of your choice : '))
    except ValueError:
        print('Invalid Input, Please Enter a number.')
        return
    
    if choice not in options:
        print('Invalid Choice, Please select a valid option.')
        return
    
    try: 
        value = int(input('Enter number you want to convert : '))
    except ValueError:
        print('Invalid Input, Please Enter a number.')
        return

    if choice == 1:
        result = value / 1000
        print(f'{value} miles is equal to {result} meters.')
    elif choice == 2:
        result = value + 10
        print(f'{value} miles is equal to {result} meters.')
    elif choice == 3:
        result = value * 0.000621371
        print(f'{value} meters is equal to {result} miles.')
    elif choice == 4:
        result = value / 0.000621371
        print(f'{value} meters is equal to {result} miles.')
    elif  choice == 5:
        result = value * 1000
        print(f'{value} miles is equal to {result} meters.')
    elif choice == 6:
        result = value + 273
        print(f'{value} Celsius is equal to {result} Kelvin.')

converter()