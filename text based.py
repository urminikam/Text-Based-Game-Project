import random

# Character class
class Character:
    def _init_(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage <= 0:
            damage = 1
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

# Enemy class
class Enemy:
    def _init_(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage <= 0:
            damage = 1
        player.take_damage(damage)
        print(f"{self.name} attacks {player} for {damage} damage.")

# Game functions
def create_character():
    name = input("Enter your character's name: ")
    player = Character(name, 100, 10, 5)
    return player

def encounter_enemy(player):
    enemy_types = ["Goblin", "Orc", "Skeleton"]
    enemy_type = random.choice(enemy_types)
    if enemy_type == "Goblin":
        enemy = Enemy("Goblin", 50, 8, 2)
    elif enemy_type == "Orc":
        enemy = Enemy("Orc", 75, 12, 4)
    elif enemy_type == "Skeleton":
        enemy = Enemy("Skeleton", 60, 10, 3)

    print(f"You encountered a {enemy_type}!")
    while player.health > 0 and enemy.health > 0:
        print("1. Attack")
        print("2. Run")
        choice = input("Choose an action: ")
        if choice == "1":
            player.attack_enemy(enemy)
            if enemy.health > 0:
                enemy.attack_player(player)
        elif choice == "2":
            run_chance = random.randint(1, 3)
            if run_chance == 1:
                print("You successfully escaped!")
                break
            else:
                print("You couldn't escape!")
                enemy.attack_player(player)

def main():
    player = create_character()
    print(f"Welcome, {player.name}!")

    while player.health > 0:
        print("\nWhat do you want to do?")
        print("1. Explore")
        print("2. Check inventory")
        choice = input("Choose an action: ")
        if choice == "1":
            encounter_chance = random.randint(1, 3)
            if encounter_chance == 1:
                encounter_enemy(player)
            else:
                print("You explore the area but find nothing.")
        elif choice == "2":
            print(f"Inventory: {player.inventory}")

    print("Game over!")

