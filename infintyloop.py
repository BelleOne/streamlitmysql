import time
num = 0
round = 1

while True:
    if round <= 20:
        if num == 0:
            print(num, 'off')
            num = 1
        elif num == 1:
            print(num, 'on')
            num = 0
            time.sleep(1)
    else:
        break
    round = round + 1
    # num = num + 1
