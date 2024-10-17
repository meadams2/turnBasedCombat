"""Marianne Adams
10/18/2024
CS120 Turn Based Combat Module
Defines Character class and fight function"""
import random
def __main__():
    hero = Character("Hero", 10, 50, 5, 2)
    villain = Character("Villain", 10, 10, 5, 0)
#     hero = Character()
#     hero.name = "Hero"
#     hero.hitPoints = 10
#     hero.hitChance = 50
#     hero.maxDamage = 5
#     hero.armor = 2
#     hero = (hero.name, hero.hitPoints, hero.hitChance, hero.maxDamage, hero.armor)
    Character.printStats(hero)
    Character.printStats(villain)
    Character.hit(hero)
    Character.hit(villain)
    fight(hero, villain)
    
class Character(object):
    def __init__(self, name = "Dan the Magical Cheese Wizard", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 0):
        super().__init__()
        self.__name = name
        self.__maxDamage = maxDamage
        self.__hitChance = hitChance
        self.__hitPoints = hitPoints
        self.__armor = armor
        
    @property
    def characterName(self):
        return self.__name
    
 
    def name(self, value):
        self.__name = value
        
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if value == int:
            if value >= 0:
                self.__maxDamage = value
            else:
                print ("Maximum Damage must be positive.")
                self.__maxDamage = 1
        else:
            print("Maximum damage must be a number.")
            self.__maxDamage = 1
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if value == int:
            self.__hitPoints = value
        else:
            print("Hit Points must be a number.")
            self.__hitPoints = 10
            
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        if value == int:
            if value >= 0:
                if value <= 100:
                    self.__hitChance = value
                else:
                    print("Hit Chance must be less than 100.")
                    self.__hitChance = 100
            else:
                print("Hit Chance must be positive. Hit Chance is now 1")
                self.__hitChance = 1
        else:
            print("Hit Chance must be a number. Hit Chance is now 1")
            self.hitChance = 1
            
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if value == int:
            if value >= 0:
                self.__armor = value
            else:
                print("Armor must be positive.")
                self.__armor = 0
        else:
            print("Armor must be a number.")
            self.__armor = 0
        
    def printStats(self):
        print(f"""{self.__name}
HP: {self.__hitPoints}
Hit Chance: {self.__hitChance}
Max Damage: {self.__maxDamage}
Armor: {self.__armor}""")
          
    def hit(self):
        hitPerc = random.randrange(1, 100)
        if hitPerc <= self.__hitChance:
            hitDamage = random.randrange(1, self.__maxDamage)
            print(f"{self.__name} hits for {hitDamage} damage")
        else:
            hitDamage = 0
            print(f"{self.__name} misses. No damage.")

    
def fight(character1, character2):
    character1.hitDamage = Character.hit(character1)
    character2.hitDamage = Character.hit(character2)
    keepGoing = True
    while keepGoing:
        if newHitPoints <= 0:
            print(f"""{newHitPoints}
                  {character1} dies.""")
            keepGoing = False
        else:
            Character.hit(self)
            print(f"{newHitPoints}")
    
__main__()
    
            
        
        
        