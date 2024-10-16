"""Marianne Adams
10/18/2024
CS120 Turn Based Combat Module
Defines Character class and fight function"""
def __main__():
    hero = Character("Hero", 10, 50, 5, 2)
    villain = Character("Villain", 10, 10, 5, 0)
#     hero.name = "Hero"
#     hero.hitPoints = 10
#     hero.hitChance = 50
#     hero.maxDamage = 5
#     hero.armor = 2
    print(Character.printStats(hero))
    fight(hero, villain)
    
class Character(object):
    def __init__(self, name, hitPoints, hitChance, maxDamage, armor):
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
                print("Hit Chance must be positive.")
                self.__hitChance = 1
        else:
            print("Hit Chance must be a number.")
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
#Why does it keep printing none???

def fight(character1, character2):
    
    
__main__()
    
            
        
        
        