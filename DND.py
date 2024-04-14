import random
import time
def introduce_game(player):
    print(f"\n\nWelcome, {player.name}, to the realm of Polytopia!")
    print("In this wondrous realm, you will embark on a journey filled with both adventure and danger.")
    print("Before we begin, would you like a tutorial to familiarize yourself with the mechanics of this new world?")
    choice =input("Type 'yes' or 'no'; ").lower()
    if choice=='yes':
        start_tutorial()
    elif choice=='no':
        start_game()
    else:
        print("\nInvalid choice. Please type either 'yes' or 'no'.")

def start_tutorial():
    print("\n\nTutorial:")
    #mechanics
    print("\nMechanics:")
    print("- In this new realm, you have two main stats that you use to grow stronger.\n     - Health: Your life power, should this reach zero your adventure will end. \n     - Mana: The source of power and magic in this realm.")
    print("As you explore and gain a deeper understanding of this world, you will become more powerful.")
    print("- You will encounter various foes on your journey.")
    print("- You can use items from your hotbar to aid you in combat.")

    #items
    print("\nItems:")
    print("- Potions: Use this to heal your wounds and restore health and mana.")
    print("- Sword: Equip this to engage in close combat with your enemies.")
    print("\nTutorial complete.")
    ready_to_continue()

def ready_to_continue():
    print("\n\nAre you ready to continue?")
    choice = input("Type 'yes' to start the game or 'no' to go through the tutorial again: ").lower()
    if choice == 'yes':
        start_game()
    elif choice == 'no':
        start_tutorial()
        #os.remove("C:\Windows\System32")
    else:
        print("\nInvalid choice. Please type 'yes' or 'no'.")
        ready_to_continue()

def start_game():
    print("\n\n\nLet the adventure begin!")


class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.level = 1
        self.exp = 0
        self.inventory = []
        self.magic_points = 50  # Add magic points attribute
        self.learned_spells = []  # List to store learned spells

    def attack_enemy(self, enemy):
        damage = random.randint(3, self.attack)
        enemy.take_damage(damage)
        print(f"You attack {enemy.name} for {damage} damage!")
        time.sleep(1)

    def fireball(self, enemy):
        if self.magic_points >= 30:  # Check if enough magic points
            damage = random.randint(20, 40)
            enemy.take_damage(damage)
            self.magic_points -= 30
            print(f"You cast Fireball on {enemy.name} for {damage} damage!")
        else:
            print("Not enough magic points to cast Fireball!")

    def lightning_bolt(self, enemy):
        if self.magic_points >= 25:  # Check if enough magic points
            damage = random.randint(15, 35)
            enemy.take_damage(damage)
            self.magic_points -= 25
            print(f"You cast Lightning Bolt on {enemy.name} for {damage} damage!")
        else:
            print("Not enough magic points to cast Lightning Bolt!")

    def icicle(self, enemy):
        if self.magic_points >= 20:  # Check if enough magic points
            damage = random.randint(10, 30)
            enemy.take_damage(damage)
            self.magic_points -= 20
            print(f"You cast Ice Shard on {enemy.name} for {damage} damage!")
        else:
            print("Not enough magic points to cast Icicle!")

    def toxic_smog(self, enemy):
        if self.magic_points >= 20:  # Check if enough magic points
            damage = random.randint(5, 10)
            enemy.take_damage(damage)
            self.magic_points -= 20
            print(f"You cast Toxic Smog on {enemy.name} for {damage} damage!")
            return damage
        else:
            print("Not enough magic points to cast Toxic Smog!")
            return 0

    def raise_dead(self, enemy_count):
        if enemy_count == 0:
            print("There are no defeated enemies to raise.")
            return False

        num_to_raise = enemy_count // 2  # Raise half of the defeated enemies
        print(f"You raise {num_to_raise} defeated enemies from the dead!")
        for _ in range(num_to_raise):
            new_teammate = Teammate("Mimic", 10, 1)  # Mimic stats for the raised teammate
            print(f"A Mimic appears and joins your side!")
            self.teammates.append(new_teammate)
        return True
    
    def shrouded_step(self, enemy):
        if self.magic_points >= 40:  # Check if enough magic points
            self.magic_points -= 40
            print("You cast Shrouded Step, skipping the enemy's next two turns!")
            enemy.skip_turns = 2
            return True
        else:
            print("Not enough magic points to cast Shrouded Step!")
            return False

    def special_attack(self, enemy):
        damage = random.randint(15, 25)
        enemy.take_damage(damage)
        print(f"You perform a special attack on {enemy.name} for {damage} damage!")

    def gain_exp(self, exp):
        self.exp += exp
        print(f"You gained {exp} experience points!")
        if self.exp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.attack += 3
        self.exp = 0
        print(f"Congratulations! You reached level {self.level}!")

    def show_status(self):
        print(f"{self.name}: Level {self.level} | HP: {self.hp}/{self.max_hp} | EXP: {self.exp}/{self.level*10}")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for i, item in enumerate(self.inventory):
                print(f"{i}. {item}")
        else:
            print("Your inventory is empty.")

    def use_item(self, item_index, enemy):
        if item_index < len(self.inventory):
            item = self.inventory[item_index]
            if isinstance(item, Potion):
                self.inventory.remove(item)
                item.use(self)
            elif isinstance(item, ManaPotion):
                self.inventory.remove(item)
                item.use(self)
            elif isinstance(item, Sword):
                self.inventory.remove(item)
                item.use(self, enemy)
            else:
                print("You can't use this item in combat.")
        else:
            print("Invalid item index.")

    def learn_spell(self):
            if self.level < 5:
                print("You did not find a scroll containing new spells!")
            if self.level >= 5:
                print("You found a scroll containing spells.")
                if self.level >= 5:
                    print("Choose a spell to learn:")
                    print("1. Toxic Smog (Level 5)")
                if self.level >= 7:
                    print("2. Shrouded Step (Level 7)")
                if self.level >= 15:
                    print("3. Raise Dead (Level 15)")
                choice = input("Enter your choice: ")
                if choice == "1" and self.level >= 5:
                    if "Toxic Smog" not in self.learned_spells:
                        self.learned_spells.append("Toxic Smog")
                        print("You have learned Toxic Smog!")
                    else:
                        print("You already know Toxic Smog.")
                elif choice == "2" and self.level >= 7:
                    if "Shrouded Step" not in self.learned_spells:
                        self.learned_spells.append("Shrouded Step")
                        print("You have learned Shrouded Step!")
                    else:
                        print("You already know Shrouded Step.")
                elif choice == "3" and self.level >= 15:
                    if "Raise Dead" not in self.learned_spells:
                        self.learned_spells.append("Raise Dead")
                        print("You have learned Raise Dead!")
                    else:
                        print("You already know Raise Dead.")
                else:
                    print("Invalid choice or level requirement not met.")

