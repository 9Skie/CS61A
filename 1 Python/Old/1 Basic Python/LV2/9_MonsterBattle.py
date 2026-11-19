def battle(hp):
    print("You have encountered an/a " + Monster_Kind[random.randint (0,7)] + " who has [" + str(hp) + "] hp!")
    print("It's time to battle!")
    damage = int(input("Attack with a damage: "))
    hp = hp - damage
    health_check(hp)
    while hp >= 0:
        print("Do another hit!")
        damage = int(input("Attack with a damage: "))
        hp = hp - damage
        health_check(hp)

def health_check(hp):
    if hp >= 0:
        print("\nThe enemy still has [" + str(hp) + "] hp left!")
    else:
        print("\nThe enemy is dead! You gained [" + str(exp) + "] exp!")
        print("Phew, that was a tough battle.")


import random

Monster_Kind = ["Goblin", "Hound", "Ghoul", "Sweeper", "Giant", "Dragon", "Elemental Spirit", "Fusion"]

 
hp = 100 * random.randint (0,50)
exp = random.randint (0,100)
battle(hp)
