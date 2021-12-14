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
    print(peoples)
else:
    print("No one is joining for the party ")