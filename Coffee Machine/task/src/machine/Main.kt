package machine

import java.util.Scanner

enum class MachineState {
    ACTION {
        override fun printCommand() {
            print("Write action (buy, fill, take, remaining, exit): ")
        }
    },
    COFFEE {
        override fun printCommand() {
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        }
    },
    WATER {
        override fun printCommand() {
            print("Write how many ml of water do you want to add: ")
        }
    },
    MILK {
        override fun printCommand() {
            print("Write how many ml of milk do you want to add: ")
        }
    },
    BEANS {
        override fun printCommand() {
            print("Write how many grams of coffee beans do you want to add: ")
        }
    },
    CUPS {
        override fun printCommand() {
            print("Write how many disposable cups of coffee do you want to add: ")
        }
    };
    abstract fun printCommand()
}

class CoffeeMachine(
    var water: Int = 400,
    var milk: Int = 540,
    var beans: Int = 120,
    var cups: Int = 9,
    var money: Int = 550) {

    var state = MachineState.ACTION

    fun take() {
        println("I gave you $$money")
        money = 0
    }

    fun remaining() {
        println("The coffee machine has:")
        println("$water of water")
        println("$milk of milk")
        println("$beans of coffee beans")
        println("$cups of disposable cups")
        println("$money of money")
    }

    fun input(value: String): Boolean {
        when (state) {
            MachineState.ACTION -> when (value) {
                "buy" -> state = MachineState.COFFEE
                "fill" -> state = MachineState.WATER
                "take" -> take()
                "remaining" -> remaining()
                "exit" -> return false
            }
            MachineState.COFFEE -> {
                when (value) {
                    "1" -> expresso()
                    "2" -> latte()
                    "3" -> cappuccino()
                }
                state = MachineState.ACTION
            }
            MachineState.WATER -> {
                water += value.toInt()
                state = MachineState.MILK
            }
            MachineState.MILK -> {
                milk += value.toInt()
                state = MachineState.BEANS
            }
            MachineState.BEANS -> {
                beans += value.toInt()
                state = MachineState.CUPS
            }
            MachineState.CUPS -> {
                cups += value.toInt()
                state = MachineState.ACTION
            }
        }
        return true
    }

    fun expresso() {
        val waterPerCup = 250
        val beansPerCup = 16
        val costPerCup = 4

        when {
            water < waterPerCup -> println("Sorry, not enough water!")
            beans < beansPerCup -> println("Sorry, not enough coffee beans!")
            else -> {
                println("I have enough resources, making you a coffee!")
                water -= waterPerCup
                beans -= beansPerCup
                money += costPerCup
                cups--
            }
        }
    }

    fun latte() {
        val waterPerCup = 350
        val milkPerCup = 75
        val beansPerCup = 20
        val costPerCup = 7

        when {
            water < waterPerCup -> println("Sorry, not enough water!")
            milk < milkPerCup -> println("Sorry, not enough milk!")
            beans < beansPerCup -> println("Sorry, not enough coffee beans!")
            else -> {
                println("I have enough resources, making you a coffee!")
                water -= waterPerCup
                milk -= milkPerCup
                beans -= beansPerCup
                money += costPerCup
                cups--
            }
        }
    }

    fun cappuccino() {
        val waterPerCup = 200
        val milkPerCup = 100
        val beansPerCup = 12
        val costPerCup = 6

        when {
            water < waterPerCup -> println("Sorry, not enough water!")
            milk < milkPerCup -> println("Sorry, not enough milk!")
            beans < beansPerCup -> println("Sorry, not enough coffee beans!")
            else -> {
                println("I have enough resources, making you a coffee!")
                water -= waterPerCup
                milk -= milkPerCup
                beans -= beansPerCup
                money += costPerCup
                cups--
            }
        }
    }
}

fun main() {
    val scanner = Scanner(System.`in`)
    val machine = CoffeeMachine()
    var action: Boolean
    do {
        machine.state.printCommand()
        action = machine.input(scanner.next())
    } while (action)
}