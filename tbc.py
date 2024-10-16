"""Marianne Adams
10/18/2024
CS120 Turn Based Combat Module
Defines Character class and fight function"""
class Character(object):
    def _init_(self, name, maxDamage, hitChance, hitPoints, armor):
        self._name = name
        self._maxDamage = maxDamage
        self._hitChance = hitChance
        self._hitPoints = hitPoints
        self._armor = armor
        
    @property
    def characterName(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def maxDamage(self):
        return self._maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if value == int:
            if value >= 0:
                self._maxDamage = value
            else:
                print ("Maximum Damage must be positive.")
                self._maxDamage = 1
        else:
            print("Maximum damage must be a number.")
            self._maxDamage = 1
    
    @property
    def hitPoints(self):
        return self._hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if value == int:
            self._hitPoints = value
        else:
            print("Hit Points must be a number.")
            self._hitPoints = 10
            
    @property
    def hitChance(self):
        return self._hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        if value == int:
            
        
        
        