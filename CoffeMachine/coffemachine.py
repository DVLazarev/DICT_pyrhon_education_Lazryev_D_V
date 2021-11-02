class CoffeeMachine:
    def __init__(self):
        self.w = 400
        self.m = 540
        self.b = 120
        self.c = 9
        self.mon = 550

    def fill(self):
        self.w += int(input("Write how many water do want: > "))
        self.m += int(input("Write how many milk do want: > "))
        self.b += int(input("Write how many beans do want: > "))
        self.c += int(input("Write how many cups do want: > "))


    def esp(self):
        if self.w < 250:
            print("Sorry, enough water in coffee machine.")
        elif self.b < 16:
            print("Sorry, enough beans in coffee machine.")
        elif self.c < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.w -= 250
            self.b -= 16
            self.c -= 1
            self.mon += 4
            print("""Starting make a coffee
Griding coffee beans
Boiling water
Mixing water with crushed beans
Pouring coffee into cup
Coffee ready!""")

    def lat(self):
        if self.w < 350:
            print("Sorry, enough water in coffee machine.")
        elif self.m < 75:
            print("Sorry, enough milk in coffee machine.")
        elif self.b < 20:
            print("Sorry, enough beans in coffee machine.")
        elif self.c < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.w -= 250
            self.m -= 75
            self.b -= 16
            self.c -= 1
            self.mon += 7
            print("""Starting make a coffee
Griding coffee beans
Boiling water
Mixing water with crushed beans
Pouring coffee into cup
Adding milk into your coffee
Coffee ready!""")


    def cap(self):
        if self.w < 200:
            print("Sorry, enough water in coffee machine.")
        elif self.m < 100:
            print("Sorry, enough milk in coffee machine.")
        elif self.b < 12:
            print("Sorry, enough beans in coffee machine.")
        elif self.c < 1:
            print("Sorry, enough cups in coffee machine.")
        else:
            self.w -= 250
            self.m -= 75
            self.b -= 16
            self.c -= 1
            self.mon += 6
            print("""Starting make a coffee
Griding coffee beans
Boiling water
Mixing water with crushed beans
Pouring coffee into cup
Adding milk into your coffee
Coffee ready!""")


    def take(self):
        print(f"I gave you {self.mon} uah.")
        self.mon = self.mon - self.mon


    def remaining(self):
        print(f"""In coffee machine:
        {self.w} of water.
        {self.m} of milk.
        {self.b} of beans.
        {self.c} of cups.
        {self.mon}  of money.""")


objects = CoffeeMachine()
while True:
    act = str(input("Write action (buy, fill, take, remaining, exit): >  "))
    if act == "buy":
        while act != "back":
            selecting = input("What you wanna buy; 1 - espresso, 2 - latte, 3 - cappuccino.")

            if selecting == "1":
                objects.esp()
                break
            if selecting == "2":
                objects.lat()
                break
            if selecting == "3":
                objects.cap()
                break
    if act == "fill":
        objects.fill()
    if act == "take":
        objects.take()
    if act == "exit":
        break
    if act == "remaining":
        objects.remaining()