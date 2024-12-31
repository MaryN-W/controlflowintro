# # Conditional statements

# lets_code = False # Declaring a boolean variable

# # if lets_code is True: # short version = lets_code: bc boolean value created above 
# # #     # If executes if condition evaluates to True 
# # #     # Else executes if condition is False
# #     print('We love coding!') # automatically indented - Can end here without else statement
#  else: 
#      print('We like other stuff')
# #  print('Period!') # Outdented to start a new block 

# # Ternary Expression - Short way to write if-else in a single line
# print('We love codng!') if lets_code else print('We like other stuff')

# Else if

# >=80 -> HD
# 70-79 -> D
# 60-69 -> C
# 50-59 -> P
# <50 -> F

# marks = 96

# if marks >= 80:
#     print('HD')
# elif marks >= 70: # and marks < 80: 
#     print('D')
# elif marks >= 60:
#     print('C')
# elif marks >= 50:
#     print('P')
# else:
#     print('F')


# Nested if

# 2 states >> State1 and State2
# State1: >=18 can vote
# State2: >=21 can vote

# state = 'State1'
# age = 21

# # Display whether they can vote or not

# # if (state == 'State1' and age >=18) or (state == 'State2'  and age >= 21)
# if state == 'State1': # Nesting if statement, Alternative to above
#     if age >= 18:
#         print('You can vote in State 1')
#     else:
#         print('You cannot vote in State 1')
# else:
#     if age >= 21:
#         print('You can vote in State 2')
#     else: 
#        print('You cannot vote in State 2')

# day_of_week = 6

# if day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')

# match day_of_week:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5: 
#         print('Friday')
#     case _: # when value provided is outside specified parameters, Always last
#         print('That is not a Weekday')

#     # 1-5: Weekday
#     # 6,7: Weekend
#     # Anything else: Error message

# match day_of_week:
#         case 1 | 2 | 3 | 4 | 5: # | represents or
#             print('Weekday')
#         case 6 | 7:
#             print('Weekend')
#         case _:
#             print('Error: Not a valid day number!')

        
    