# Write a program that will convert degrees 
# fahrenheit to degrees celsius.

print('=====================')
print(' Celsius to fahrenheit ')
print('=====================')

far = float( input('fahrenheit: ') )

cel = round( ( far - 32 ) * (5/9), 2)

# Formula
# (32 °F − 32) × 5/9 = 0 °C

print( far, 'fahrenheit to celsius is ', cel )

