import random
import os

from entities.hero import Hero
from entities.enemy import Enemy
from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from enemies.templates import spawn_enemy, spawn_boss
from utils.monster_art import ASCII_ART, BOSS_ART
from utils.display import show_status, show_enemy_health
from utils.save_system import save_game
from adventure.quest import PeasantQuest
from core.armour import Armour
from core.weapons import Weapon

ENCOUNTER_TYPES = {
    "Innkeeper": 10,
    "Merchant": 10,
    "Huntsman": 10,
    "Blacksmith": 10,
    "Peasant": 15,
    "Enemy": 45
}

LIST_OF_ENEMIES = ["Goblin", "Gnoll", "Wolf", "Bandit", "Skeleton",
                   "Orc", "Dire Wolf", "Cultist", "Ogre", "Wraith",
                   "Troll", "Wyvern", "Griffin", "Archgriffin"]
JUNK_PRICES = {
    "Goblin Ear": 5,
    "Gnoll Fang": 7,
    "Wolf Pelt": 8,
    "Bandit Insignia": 12,
    "Bone Fragments": 10,
    "Orc Tusk": 18,
    "Dire Wolf Pelt": 22,
    "Bloody Robes": 25,
    "Ogre Hide": 35,
    "Wraith Essence": 45,
    "Troll Tongue": 55,
    "Enchanted Grimoire": 60,
    "Wyvern Scale": 100,
    "Griffin Feather": 175,
    "Archgriffin Talon": 300,
    "Goblin King's Crown": 120,
    "Champion's Blade": 250,
    "Warlord's Armour": 350,
    "Lich's Phylactery": 500,
    "Ancient Wyvern Heart": 750,
    "Fiend's Crest": 1000
}

def roll_check(stat: int, target: int) -> bool:
    dice_roll = random.randint(1, 20)
    full_stat = dice_roll + stat
    print(f"You needed {target}")
    print(f"You have rolled {full_stat}")
    if full_stat >= target:
        return True
    return False

def ask_about_rumours(hero: Hero):
    print("\nThe innkeeper lowers his voice.")
    print('"Strange things have been happening around these parts at night..."')
    print("\n1) Listen carefully to the local rumours")
    print("2) Pretend you are an envoy of the kingdom")

    choice = input("\nChoose your approach: ")

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

def show_quests(hero: Hero):
    print(f"A pint in hand and home cooked meal in front of them, {hero.get_name()} thinks of requests they've received from peasants.")
    print("\n========== CURRENT QUESTS ==========")
    if not hero.quests:
        print(f"{hero.get_name()} eats and drinks in peace, as to their knowledge, no village is being troubled by monsters.")
        return
    
    for quest in hero.quests:
        if quest.completed:
            continue

        print(f"\nTarget: {quest.monster_name}")
        print(f"Progress: {quest.current_kills}/{quest.required_kills}")
        print('\n')

    print("\n====================================")
        
def innkeeper_encounter(hero: Hero):
    print("\nYou enter a small tavern.")
    print("The innkeeper looks up from polishing a glass.")
    print('"Welcome, traveller!! What would you like to have?"')

    print("1) Ask about rumours")
    print("2) Spend the night at the inn")
    print("3) Leave town")
    print("4) Save Game")

    choice = input('\nMake a decision: ')
    match choice:
        case "1":
            ask_about_rumours(hero)
            show_quests(hero)
        case "2":
            if hero.gold < 25:
                print(f"{hero.get_name()} does not have enough Gold to rent a room")
            else:
                hero.gold -= 25
                print(f"\n{hero.get_name()} paid 25 Gold. Remaining Gold: {hero.gold}")
                print(f"{hero.get_name()} spends the night resting and recover some health and mana.")
                hero.heal(int(0.2 * hero.get_max_health()))
                hero.restore_mana(int(0.2 * hero.get_max_mana()))
            show_quests(hero)
        case "3":
            print(f"{hero.get_name()} finds no reason to visit the tavern and goes on their own way")
        case "4":
            save_game(hero)
            print(f"{hero.get_name()} has taken a sip of Saviour Schnapp")
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

    choice = input("\nMake a decision: ")

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

