import random
from entities.hero import Hero

ENCOUNTER_TYPES = {
    "Innkeeper": 20,
    "Merchant": 20,
    "Huntsman": 30,
    "Enemy": 30
}


def roll_check(stat: int, target: int) -> bool:
    dice_roll = random.randint(1, 20)
    full_stat = dice_roll + stat
    if full_stat >= target:
        return True
    return False

def ask_about_rumours(hero: Hero):
    print("\nThe innkeeper lowers his voice.")
    print('"Strange things have been happening around these parts at night..."')
    print("\n1) Listen carefully to the local rumours")
    print("2) Pretend you are an envoy of the kingdom")

    choice = input("Choose your approach: ")

    if choice == "1":
        if roll_check(hero.intelligence, 14):
            print("\nYou piece together useful information!")
            hero.attack_modifier = 1.15
        else:
            print("\nThe rumours reveal nothing particularly useful.")

    elif choice == "2":
        if roll_check(hero.deception, 18):
            print("\nThe innkeeper believes your bluff and reveals impending threats!")
            print("\nHe requests you to spend the night at the inn.")
            print("\nYou wake up refreshed and ready for the day")
            hero.attack_modifier = 1.45

            hero.heal(int(0.2 * hero.get_max_health()))
            hero.restore_mana(int(0.2 * hero.get_max_mana()))
        else:
            print("\nThe innkeeper sees through your bluff and feeds you false information.")
            hero.attack_modifier = 0.75

    else:
        print("\nYou decide not to pursue the conversation. You have a pint at the inn and leave")

def innkeeper_encounter(hero: Hero):
    print("\nYou enter a small tavern.")
    print("The innkeeper looks up from polishing a glass.")
    print('"Welcome, traveller!! What would you like to have?"')

    print("1) Ask about rumours")
    print("2) Spend the night at the inn")
    print("3) Leave town")

    choice = input('Make a decision')
    match choice:
        case "1":
            ask_about_rumours(hero)
        case "2":
            if hero.gold < 25:
                print(f"{hero.get_name()} does not have enough Gold to rent a room")
            else:
                hero.gold -= 25
                print(f"\n{hero.get_name()} paid 25 Gold. Remaining Gold: {hero.gold}")
                print(f"{hero.get_name()} spends the night resting and recover some health and mana.")
                hero.heal(int(0.2 * hero.get_max_health()))
                hero.restore_mana(int(0.2 * hero.get_max_mana()))
        case "3":
            print(f"{hero.get_name()} finds no reason to visit the tavern and goes on their own way")
        case _:
            print("The innkeeper kicks you out of the inn, fearing that you're a spy from the neighbouring kingdom")

def buy_potions(hero: Hero, price_mul: float):
    potions = {
        "1": ("Minor Healing Draught", 10, "health"),
        "2": ("Concentrated Healing Draught", 25, "health"),
        "3": ("Pure Vitality Draught", 50, "health"),
        "4": ("Minor Arcane Elixir", 10, "mana"),
        "5": ("Potent Leyline Flask", 25, "mana"),
        "6": ("Supreme Celestial Nectar", 50, "mana")
    }

    print("\nThe list of available potions:")

    for key, (name, price, _) in potions.items():
        final_price = round(price * price_mul)
        print(f"{key}) {name} - {final_price} Gold")

    print("7) Leave")

    choice = input("\nWhich potion would you like to buy? ")

    if choice == "7":
        print("You decide not to buy anything.")
        return

    if choice not in potions:
        print("Invalid choice.")
        return

    name, price, potion_type = potions[choice]
    final_price = round(price * price_mul)

    if hero.gold < final_price:
        print("You don't have enough Gold...")
        return

    hero.gold -= final_price

    if potion_type == "health":
        hero.healing_potion_inventory.append(name)
    else:
        hero.mana_potion_inventory.append(name)

    print(f"You purchased {name} for {final_price} Gold.")
    print(f"Remaining Gold: {hero.gold}")


def merchant_encounter(hero: Hero):
    print("\nYou approach a merchant with a cart full of potions.")
    print('"Looking to buy something, traveller?"')

    print("\n1) Ask for a discount (INT Check)")
    print("2) Try to swindle the merchant (DEC Check)")
    print("3) Browse potions at the listed price")
    print("4) Leave")

    choice = input("Make a decision: ")

    match choice:
        case "1":
            if roll_check(hero.intelligence, 15):
                print('\nThe merchant yields to your smooth words and offers a short discount')
                buy_potions(hero, 0.85)
            else:
                print("\nThe merchant turns the tables and you must now pay an extra tax on top of the price")
                buy_potions(hero, 1.1)
        case "2":
            if roll_check(hero.deception, 18):
                print("\nThe merchant hands over a Concentrated Healing Draught and a Potent Leyline Flask free of charge. He now feels he has been blessed by the Gods!")
                hero.mana_potion_inventory.append('Potent Leyline Flask')
                hero.healing_potion_inventory.append('Concentrated Healing Draught')
            else:
                print("\nThe merchant is convinced that the hero is a devil worshipper and flings a bomb at the hero")
                hero.cur_health -= 30
        case "3":
            buy_potions(hero, 1.0)
        case "4":
            print("You admire the merchant's wares but decide not to purchase anything.")
        case _:
            print("The merchant tells you to stop wasting his time and walks away spitting next to your foot.")

    

def get_random_encounter():
    choice = random.choices(
        population=list(ENCOUNTER_TYPES.keys()),
        weights=list(ENCOUNTER_TYPES.values()),
        k=1
    )[0]
    match choice:
        case "Innkeeper":
            innkeeper_encounter()

    return choice

for i in range(15):
    print(get_random_encounter())