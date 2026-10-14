from entities.knight import Knight
from entities.mage import Mage
from entities.rogue import Rogue
from entities.hero import Hero
from core.enums import Species

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


def main():
    choices = create_hero()
    print(choices)

if __name__=="__main__":
    main()