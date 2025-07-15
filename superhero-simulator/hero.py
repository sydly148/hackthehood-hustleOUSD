# Lab 6 - Sydney Ly

import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []

    def battle(self, opponent):
        '''Fight another hero and randomly choose a winner.'''
        winner = random.choice([self.name, opponent.name])
        print(f"The winner of this battle is {winner}!")
    
    def add_ability(self, ability):
        '''Appends an ability to a hero's list of abilities.'''
        self.abilities.append(ability)
        print(f"{ability.name} has been added to the list of abilities.")
    
    def sum_of_attacks(self):
        '''Iterates through entire list of abilities and sums up their attack values.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        '''Appends an armor to a hero's list of armors.'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to the list of armors.")
    
    def defend(self):
        '''Iterates through entire list of armors and sums up their total block.'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block 




if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("Spider-Man", 300)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
    ability1 = Ability("Explosion", 300)
    ability2 = Ability("Electrocution", 150)
    ability3 = Ability("Web shooter", 50)
    ability4 = Ability("Punch", 15)
    my_hero.add_ability(ability1)
    my_hero.add_ability(ability4)
    my_hero2.add_ability(ability2)
    my_hero2.add_ability(ability3)
    print(my_hero.abilities)
    print(my_hero2.abilities)

