# This will be a code displaying all the attributes of a pokemon
# the attributes will be attack, hp, defense, and their 4 seperate abilities which will be given in the other program
# we will also introduce a crit chance and a dodge chance, and life steal for the pokemons

from random import randint



class Pokemon:
    def __init__(self, attack, health_point, defense, crit_chance, dodge_chance):
        self.attack = attack
        self.health_point = health_point
        self.defense = defense
        self.crit_chance = crit_chance
        self.dodge_chance = dodge_chance

    def successful_crit_check(self, damage):
        has_critted = False
        if self.crit_chance >= randint(0, 99):
            damage = damage * 2
            has_critted = True
        return damage, has_critted

    def successful_dodge_check(self, damage):
        has_dodged = False
        if self.dodge_chance >= randint(0, 99):
            damage = damage * 0
            has_dodged = True
        return damage, has_dodged

    def damage_dealt(self, damage):
        damage = damage - self.defense   
        return damage                        


