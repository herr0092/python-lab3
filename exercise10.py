# Write a program that will compute MPG for a car. 
# Prompt the user to enter the number of miles driven 
# and the number of gallons used. 
# Print a nice message with the answer.

print('===================')
print('   MPG for a car ')
print('===================')

minimun = int(input('Enter miles driven: '))
galons  = int( input('Enter number of gallons used: ') )

mpg = minimun * galons

print('MPG is:', mpg )