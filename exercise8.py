# Write a program that will compute the area of a circle. 
# Prompt the user to enter the radius and 
# print a nice message back to the user with the answer.
import math

print('===================')
print(' Area of a Circle ')
print('===================')

r = int(input('Enter radius: '))

area = math.pi * ( r * r)


print('The area of a circle with a radius of ',  r , 'is: ' , round(area,2) )

