from entities.hero import Hero

def display_bar(current: int, maximum: int, width: int = 20) -> str:

    if maximum <= 0:
        return ""
    else:
        filled = int((current / maximum) * width)

    empty = width - filled
    bar = "█" * filled + "░" * empty
    return bar

def show_status(hero: Hero) -> str:
    return f"""
    ===========================================
                  CHARACTER SHEET
    ===========================================
        Name:           {hero.get_name().upper()}
        Class:          {type(hero).__name__.upper()}    

    HEALTH & MANA
        Current Health:  {display_bar(hero.cur_health, hero.get_max_health())}\n
        Current Mana:    {display_bar(hero.cur_mana, hero.get_max_mana())}   
        
    """
