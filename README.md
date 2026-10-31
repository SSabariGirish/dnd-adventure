# DnD Adventure

A Python-based, command-line Dungeons & Dragons-inspired RPG where you create a hero, explore a fantasy world, fight monsters, complete quests, collect loot, and grow stronger.

Choose your class, develop your character, encounter unpredictable challenges, and see how far you can survive.

## Features

### Character Creation
- Choose between three playable classes:
  - **Knight** – A durable warrior specialising in physical combat and defence.
  - **Mage** – A spellcaster who uses mana to unleash powerful attacks.
  - **Rogue** – An agile fighter who uses evasion and different combat stances.
- Select your character's species, each with its own starting attributes.
- Character attributes improve as you level up.

### Combat System
- Turn-based combat against a variety of enemies.
- Class-specific abilities and mechanics.
- Health and mana management.
- Healing and mana restoration potions.
- Enemy health bars to help assess combat situations.
- Different weapons and armour with unique damage and defence values.

### Exploration & Encounters
Encounter different characters and situations throughout your adventure:
- **Innkeeper** – Visit the inn and manage your adventure.
- **Merchant** – Purchase useful items.
- **Blacksmith** – Upgrade your equipment.
- **Huntsman** – Interact with the local hunter.
- **Peasant** – Accept quests and earn rewards.
- **Enemies** – Fight monsters and collect their drops.

### Quests & Progression
- Accept quests from villagers.
- Complete monster-hunting objectives.
- Track quest progress.
- Earn XP and gold for completing quests.
- Gain experience and level up your character.

### Inventory & Equipment
- Collect monster drops and other loot.
- Manage healing and mana potions.
- Purchase weapons and armour.
- Upgrade your character's equipment.

### Save & Load
- Save your character's progress at inns.
- Load an existing adventure.
- JSON-based save system.
- Preserve character attributes, equipment, inventory, quest progress, and game progression.

### Dynamic World
- AI-assisted town lore generation using OpenRouter.
- Randomised encounters to make each adventure less predictable.

---

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Core game implementation |
| Object-Oriented Programming | Character classes, enemies and game entities |
| JSON | Save and load system |
| OpenRouter API | AI-assisted town lore generation |
| python-dotenv | Environment variable management |

## Project Structure

```text
dnd-adventure/
│
├── adventure/
│   ├── encounters.py
│   └── quest.py
│
├── core/
│   ├── armour.py
│   ├── enums.py
│   ├── stats.py
│   └── weapons.py
│
├── enemies/
│   ├── abilities.py
│   └── templates.py
│
├── entities/
│   ├── enemy.py
│   ├── hero.py
│   ├── knight.py
│   ├── mage.py
│   └── rogue.py
│
├── utils/
│   ├── display.py
│   ├── monster_art.py
│   └── save_system.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

*Note: The structure above represents the main project modules; adjust filenames if your local repository differs.*

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or later.
- An OpenRouter API key for AI-generated town lore.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/SSabariGirish/dnd-adventure.git
```

2. Navigate to the project directory:

```bash
cd dnd-adventure
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows (Git Bash):

```bash
source venv/Scripts/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```
### Configuration

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace the placeholder with your OpenRouter API key.

### Running the Game

```bash
python main.py
```

Choose between starting a new adventure, loading an existing save, or exiting.

---

## Save System

The game uses JSON to persist character progress.

Save files preserve:
- Character identity and class.
- Level, experience and gold.
- Health, mana and attributes.
- Weapons and armour.
- Potions and collected loot.
- Quest progress.
- Game completion state.

Saving is available when visiting an inn.

---

## Future Improvements

Some ideas for expanding the adventure:

- More enemy types and boss-specific abilities.
- Additional quests and branching storylines.
- More weapons, armour and consumables.
- Expanded exploration and town interactions.
- More sophisticated combat mechanics.
- Multiple save slots.

---

## Author

**Sabari Girish**

GitHub: [@SSabariGirish](https://github.com/SSabariGirish)

---

*Built with Python, a little imagination, and an unhealthy number of hours in the Witcher series.*