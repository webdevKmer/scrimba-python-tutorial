msg='welcome to Python 101: Strings'

# Lists Exercices
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

last_sale = int(input('How much lemonade did you sell the last day : '))

sales_w2.append(last_sale)
print(sales_w2)
# sales.extend(sales_w2)
# sales.extend(sales_w1)
sales = sales_w1 + sales_w2
# sales.sort()
# print(f'The best day, i earned : {sales[-1] * 1.5} $')
# print(f'The worst day, i earned : {sales[0] * 1.5} $')

print(f'The worst day, i earned : {min(sales) * 1.5} $')
print(f'The best day, i earned : {max(sales) * 1.5} $')


# # User Input Exercices
# name = input("Whats's your name ? ")
# distance = int(input("Whats's the distance in km ? "))

# print(f'Hi {name.title()}, the distance you entered is {distance} kms or {round(distance/1.609,1)} miles.')

#  String Exercices 
# print(msg)
# # print(msg[18:19], msg[0:7].capitalize(), msg[-5:-1:].capitalize(), msg[8:10].capitalize(), "tyler".capitalize())
# newStr = msg[18:19] + ' ' + msg[0:7].capitalize() + ' ' + msg[-5:-1:].capitalize() + ' ' + msg[8:10].capitalize() + ' ' + "tyler".capitalize()
# print(newStr)

# print(newStr[::-1])