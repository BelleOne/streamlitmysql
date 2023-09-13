try:
    num1 = int(input('enter the fisrt number:'))
    num2 = int(input('enter the second number:'))
    print(f'{num1} / {num2} = {num1/num2}')
    # print(f'Result is {num1/num2})


except ValueError:
    print('Please enter a valid number')

except ZeroDivisionError:
    print('Cannot divide by zero')

except Exception:
    print('Soemting exception', Exception)
# else:
