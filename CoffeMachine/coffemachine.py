w = 400
m = 540
b = 120
c = 9
mon = 550


def esp():
    global  w, b, c, mon
    w -= 250
    b -= 16
    c -= 1
    mon += 4
    return


def lat():
    global  w, m, b, c, mon
    w -= 350
    m -= 75
    b -= 20
    c -= 1
    mon += 7
    return


def cap():
    global  w, m, b, c, mon
    w -= 200
    m -= 100
    b -= 12
    c -= 1
    mon += 6
    return


def cof_trade():
    global w, m, b, c, mon
    print("The coffee machine has\n  " + str(w) + "  of water\n  "+ str(m) + "  of milk\n  " + str(b) + "  of beans\n  " + str(c) + "  of cup\n  ")
    print(str(mon) + " of money")


def buy():
    a = int(input("What do you wanna buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if a == 1:
        esp()
    if a == 2:
        lat()
    if a == 3:
        cap()
    else:
        print("No, i can make only: espresso, latte, capuchino" +"  cups of coffee")
        print("Please enter correct number.")
cof_trade()


def fill():
    global w, m, b, c, mon
    w += int(input("How many water you want?: "))
    m += int(input("How many milk you want?: "))
    b += int(input("How many beans you want?: "))
    c += int(input("How many cups you want?: "))
cof_trade()

def take():
    global  mon
    print("You give me" + str(mon))
    mon -= mon
cof_trade()


while True:
    cof_trade()
    print("")
    answer = input("Write action (buy, fill, take):  ")
    if answer == "buy":
        buy()
    elif answer == "fill":
        fill()
    elif answer == "take":
        take()
    else:
        print("Write your answer correctly!")