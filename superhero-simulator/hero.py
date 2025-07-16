# Lab 6 - Sydney Ly

import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def battle(self, opponent):
        '''Print a random winner.'''
        winner = random.choice([self.name, opponent.name])
        print(f"{winner} has won the battle!")
    
    def add_ability(self, ability):
        '''Adds an ability to the existing abilities list.'''
        self.abilities.append(ability)
        print(f"{ability.name} has been added to {self.name}'s ability list!")
    
    def sum_of_attacks(self):
        '''Loops through abilities list and sums up all attack damage.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Adds an armor to the armors list.'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s ability list!")

    def defend(self):
        '''Loops through armors list and sums up all block values.'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("Superman", 500)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200
    my_hero.battle(my_hero2)
    fireball = Ability("Fireball", 50)
    lightning = Ability("Lightning", 55)
    telekinesis = Ability("Telekinesis", 60)
    my_hero.add_ability(fireball)
    my_hero.add_ability(lightning)
    my_hero.add_ability(telekinesis)
    print(my_hero.sum_of_attacks())
    shield = Armor("Shield", 30)
    helmet = Armor("Helmet", 25)
    boots = Armor("Boots", 10)
    my_hero.add_armor(shield)
    my_hero.add_armor(helmet)
    my_hero.add_armor(boots)
    print(my_hero.defend())