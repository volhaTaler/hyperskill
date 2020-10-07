class CoffeeMachine:
    existing_ingredients = {"water": 0, "milk": 0, "coffee beans": 0, "disposable cups": 0, "money": 0}
    DRINKS = {"1": "ESPRESSO", "2": "LATTE", "3": "CAPPUCCINO"}
    ESPRESSO = {"water": 250, "coffee beans": 16, "disposable cups": 1, "money": 4}
    LATTE = {"water": 350, "coffee beans": 20, "milk": 75, "disposable cups": 1, "money": 7}
    CAPPUCCINO = {"water": 200, "coffee beans": 12, "milk": 100, "disposable cups": 1, "money": 6}
    lst = [DRINKS, ESPRESSO, LATTE, CAPPUCCINO]
    ACTIONS = {"take": "take", "buy": "buy", "fill": "fill", "remaining": "remaining", "exit": "exit"}

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        CoffeeMachine.existing_ingredients["water"] = water
        CoffeeMachine.existing_ingredients["milk"] = milk
        CoffeeMachine.existing_ingredients["coffee beans"] = beans
        CoffeeMachine.existing_ingredients["disposable cups"] = cups
        CoffeeMachine.existing_ingredients["money"] = money
    def print_supplies(self):
        print("The coffee machine has:")
        for key in CoffeeMachine.existing_ingredients:
            print(f"{CoffeeMachine.existing_ingredients[key]} of {key}")
    
    def choose_action(self):
        print()
        print("Write an action (buy, fill, take, remaining, exit):")
        return input()
    
    def take_action(self):
        print(f"I gave you $ {CoffeeMachine.existing_ingredients['money']}")
        CoffeeMachine.existing_ingredients["money"] = 0
        print()
    
    def buy_drink(self, drink):
        for key in drink:
            CoffeeMachine.existing_ingredients[key] -= drink[key]
        CoffeeMachine.existing_ingredients["money"] += 2 * drink["money"]
    
    def remaining_action(self):
        print()
        self.print_supplies()
    
    def exit_action(self):
        return False
    
    def check_supplies(self, drink):
        needed_supplies = []
        for key in drink:
            if CoffeeMachine.existing_ingredients[key] < drink[key]:
                needed_supplies.append(key)
        
        return needed_supplies
          
    def print_necessary_supplies(self, needed_supplies):
        for item in needed_supplies:
            print(f"Sorry, not enough {item}!")
        
    def buy_action(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        chosen_drink = input()
        if chosen_drink in CoffeeMachine.DRINKS.keys():
            needed_supplies = self.check_supplies(CoffeeMachine.lst[int(chosen_drink)])
            if not needed_supplies:
                print("I have enough resources, making you a coffee!")
                self.buy_drink(CoffeeMachine.lst[int(chosen_drink)])
            else:
                self.print_necessary_supplies(needed_supplies)
        else:
            print("There is no drinks with such ID. Please choose 1 - espresso, 2 - latte, 3 - cappuccino:")
    
    def fill_action(self):
        print("Write how many ml of water do you want to add:")
        CoffeeMachine.existing_ingredients["water"] += int(input())
        print("Write how many ml of milk do you want to add:")
        CoffeeMachine.existing_ingredients["milk"] += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        CoffeeMachine.existing_ingredients["coffee beans"] += int(input())
        print("Write how many disposable cups do you want to add:")
        CoffeeMachine.existing_ingredients["disposable cups"] += int(input())
        print()

    def working_mode(self):
        work = True
        while work:
            action = self.choose_action()
            if action == CoffeeMachine.ACTIONS["take"]:
                self.take_action()
            elif action == CoffeeMachine.ACTIONS["buy"]:
                self.buy_action()
            elif action == CoffeeMachine.ACTIONS["fill"]:
                self.fill_action()
            elif action == CoffeeMachine.ACTIONS["remaining"]:
                self.remaining_action()
            else:
                work = self.exit_action()
        
      
def main():
    obj = CoffeeMachine()
    obj.working_mode()

####  start ####### 

main()  
 