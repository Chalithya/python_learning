# hello = input("Enter your Name  ")
# print(hello)

# bday = input(" Enter your Birth Year: ")
# bday = 2020 - int(bday)
# print(bday)3

# #Sum
# fnumber = float(input(" Enter First Number: "))
# lnumber = float(input(" Enter Second Number: "))

# print("The Sum is " + str(fnumber+ lnumber))


# course = ' This is a text'
# print(course.replace('a', '4'))


# x=2
# y=3
# z=3

# y=+x
# z+=x

# print(x)
# print(y)



# weight = float(input("Enter your weight: "))
# type = input("Is it Kg(k) or Lb(L): ")

# if type=='K' or type=='k':
#     print(weight*2.20462262185)
# elif type=='L' or type=='l' :
#     print(weight*0.453592)
# else :
#     print("You have enterd a wrong type")


# number = [1,2,3,4,5]

# for item in number:
#     print(item)

# i=0

# while i<len(number):
#     print(number[i])
#     i+=1

# swapping 2 varaibles
# x = 5
# y = 10

# y = x+y
# x = y-x
# y = y-x

# print(str(x)+" "+ str(y))


# Guessing Game

# secret_number = 5
# guess_count = 0
# guess_limit = 3
# guess_value =0

# while guess_count<guess_limit:
#     guess_value = int(input("Enter your value: "))
#     if guess_value==secret_number:
#         print("You won")
#         break
#     else:
#         print("Try again")
#     guess_count+=1

# else:
#     print("Sorry You Failed")

    
# Car Game    

# command = ''
# print('type Help for help')
# while True:
#     command =  input('> ')
#     if command.upper() == 'HELP':
#         print('''
#         Start ---->  Start the car
#         Stop  ---->  Stop the car
#         Quit  ---->  Exit the process''')

#     elif command.upper() == 'START':
#         print('Car started ... Ready to go')

#     elif command.upper() == 'STOP':
#         print('Car stopped ...')

#     elif command.upper() == 'QUIT':
#         print('Exiting ...')
#         break

#     else:
#         print("I don't understand")

# else:
#     print('Process ended')

###################################
#For loop

# prices = [10,20,30]
# tot = 0
# for price in prices:
#     tot+=price

# print(tot)


# Nested Loops

# for x in range(4):
#     for y in range(4):
#         print(f'({x},{y})')


# numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     op = ''
#     for val in range(number):
#         op+='x'
#     print(op)

################################### 
# Lists
# numbers = [3, 6, 10, 2, 8, 4]

# max = numbers[0]
# for number  in numbers:
#     if max<number:
#         max=number
# print(f'The Largest number is {max}')


#############################
#2D Lists

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix[0][0])

# for row in matrix:
#     for val in row:
#         print(val)



# numbers = [3,45,5,7,1,23,9, 9 , 45]

# numbers.sort()
# numbers.reverse()
# print(numbers)

# Removing duplicates

# numbers = [3, 45, 5, 7, 1, 23, 9, 9 , 45]

# uniqueList = []

# for number in numbers:
#     if number not in uniqueList:
#         uniqueList.append(number)

# print(uniqueList)


#################################
#Tuples
# number = (1, 2, 3)
 
# Dictionaries

# phoneNo = input('Enter your phone number: ')

# values = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five",
#     "6" : "Six",
#     "7" : "Seven",
#     "8" : "Eight",
#     "9" : "Nine"
# }

# output = ""

# for ph in phoneNo:
#     output+=values.get(ph,"#")+" "

# print(output)

# Emoji app

# txt = input("> ")

# words = txt.split(' ')

# emoji = {
#     ":)" : "😊",
#     ":(" : "😢"
# }
# output = ""

# for word in words:
#     output+= emoji.get(word, word)

# print(output)
#########################################

# Functions

# firstName = input('Enter Your First Name: ')
# lastName = input('Enter Your Last Name: ')
# def greetiing_message(fname, lname):
#     print(f'Hello {fname} {lname}')
#     print('My name is Floki')


# print('start')
# greetiing_message(fname=firstName, lname= lastName)
# greetiing_message(firstName,  lastName)

# print('End')


# number = int(input('Enter a number: '))

# def square(num):
#     return num**2


# print(square(number))

# Emoji app with functions

# txt = input("> ")

# def emoji_converter(message):
#     words = txt.split(' ')
#     emoji = {
#         ":)" : "😊",
#         ":(" : "😢"
#     }
#     output = ""
#     for word in words:
#         output+= emoji.get(word, word)
#     return output


# print(emoji_converter(txt))

# Exception Handling

# try:
#     age = int(input('Age: '))
# except:
#     print('Something went wrong')


# try:
#     age = int(input('Age: '))
#     income = 200
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot divide by 0')
# except  ValueError:
#     print('invalid value')
# else:
#     print('Nothing went wrong')
# finally:
#     print('try except is finished')


#Raising an exception
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")