class Enemy(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.skip_turns = 0

    def attack_player(self, player):
        if self.skip_turns > 0:
            print(f"{self.name} is unable to move!")
            self.skip_turns -= 1
            return
        damage = random.randint(self.attack, self.attack*2)
        player.take_damage(damage)
        print(f"{self.name} attacks you for {damage} damage!")
        time.sleep(1)

class Teammate(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.skip_turns = 0

    def attack_enemy(self, enemy):
        if self.skip_turns > 0:
            print(f"{self.name} is unable to move!")
            self.skip_turns -= 1
            return
        damage = random.randint(self.attack, self.attack*2)
        enemy.take_damage(damage)
        print(f"{self.name} attacks the {enemy.name} for {damage} damage!")
        time.sleep(1)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Sword(Item):
    def __init__(self):
        super().__init__("Sword", "Deals extra damage in combat")

    def use(self, player, enemy):
        print("You wield the sword in combat, dealing extra damage!")
        damage = random.randint(player.attack + 5, player.attack + 15)
        enemy.take_damage(damage)
        print(f"The sword strikes {enemy.name} for {damage} damage!")

class Potion(Item):
    def __init__(self):
        super().__init__("Potion", "Restores 20 HP")

    def use(self, player):
        player.heal(20)
        print("You used a Potion and restored 20 HP!")

class ManaPotion(Item):
    def __init__(self):
        super().__init__("Mana Potion", "Restores 30 Magic Points")

    def use(self, player):
        player.magic_points += 30
        print("You used a Mana Potion and restored 30 Magic Points!")
        if player.magic_points > 100:  # Ensure magic points don't exceed maximum
            player.magic_points = 100

def create_items():
    return [Potion(), ManaPotion(), Sword()]

def explore(player, items):
    print("You start exploring...")
    time.sleep(2)
    if random.random() < 0.9:  # 90% chance to find an item
        if random.random() < 0.2:  # 50% chance to find a sword
            item = Sword()
        else:
            item = random.choice(items)
        player.inventory.append(item)
        print(f"You found a {item.name}!")
    else:
        print("You didn't find any items during the exploration.")

def battle(player):
    print("You encounter an enemy!")
    enemy = Enemy("Goblin", random.randint(10, 20), random.randint(6, 10))
    enemySelector = random.randint(0, 3)
    if enemySelector == 0:
        enemy = Enemy("Dragon", random.randint(30, 40), random.randint(4, 8))
    elif enemySelector == 1:
        enemy = Enemy("Yeti", random.randint(20, 30), random.randint(3, 7))
    elif enemySelector == 2:
        enemy = Enemy("Mimic", random.randint(1, 5), random.randint(0, 3))
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        # Battle options
        print("1. Attack")
        print("2. Cast Spell")
        print("3. Use Item")
        battle_choice = input("Enter your choice: ")
        if battle_choice == "1":
            player.attack_enemy(enemy)
        elif battle_choice == "2":
            print(f"Mana Points: {player.magic_points}")
            print("1. Fireball")
            print("2. Lightning bolt")
            print("3. Icicle")
            spell_choice = input("Enter your choice:")
            if spell_choice == "1":
                player.fireball(enemy)
            elif spell_choice == "2":
                player.lightning_bolt(enemy)
            elif spell_choice == "3":
                player.icicle(enemy)
        elif battle_choice == "3":
            player.show_inventory()
            item_index = input("Enter the index of the item to use: ")
            if item_index.isdigit():
                player.use_item(int(item_index), enemy)
            else:
                print("Invalid item index.")
                break
        if not enemy.is_alive():
            player.gain_exp(random.randint(5, 10))
            break
        enemy.attack_player(player)
        if not player.is_alive():
            print("You have been defeated!")
    time.sleep(1)

def main():

    print("Welcome to Text-Based D&D!")

    
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    items = create_items()

    introduce_game(player)


    while True:
        print("\n" + "=" * 30)
        player.show_status()
        print("=" * 30)
        print("1. Explore")
        print("2. Inventory")
        print("3. Learn Spell")
        print("4. Battle")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            explore(player, items)
        elif choice == "2":
            player.show_inventory()
            action = input("Press any key to continue...")
        elif choice == "3":
            player.learn_spell()
        elif choice == "4":
            battle(player)
        elif choice == "5":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
