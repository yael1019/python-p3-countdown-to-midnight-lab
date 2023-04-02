# your code goes here!
import time

def countdown(int):
    while int >= 0:
        if int == 0:
            print('HAPPY NEW YEAR!')
        else:
            print(f'{int} SECOND(S)!')
        int -= 1

# countdown(10)

def countdown_with_sleep(int):
    while int >= 0:
        if int == 0:
            print('HAPPY NEW YEAR!')
        else:
            print(f'{int} SECOND(S)!')
        int -= 1
        time.sleep(1)