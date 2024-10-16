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
        
        
        
        