ml_of_water = 400
ml_of_milk = 540
grams_of_beans = 120
disposable_cups = 9
money = 550


def state():
    print("The coffee machine has:")
    print("{} of water".format(ml_of_water))
    print("{} of milk".format(ml_of_milk))
    print("{} of coffee beans".format(grams_of_beans))
    print("{} of disposable cups".format(disposable_cups))
    print("{} of money".format(money))


def check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup):
    global ml_of_water
    global ml_of_milk
    global grams_of_beans
    if ml_of_water < water_per_cup:
        print("Sorry, not enough water!")
    elif ml_of_milk < milk_per_cup:
        print("Sorry, not enough milk!")
    elif grams_of_beans < beans_per_cup:
        print("Sorry, not enough coffee beans!")
    else:
        update(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)


def update(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup):
    global ml_of_water
    global ml_of_milk
    global grams_of_beans
    global money
    global disposable_cups
    print("I have enough resources, making you a coffee!")
    ml_of_water -= water_per_cup
    ml_of_milk -= milk_per_cup
    grams_of_beans -= beans_per_cup
    money += cost_per_cup
    disposable_cups -= 1


def expresso():
    water_per_cup = 250
    milk_per_cup = 0
    beans_per_cup = 16
    cost_per_cup = 4
    check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)


def latte():
    water_per_cup = 350
    milk_per_cup = 75
    beans_per_cup = 20
    cost_per_cup = 7
    check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)


def cappuccino():
    water_per_cup = 200
    milk_per_cup = 100
    beans_per_cup = 12
    cost_per_cup = 6
    check(water_per_cup, milk_per_cup, beans_per_cup, cost_per_cup)


def buy():
    purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if purchase == "1":
        expresso()
    elif purchase == "2":
        latte()
    elif purchase == "3":
        cappuccino()


def fill():
    water_to_fill = int(input("Write how many ml of water do you want to add: "))
    milk_to_fill = int(input("Write how many ml of milk do you want to add: "))
    beans_to_fill = int(input("Write how many grams of coffee beans do you want to add: "))
    cups_to_fill = int(input("Write how many disposable cups of coffee do you want to add: "))

    global ml_of_water
    global ml_of_milk
    global grams_of_beans
    global disposable_cups

    ml_of_water += water_to_fill
    ml_of_milk += milk_to_fill
    grams_of_beans += beans_to_fill
    disposable_cups += cups_to_fill


def take():
    global money
    print("I gave you {}".format(money))
    money = 0


while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        state()
    else:
        break
