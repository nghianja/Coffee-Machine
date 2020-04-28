ml_of_water = int(input("Write how many ml of water the coffee machine has:"))
ml_of_milk = int(input("Write how many ml of milk the coffee machine has:"))
grams_of_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups_of_coffee_needed = int(input("Write how many cups of coffee you will need:"))

water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15

cups_of_coffee_made = 0

while water_per_cup <= ml_of_water and \
        milk_per_cup <= ml_of_milk and \
        beans_per_cup <= grams_of_beans:
    cups_of_coffee_made += 1
    ml_of_water -= water_per_cup
    ml_of_milk -= milk_per_cup
    grams_of_beans -= beans_per_cup

if cups_of_coffee_made >= cups_of_coffee_needed:
    message = "Yes, I can make that amount of coffee"
    if cups_of_coffee_made > cups_of_coffee_needed:
        message += " (and even {} more than that)".format(cups_of_coffee_made - cups_of_coffee_needed)
    print(message)
else:
    print("No, I can make only {} cups of coffee".format(cups_of_coffee_made))
