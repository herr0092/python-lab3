# Write a program that will convert 
# degrees celsius to degrees fahrenheit.

print('===================')
print(' Celsius to fahrenheit ')
print('===================')

cel = int( input('Enter celsius temperature: ') )

far = round( (( cel ) * (9/5)) + 32, 2 )

print( cel, 'celsius to fahrenheit is ', far )