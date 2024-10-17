"""Marianne Adams
CS120 Turn Based Combat System
Combat Sequence"""
import meadams2_tbc
def main():
    hero = meadams2_tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    monster = meadams2_tbc.Character("Monster", 20, 30, 5, 0)
    hero.printStats()
    monster.printStats()
    meadams2_tbc.fight(hero, monster)

if __name__ == "__main__":
    main()

