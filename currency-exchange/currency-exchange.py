'''
import requests
import simplejson

cache = {}


def enter(two):
    mon = cache[two]["inverseRate"]
    money = round(mon, 2)
    print(f'You received {round((numb / money), 2)} {str(two).upper()}.')


if name == 'main':
    main_val = input('> ').strip().lower()

    while True:

        while True:
            try:
                s_val = input('> ').strip().lower()
                numb = int(input('> '))
                break
            except ValueError:
                print('Invalid input')


        print('Checking the cache...')
        if s_val in cache:
            print('It is in the cache!')
            enter(s_val)

            f = str(input("Do you want to continue? > "))
            if f == "yes":
                pass
            elif f == "no":
                print("Bye")
                break

        else:
            print('Sorry, but it is not in the cache!')
            try:
                val_try = requests.get(f'http://www.floatrates.com/daily/{main_val}.json')
                x = val_try.json()
                cache = dict(x)
                enter(s_val)

                f = str(input("Do you want to continue? > "))
                if f == "yes":
                    pass
                elif f == "no":
                    print("Bye")
                    break

            except simplejson.JSONDecodeError:
                print('error')'''