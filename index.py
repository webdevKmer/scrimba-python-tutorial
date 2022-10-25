msg='welcome to Python 101: Strings'
#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# if ('Eric' in friends) :
#     print('Yes, Eric')
# if ('John' in friends) :
#         print('Yes, John')

# all_friends = friends.union(my_friends)
# all_friends = friends | my_friends
# print(all_friends)

# duplicates_friends = friends.intersection(my_friends)
# duplicates_friends = friends & my_friends
# print(duplicates_friends)

# print(friends.difference(my_friends))
# print(friends - my_friends)
# print(my_friends.difference(friends))

# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends)

# unique_cars = set(cars)
# print(unique_cars)

# # Split and Join 

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']

# arr_to_split = csv.split(',')

# friends_list = [] + arr_to_split[:-1] + arr_to_split[-1].split(':')
# arr_to_split = friends_list.pop()

# friends_list += arr_to_split.split(';')
# print(friends_list)

# print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise


# # Lists Exercices
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []

# last_sale = int(input('How much lemonade did you sell the last day : '))

# sales_w2.append(last_sale)
# print(sales_w2)
# # sales.extend(sales_w2)
# # sales.extend(sales_w1)
# sales = sales_w1 + sales_w2
# # sales.sort()
# # print(f'The best day, i earned : {sales[-1] * 1.5} $')
# # print(f'The worst day, i earned : {sales[0] * 1.5} $')

# print(f'The worst day, i earned : {min(sales) * 1.5} $')
# print(f'The best day, i earned : {max(sales) * 1.5} $')


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