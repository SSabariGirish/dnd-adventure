from entities.hero import Hero
from entities.enemy import Enemy

def display_bar(current: int, maximum: int, width: int = 20) -> str:

    if maximum <= 0:
        return ""
    else:
        filled = int((current / maximum) * width)

    empty = width - filled
    bar = "█" * filled + "░" * empty
    return bar


def show_enemy_health(enemy: Enemy):
    bar_length = 25

    current_hp = enemy._cur_health
    max_hp = enemy.get_max_health()

    hp_bar = display_bar(current_hp, max_hp, bar_length)
    print(f"\n{enemy.get_name()}")
    print(f"HP: [{hp_bar}] {current_hp}/{max_hp}")

def show_status(hero: Hero) -> str:
    return f"""
===========================================
              CHARACTER SHEET
===========================================
    Name:           {hero.get_name().upper()}
    Class:          {type(hero).__name__.upper()}    

    Current Level:  {hero.level}
    To Next Level:  {hero.get_next_level_xp(hero.level) - hero.xp} XP


HEALTH & MANA\n
    Current Health: {hero.cur_health} / {hero.get_max_health()}\n  
                    {display_bar(hero.cur_health, hero.get_max_health())}\n\n
    Current Mana:   {hero.cur_mana} / {hero.get_max_mana()}\n
                    {display_bar(hero.cur_mana, hero.get_max_mana())}   
        
    """

