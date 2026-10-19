class PeasantQuest:

    def __init__(self, monster_name: str, required_kills: int, xp_reward: int, gold_reward: int):
        self.monster_name = monster_name
        self.required_kills = required_kills
        self.current_kills = 0
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.completed = False

    def record_kill(self, enemy_name: str) -> bool:
        if self.completed:
            return False

        if self.monster_name.lower() == enemy_name.lower():
            self.current_kills += 1

        if self.current_kills == self.required_kills:
            self.completed = True
            return True

        return False