print('################ Basic Calculator ################')
mode = input('Select a Mode: "Operation" or "Conversion" : ')
if (mode == 'Operation'):
    first = input('First Value : ')
    second = input('Second Value : ')
    operation = input('Enter an operation "+", "-", "x", "/" : ')
    if(operation == '+'):
        print(f'Result : {int(first) + int(second)}')
    elif (operation == "-"):
        print(f'Result : {int(first) - int(second)}')
    elif (operation == "x"):
        print(f'Result : {int(first) * int(second)}')
    elif (operation == "/"):
        if(int(second) == 0):
            print('Not a valid operation, you are dividing by zero...')
        else:
            print(f'Result : {int(first) / int(second)}')
    else:
        print('Not a valid choice!')
elif(mode == 'Conversion'):
    conversion = input('"Celsius" or "Fahrenheit" : ')
    value = input(f'Enter the value to convert : ')
    print('----------------------------------------------------')
    if (conversion == "Celsius"):
        print(f'{int(value)} Celsius is {int(value)*9/5 + 32} Farenheit.')
    elif (conversion == "Fahrenheit"):
        print(f'{int(value)} Fahrenheit is {(int(value) - 32) *5/9} Celsius.')
    else:
       print('Not a valid choice!') 
else :
    print('Bad value entered.')