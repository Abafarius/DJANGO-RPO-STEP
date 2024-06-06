data = input('Enter your number: ')
data1 = input('Enter your number: ')
try:
    num = int(data)
    num1 = int(data1)
except:
    print('Enter valid number!')

mean = (num+num1)/2
print('Here is your doubled number: ', mean)