def blacksmith_encounter(hero: Hero):
    available_weapons = [
        weapon for weapon in Weapon
        if weapon.hero_class == hero.__class__.__name__
    ]

    available_armour = [
        armour for armour in Armour
        if armour.hero_class == hero.__class__.__name__
    ]

    print("\nYou feel a burst of heat as you enter a blacksmith's forge.")
    print('"Welcome, adventurer! Looking to upgrade your equipment?"')

    while True:
        print("\n========== BLACKSMITH ==========")
        print(f"Gold: {hero.gold}")
        print(f"Current weapon: {hero._weapon.display_name}")
        print(f"Current armour: {hero._armour.display_name}")
        print("\n1. Browse weapons")
        print("2. Browse armour")
        print("3. Leave")

        choice = input("What would you like to do? ").strip()

        if choice == "1":
            print("\n========== WEAPONS ==========")

            for index, weapon in enumerate(available_weapons, start=1):
                equipped = " (Equipped)" if weapon == hero._weapon else ""
                print(
                    f"{index}. {weapon.display_name} | "
                    f"Damage: {weapon.damage} | "
                    f"Price: {weapon.price} gold{equipped}"
                )

            print("0. Back")

            try:
                selection = int(input("Choose a weapon: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if selection == 0:
                continue

            if not 1 <= selection <= len(available_weapons):
                print("Invalid selection.")
                continue

            weapon = available_weapons[selection - 1]

            if weapon == hero._weapon:
                print("You already have this weapon equipped.")
                continue

            if weapon.damage <= hero._weapon.damage:
                print("That weapon isn't an upgrade over your current weapon.")
                continue

            if hero.gold < weapon.price:
                print("You don't have enough gold.")
                continue

            confirm = input(
                f"Buy {weapon.display_name} for {weapon.price} gold? (y/n): "
            ).strip().lower()

            if confirm == "y":
                hero.gold -= weapon.price
                hero._weapon = weapon
                print(f"You have purchased and equipped {weapon.display_name}!")
            else:
                print("Purchase cancelled.")

        elif choice == "2":
            print("\n========== ARMOUR ==========")

            for index, armour in enumerate(available_armour, start=1):
                equipped = " (Equipped)" if armour == hero._armour else ""
                print(
                    f"{index}. {armour.display_name} | "
                    f"Defence: {armour.defence} | "
                    f"Price: {armour.price} gold{equipped}"
                )

            print("0. Back")

            try:
                selection = int(input("Choose a piece of armour: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if selection == 0:
                continue

            if not 1 <= selection <= len(available_armour):
                print("Invalid selection.")
                continue

            armour = available_armour[selection - 1]

            if armour == hero._armour:
                print("You already have this armour equipped.")
                continue

            if armour.defence <= hero._armour.defence:
                print("That armour isn't an upgrade over your current armour.")
                continue

            if hero.gold < armour.price:
                print("You don't have enough gold.")
                continue

            confirm = input(
                f"Buy {armour.display_name} for {armour.price} gold? (y/n): "
            ).strip().lower()

            if confirm == "y":
                hero.gold -= armour.price
                hero._armour = armour
                print(f"You purchased and equipped {armour.display_name}!")
            else:
                print("Purchase cancelled.")

        elif choice == "3":
            print("The blacksmith thanks you for your time and mutters a soft prayer on your behalf")
            print('"May your blade stay sharp and your armour hold firm!"')
            break

        else:
            print("The blacksmith thinks you have gone crazy and shows you the way out of his forge")
            break

def sell_junk(hero: Hero, price_mul: float):
    if not hero.junk_inventory:
        print("\nYou have no monster trophies to sell.")
        return

    total_value = 0

    print("\nThe huntsman examines your trophies:")

    for item, quantity in hero.junk_inventory.items():
        base_price = JUNK_PRICES.get(item, 0)
        item_price = round(base_price * price_mul)
        subtotal = item_price * quantity

        print(f"{item} x{quantity} - {subtotal} Gold")
        total_value += subtotal

    if total_value == 0:
        print("\nThe huntsman finds nothing worth buying.")
        return

    print(f"\nTotal payment: {total_value} Gold")
    hero.gold += total_value
    hero.junk_inventory.clear()

    print(f"You receive {total_value} Gold!")
    print(f"Remaining Gold: {hero.gold}")

def huntsman_encounter(hero: Hero):
    print("\nYou meet a huntsman who buys monster trophies.")
    print('"Anything worth selling, traveller?"')

    print("\n1) Negotiate (INT Check)")
    print("2) Bluff (DEC Check)")
    print("3) Sell at the listed price")
    print("4) Leave")

    choice = input("\nMake a decision: ")

    match choice:
        case "1":
            if roll_check(hero.intelligence, 15):
                print("\nThe huntsman nods, impressed by your knowledge of monster trophies.")
                print("He agrees to pay you a little above the usual price acknowledging the difficulty.")
                sell_junk(hero, 1.25)
            else:
                print("\nThe huntsman catches a flaw in your valuation and turns the tables.")
                print("He offers you only 3/4th of the usual price.")
                sell_junk(hero, 0.75)

        case "2":
            if roll_check(hero.deception, 18):
                print("\nThe huntsman falls for your outrageous claims about the rarity of your trophies.")
                print("He pays you DOUBLE their usual value!")
                sell_junk(hero, 2.0)
            else:
                print("\nThe huntsman sees straight through your lies and snarls.")
                print("He hurls a poisoned dart at you!")
                print("You take 20 true damage, and your armour deteriorates permanently.")
                hero.cur_health -= 20
                hero.deteriorate_armour(1)

        case "3":
            print("\nThe huntsman inspects your trophies and offers you their standard value.")
            sell_junk(hero, 1.0)

        case "4":
            print("\nYou decide to keep your trophies and move on.")

        case _:
            print("\nThe huntsman dismisses you as a madman and leaves, muttering a prayer to himself.")

def boss_encounter(hero: Hero, boss_level: int) -> bool:
    boss = spawn_boss(boss_level)

    boss_art = BOSS_ART.get(boss.get_name().lower())

    if boss_art:
        print(boss_art + "\n")

    while hero.is_alive() and boss.is_alive():
        combat(hero, boss)
    
    if not hero.is_alive():
        print(f"\n{hero.get_name()} has fallen before {boss.get_name()}!")
        return False
    
    print(f"\n{boss.get_name()} has been defeated!")
    print(f"{hero.get_name()} earned {boss.get_xp_reward()} XP!")

    hero.xp += boss.get_xp_reward()
    drop = boss.get_drop_reward()

    if drop:
        hero.junk_inventory[drop] = hero.junk_inventory.get(drop, 0) + 1
        print(f"You obtained: {drop}")

    return True

def clear_screen():
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

def enemy_turn(hero: Knight | Mage | Rogue, enemy: Enemy):
    enemy.attack(hero)
    clear_screen()

def combat(hero: Knight | Mage | Rogue, enemy: Enemy):

    while hero.is_alive() and enemy.is_alive():
        current_status = show_status(hero)
        print(current_status)
        show_enemy_health(enemy)

        try:
            action_choice = get_player_action(hero)
            res = True

            match action_choice:
                case 1:
                    res = hero.attack(enemy)
                case 2:
                    if isinstance(hero, Knight):
                        res = hero.raise_shield()
                    elif isinstance(hero, Mage):
                        res = hero.cast_spell(enemy)
                    elif isinstance(hero, Rogue):
                        res = hero.raise_evasion()
                case 3:
                    res = hero.consume_healing_potion()
                case 4:
                    res = hero.consume_mana_potion()
                case 5:
                    res = hero.get_inventory()
                case 6:
                    if isinstance(hero, Rogue):
                        res = hero.switch_stance()
                    else:
                        raise ValueError("Invalid Option")

            if res and enemy.is_alive() and hero.is_alive():
                clear_screen()
                enemy_turn(hero, enemy)

        except ValueError as v:
            print(v)
            input("\nPress Enter to try again...")
            os.system("cls" if os.name == "nt" else "clear")

def get_player_action(hero: Knight | Mage | Rogue) -> int:
    print("===========================================")
    print("         What are you Going to Do?         ")
    print("===========================================")
    print("1) ATTACK")
    if isinstance(hero, Knight):
        print("2) RAISE HOLY SHIELD")
    elif isinstance(hero, Mage):
        print("2) CAST SPELL")
    else:
        print("2) RAISE EVASION")
    print("3) CONSUME HEALTH ELIXIR")
    print("4) CONSUME MANA ELIXIR")
    print("5) SEE INVENTORY")
    if isinstance(hero, Rogue):
        print(f"6) SWITCH STANCE - (current stance = {hero._stance})")

    choice = int(input("Choose your action\n"))
    if isinstance(hero, Rogue):
        valid_choices = list(range(1, 7))
    else:
        valid_choices = list(range(1, 6))

    if choice not in valid_choices:
        raise ValueError("Invalid Option")

    return choice

def enemy_encounter(hero: Hero):
    cur_enemy = spawn_enemy(hero.level)
    print(f"\nA {cur_enemy.get_name()} has stopped {hero.get_name()} in their path!\n\n")
    print(ASCII_ART[cur_enemy.get_name().lower()])
    print('\n')
    enemy_turn(hero, cur_enemy)

    while hero.is_alive() and cur_enemy.is_alive(): 
        combat(hero, cur_enemy)

    if not hero.is_alive():
        return
            
    print(f"\n{cur_enemy.get_name()} has been slain by {hero.get_name()}")
    hero.xp += cur_enemy.get_xp_reward()
    for quest in hero.quests:
        ans = quest.record_kill(cur_enemy.get_name())
        if ans:
            print(f"{hero.get_name()} has completed a citizen's quest")
            print(f"The village sends prayers in your name, promising to never forget your valour")
            print(f"You have earned {quest.xp_reward} XP and {quest.gold_reward} Gold\n")
            hero.xp += quest.xp_reward
            hero.gold += quest.gold_reward
            del quest
            break
    hero.verify_level_up()
    
    if cur_enemy.get_drop_reward() in hero.junk_inventory:
        hero.junk_inventory[cur_enemy.get_drop_reward()] += 1
    else:
        hero.junk_inventory[cur_enemy.get_drop_reward()] = 1    
                
    del cur_enemy

def peasant_encounter(hero: Hero):
    print("\nA worried peasant approaches you.")
    print('"Please, traveller! Monsters are terrorising our village!"')
    print('"Will you help us?"')

    print("\n1) Accept the quest")
    print("2) Decline")

    choice = input("Make a decision: ")

    match choice:
        case "1":
            print("\nThe peasant explains the situation.")
            num_enemies = random.randint(1, 5)
            enemy_choice = LIST_OF_ENEMIES[random.randint(0, len(LIST_OF_ENEMIES) - 1)]
            new_quest = PeasantQuest(enemy_choice, num_enemies, 250, 100)
            print(f"The village asks you to hunt {num_enemies} {enemy_choice}(s)")
            print(f"They pool their assets together to grant you 250 XP and 100 Gold if you complete the quest")
            hero.quests.append(new_quest)

        case "2":
            print("\nYou apologise and continue on your journey.")

        case _:
            print("\nThe peasant looks confused, mutters a prayer for your lost soul and walks away.")

def get_random_encounter(hero: Hero) -> str:

    choice = random.choices(
        population=list(ENCOUNTER_TYPES.keys()),
        weights=list(ENCOUNTER_TYPES.values()),
        k=1
    )[0]

    return choice
