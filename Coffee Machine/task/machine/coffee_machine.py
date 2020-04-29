class CoffeeMachine:
    def __init__(self):
        self.ml_of_water = 400
        self.ml_of_milk = 540
        self.grams_of_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "action"

    def check(self, water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup):
        if self.ml_of_water < water_per_cup:
            print("Sorry, not enough water!")
        elif self.ml_of_milk < milk_per_cup:
            print("Sorry, not enough milk!")
        elif self.grams_of_beans < beans_per_cup:
            print("Sorry, not enough coffee beans!")
        else:
            self.update(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)

    def cappuccino(self):
        water_per_cup = 200
        milk_per_cup = 100
        beans_per_cup = 12
        cost_per_cup = 6
        self.check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)

    def expresso(self):
        water_per_cup = 250
        milk_per_cup = 0
        beans_per_cup = 16
        cost_per_cup = 4
        self.check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)

    def get_command(self):
        if self.state == "action":
            return input("Write action (buy, fill, take, remaining, exit): ")
        elif self.state == "coffee":
            return input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        elif self.state == "water":
            return input("Write how many ml of water do you want to add: ")
        elif self.state == "milk":
            return input("Write how many ml of milk do you want to add: ")
        elif self.state == "beans":
            return input("Write how many grams of coffee beans do you want to add: ")
        elif self.state == "cups":
            return input("Write how many disposable cups of coffee do you want to add: ")

    def latte(self):
        water_per_cup = 350
        milk_per_cup = 75
        beans_per_cup = 20
        cost_per_cup = 7
        self.check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)

    def remaining(self):
        print("The coffee machine has:")
        print("{} of water".format(self.ml_of_water))
        print("{} of milk".format(self.ml_of_milk))
        print("{} of coffee beans".format(self.grams_of_beans))
        print("{} of disposable cups".format(self.disposable_cups))
        print("{} of money".format(self.money))

    def take(self):
        print("I gave you {}".format(self.money))
        self.money = 0

    def update(self, water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup):
        print("I have enough resources, making you a coffee!")
        self.ml_of_water -= water_per_cup
        self.ml_of_milk -= milk_per_cup
        self.grams_of_beans -= beans_per_cup
        self.money += cost_per_cup
        self.disposable_cups -= 1

    def use_command(self, command):
        if self.state == "action":
            if command == "buy":
                self.state = "coffee"
            elif command == "fill":
                self.state = "water"
            elif command == "take":
                self.take()
            elif command == "remaining":
                self.remaining()
            elif command == "exit":
                return False
        elif self.state == "coffee":
            if command == "1":
                self.expresso()
            elif command == "2":
                self.latte()
            elif command == "3":
                self.cappuccino()
            self.state = "action"
        elif self.state == "water":
            self.ml_of_water += int(command)
            self.state = "milk"
        elif self.state == "milk":
            self.ml_of_milk += int(command)
            self.state = "beans"
        elif self.state == "beans":
            self.grams_of_beans += int(command)
            self.state = "cups"
        elif self.state == "cups":
            self.disposable_cups += int(command)
            self.state = "action"
        return True


machine = CoffeeMachine()
while True:
    action = machine.get_command()
    if not machine.use_command(action):
        break
