data = input('Enter your number: ')
try:
    num = int(data)
except:
    print('Enter valid number!')

degree = num**2
print('Here is your doubled number: ', degree)
