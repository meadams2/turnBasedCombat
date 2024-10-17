"""Marianne Adams
10/18/2024
CS120 Turn Based Combat Module
Defines Character class and fight function"""
import random

def main():
    hero = Character("Hero", 10, 50, 5, 2)
    villain = Character("Villain", 10, 10, 5, 0)
#     hero = Character()
#     hero.name = "Hero"
#     hero.hitPoints = 10
#     hero.hitChance = 50
#     hero.maxDamage = 5
#     hero.armor = 2
#     hero = (hero.name, hero.hitPoints, hero.hitChance, hero.maxDamage, hero.armor)
    hero.printStats()
    villain.printStats()
    #villain.hit(hero)
    #hero.hit(villain)
#     fight(hero, villain)
    
class Character(object):
    def __init__(self, name = "Dan the Magical Cheese Wizard", hitPoints = 10, hitChance = 50, maxDamage = 5, armor = 0):
        super().__init__()
        self.name = name
        self.maxDamage = maxDamage
        self.hitChance = hitChance
        self.hitPoints = hitPoints
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
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
        return self.__maxDamage
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value)==int:
            self.__hitPoints = value
        return self.__hitPoints
            
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = testInt(self, value, 0, 100, 0)
        return self.__hitChance
            
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = testInt(self, value, 0, 1000, 0)
        return self.__armor
    
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
        return out
        
    def printStats(self):
        print(f"""{self.name}
HP: {self.hitPoints}
Hit Chance: {self.hitChance}
Max Damage: {self.maxDamage}
Armor: {self.armor}""")
          
    def hit(self, enemy):
        if random.randrange(1,100) <= self.hitChance:
            hitDamage = random.randrange(1, self.maxDamage)
            print(f"{self.name} hits {enemy.name} for {hitDamage} damage")
            print(f"{enemy.name}'s armor absorbs {enemy.armor} points")
            hitDamage -= enemy.armor
            if hitDamage < 0:
                hitDamage = 0
            enemy.hitPoints -= hitDamage
            print(f"{enemy.name}: {enemy.hitPoints}")
        else:
            hitDamage = 0
            print(f"{self.name} misses. No damage.")
        
        return enemy.hitPoints

    
# def fight(character1, character2):
#     
#     
#     keepGoing = True
#     while keepGoing:
#         if character1.hitPoints <= 0:
#             print(f"""{newHitPoints}
#                   {character1} dies.""")
#             keepGoing = False
#         else:
#             Character.hit(self)
#             print(f"{newHitPoints}")
    
main()
    
            
        
        
        