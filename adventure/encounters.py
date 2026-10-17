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
        if roll_check(hero.intelligence):
            print("\nYou piece together useful information!")
            hero.attack_modifier = 1.15
        else:
            print("\nThe rumours reveal nothing particularly useful.")

    elif choice == "2":
        if roll_check(hero.deception):
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

def merchant_encounter(hero: Hero):
    pass


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