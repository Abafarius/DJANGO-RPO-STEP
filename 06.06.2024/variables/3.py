data = input('Enter your number in KM: ')
try:
    num = int(data)
except:
    print('Enter valid number!')

miles = num*0.621371
print('Here is your number in miles: ', miles, 'miles')