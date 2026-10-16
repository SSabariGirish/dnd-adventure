import os

from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from entities.hero import Hero
from entities.enemy import Enemy
from core.enums import Species
from utils.display import show_status
from utils.monster_art import ASCII_ART

from enemies.templates import spawn_enemy

def clear_screen():
    input("\nPress Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

def enemy_turn(hero: Knight | Mage | Rogue, enemy: Enemy):
    enemy.attack(hero)
    clear_screen()

#Creating the Hero character
def create_hero() -> list:
    info_list = []

    print("===========================================")
    print("          Begin your Adventure!            ")
    print("===========================================")
    name = str(input("What is the name of your Hero?\n"))
    name = name.strip()
    info_list.append(name)
    print("===========================================")
    print(f"Which species does {name} belong to?")
    print("===========================================")
    print("1) HUMAN")
    print("2) ELF")
    print("3) DWARF")
    print("4) DEMON")
    species_choice = int(input("           Choose your species             \n"))

    match species_choice:
        case 1:
            info_list.append(Species.HUMAN)
        case 2:
            info_list.append(Species.ELF)
        case 3:
            info_list.append(Species.DWARF)
        case 4:
            info_list.append(Species.DEMON)
        case _:
            raise ValueError("Invalid Species Chosen")

    print("===========================================")
    print(f"Which class does {name} belong to?")
    print("===========================================")
    print("1) KNIGHT")
    print("2) ROGUE")
    print("3) MAGE") 
    class_choice = int(input("           Choose your class             \n"))

    match class_choice:
        case 1:
            info_list.append("Knight")
        case 2:
            info_list.append("Rogue")
        case 3:
            info_list.append("Mage")
        case _:
            raise ValueError("Invalid Class Chosen")         

    return info_list

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
    if isinstance(hero, Rogue):
        print(f"5) SWITCH STANCE - (current stance = {hero.get_stance()})")

    choice = int(input("Choose your action\n"))
    if isinstance(hero, Rogue):
        valid_choices = list(range(1, 6))
    else:
        valid_choices = list(range(1, 5))

    if choice not in valid_choices:
        raise ValueError("Invalid Option")

    return choice

def combat(hero: Knight | Mage | Rogue, enemy: Enemy):

    while hero.is_alive() and enemy.is_alive():
        current_status = show_status(hero)
        print(current_status)

        try:
            action_choice = get_player_action(hero)
            res = True

            match action_choice:
                case 1:
                    hero.attack(enemy)
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
                    if isinstance(hero, Rogue):
                        res = hero.switch_stance()
                    else:
                        raise ValueError("Invalid Option")

            if res and enemy.is_alive() and hero.is_alive():
                os.system("cls" if os.name == "nt" else "clear")
                enemy_turn(hero, enemy)

        except ValueError as v:
            print(v)
            input("\nPress Enter to try again...")
            os.system("cls" if os.name == "nt" else "clear")
    
        

def main():
    invalid = True
    while invalid:
        try:
            choices = create_hero()
            invalid = False
        except ValueError as v:
            print(v)
            clear_screen()

    match choices[2]:
        case 'Knight':
            hero = Knight(choices[1], choices[0])
        case 'Rogue':
            hero = Rogue(choices[1], choices[0])
        case 'Mage':
            hero = Mage(choices[1], choices[0])
    clear_screen()
    print(hero)
    clear_screen()
    spawn_now = True

    while hero.is_alive():
        
        if spawn_now:    
            cur_enemy = spawn_enemy(hero.level)
            spawn_now = False

            print(f"\nA {cur_enemy.get_name()} has stopped {hero.get_name()} in their path!\n\n")
            print(ASCII_ART[cur_enemy.get_name().lower()])
            print('\n')
            enemy_turn(hero, cur_enemy)
        
        combat(hero, cur_enemy)
        

        if not hero.is_alive():
            print(f"{hero.get_name()} has courageously fallen in battle and will not be forgotten")
            clear_screen()
        
        if not cur_enemy.is_alive():
            spawn_now = True
            print(f"\n{cur_enemy.get_name()} has been slain by {hero.get_name()}")
            hero.xp += cur_enemy.get_xp_reward()
            hero.verify_level_up()

            if cur_enemy.get_drop_reward() in hero.junk_inventory:
                hero.junk_inventory[cur_enemy.get_drop_reward()] += 1
            else:
                hero.junk_inventory[cur_enemy.get_drop_reward()] = 1    
            
            del cur_enemy

        clear_screen()

if __name__=="__main__":
    main()