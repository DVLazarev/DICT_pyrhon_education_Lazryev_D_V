def cof():
    w = int(input("Please how many water has coffee machine: > "))
    m = int(input("Please how many milk has coffee machine: > "))
    b = int(input("Please how many beans has coffee machine: > "))
    c = int(input("Please how many cups you need: > "))
    water = w // 200
    milk = m // 50
    beans = b // 15
    cup = [water, milk, beans]
    cup2 = min(cup)
    if cup2 == c:
        print("Yes i can make coffee for you!")
    elif cup2 > c:
        print("Yes i can make coffee for you (and even " + str(cup2) + "more than that)")
    else:
        print("No, i can make only " + str(cup2) +"cups of coffee")
cof()

