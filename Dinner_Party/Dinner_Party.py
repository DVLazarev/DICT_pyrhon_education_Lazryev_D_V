import random
count = int(input("Enter the number of friends joining (including you):"))
ls = []
def dict_update(items,values =0,lucky=None):
    result = {}
    for key in items.keys():
        if lucky is not None:
            if key == lucky:result[key] = 0
            else:result[key] = values
        else:result[key] = values
    return result
if count >=1:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(count):
        ls.append(input())
    peoples = dict_update(dict.fromkeys(ls))
    money = int(input("Enter the total amount: "))
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_check = False
    if answer == "Yes" or answer == "yes":
        lucky = random.choice(list(peoples.keys()))
        print(f"{lucky} is the lucky one!")
        lucky_check = True
    else:
        print("No one is going to be lucky ")
    if lucky_check == True :
        res_money = round(money/(count-1),2)
        peoples = dict_update(peoples,res_money,lucky)
    else:
        res_money = round(money / (count ), 2)
        peoples = dict_update(peoples, res_money)
    print(peoples)
else:
    print("No one is joining for the party ")