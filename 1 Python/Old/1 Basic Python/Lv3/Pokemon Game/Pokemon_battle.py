# This will be the actual code running the battle between the two pokemons
# So it's a turn based game, and the game ends with one side losing it's hp to =< 0
# The players will be given 4 random ability combos (geez I need to make 16 abilities) with their own named pokemon

# Each turn they can use 1 ability, for damage, damage can be ones with side effects such as poison, burning, bleeding,
# etc. A damage ability can do massive damage but have a low chance of hitting, or can do rapid amounts of low damage,

# buff (self) such as increase stats (hp, attack, defense), increase ability multiplier,
# increasing one's chance of critical rate, dodge rate, or gain life steal etc.

# they can debuff (enemy) such as decrease stats (hp, attack, defense)

# defense in the game is calculated as damage - defense = true damage taken

# punch is damage with chance of stun, slash is damage with bleed,
# crush reduces defense, whirlwind increases in damage the more used but has low basic damage

# there is a chance to dodge and a chance to crit
# this code would've been much more easier if we were to use the self function to write all these def's

from Pokemon_stats import Pokemon
from random import randint


def punch(your_stats, opponent_stats, opponent_is_stunned):
    stun_chance = 20
    damage = your_stats.attack * 1.2
    damage = round(damage)
    damage, did_crit = Pokemon.successful_crit_check(your_stats, damage)
    if did_crit is True:
        print("The attack has critted! Double damage!")
    damage, did_dodge = Pokemon.successful_dodge_check(opponent_stats, damage)
    if did_dodge is True:
        print("The opponent has dodged the attack!")
        actual_damage = damage
    else:
        if stun_chance >= randint(0, 99):
            opponent_is_stunned = True
            print("The opponent has been stunned!")
        actual_damage = Pokemon.damage_dealt(opponent_stats, damage)
        if actual_damage < 0:
            actual_damage = 0
        opponent_stats.health_point = opponent_stats.health_point - actual_damage
    return opponent_stats, actual_damage, opponent_is_stunned


def slash(your_stats, opponent_stats, opponent_is_bleeding, opponent_bleed_counter):
    damage = your_stats.attack * 0.9
    damage = round(damage)
    damage, did_crit = Pokemon.successful_crit_check(your_stats, damage)
    if did_crit is True:
        print("The attack has critted! Double damage!")
    damage, did_dodge = Pokemon.successful_dodge_check(opponent_stats, damage)
    if did_dodge is True:
        print("The opponent has dodged the attack!")
        actual_damage = damage
    else:
        actual_damage = Pokemon.damage_dealt(opponent_stats, damage)
        if actual_damage < 0:
            actual_damage = 0
        opponent_stats.health_point = opponent_stats.health_point - actual_damage
        opponent_is_bleeding = True
        opponent_bleed_counter = 2
    return opponent_stats, actual_damage, opponent_is_bleeding, opponent_bleed_counter


def crush(your_stats, opponent_stats):
    damage = your_stats.attack * 1.0
    damage = round(damage)
    damage, did_crit = Pokemon.successful_crit_check(your_stats, damage)
    if did_crit is True:
        print("The attack has critted! Double damage!")
    damage, did_dodge = Pokemon.successful_dodge_check(opponent_stats, damage)
    if did_dodge is True:
        print("The opponent has dodged the attack!")
        actual_damage = damage
    else:
        opponent_stats.defense = opponent_stats.defense - 15
        actual_damage = Pokemon.damage_dealt(opponent_stats, damage)
        if actual_damage < 0:
            actual_damage = 0
        opponent_stats.health_point = opponent_stats.health_point - actual_damage
    return opponent_stats, actual_damage


def whirlwind(your_stats, opponent_stats, your_stack_count):
    damage = your_stats.attack * 0.3 * your_stack_count
    damage = round(damage)
    your_stack_count += 1
    (damage, did_crit) = Pokemon.successful_crit_check(your_stats, damage)
    if did_crit is True:
        print("The attack has critted! Double damage!")
    (damage, did_dodge) = Pokemon.successful_dodge_check(opponent_stats, damage)
    if did_dodge is True:
        print("The opponent has dodged the attack!")
        actual_damage = damage
    else:
        actual_damage = Pokemon.damage_dealt(opponent_stats, damage)
        if actual_damage < 0:
            actual_damage = 0
        opponent_stats.health_point = opponent_stats.health_point - actual_damage
    return opponent_stats, actual_damage, your_stack_count


def battle_cry(your_stats):  # atk_up
    your_stats.attack += 50
    print("Your pokemon\'s attack increased by 50!")
    return your_stats


def healing_potion():  # hp_regen
    your_is_healing = True
    your_heal_counter = 3
    return your_is_healing, your_heal_counter


def iron_skin(your_stats):  # def_up
    your_stats.defense += 30
    print("Your pokemon's defense increased by 30!")
    return your_stats


def decipher(your_stats):  # crit_up
    your_stats.crit_chance += 10
    print("Your pokemon's crit% increased by 10!")
    return your_stats


def ninjutsu(your_stats):  # dodge_up
    your_stats.dodge_chance += 10
    print("Your pokemon's dodge% increased by 10!")
    return your_stats


def wither(opponent_stats):  # atk_down
    opponent_stats.attack -= 25
    print("Your opponent's pokemon's attack decreased by 25!")
    return opponent_stats


def corrosion(opponent_stats):  # def_down
    opponent_stats.defense -= 25
    print("Your opponent's pokemon's defense decreased by 25!")
    return opponent_stats


def confusion(opponent_stats):  # crit_down
    opponent_stats.crit_chance -= 5
    print("Your opponent's pokemon's crit% decreased by 5!")
    return opponent_stats


def slime(opponent_stats):  # dodge_down
    opponent_stats.dodge_chance -= 5
    print("Your opponent's pokemon's dodge% decreased by 5!")
    return opponent_stats


player_round_count = 1
player_input_count = 0
ability_amount = 0

p1_stunned = False
p1_bleeding = False
p1_healing = False
p1_valid_ability = False
p1_heal_count = 3
p1_bleed_count = 2
p1_whirlwind_stack_count = 1

p2_stunned = False
p2_bleeding = False
p2_healing = False
p2_valid_ability = False
p2_heal_count = 3
p2_bleed_count = 2
p2_whirlwind_stack_count = 1


ability_list_offense = ["punch", "slash", "crush", "whirlwind"]
ability_list_buff = ["battle_cry", "healing_potion", "iron_skin", "decipher", "ninjutsu"]
ability_list_debuff = ["wither", "corrosion", "confusion", "slime"]


print("Welcome to the game of... a very bad ripoff of Pokemon!")
print("Because the creator is terrible at coding, he can only mimic the game to this degree.\n")

print("In the game, both players will have a respective pokemon, they can name it themselves.")
print("Each pokemon will have 5 stats: atk, hp, def, crit, dodge.")
print("Crit is a chance to deal double the attack damage, dodge means a chance to evade opponent's attack damage.")
print("All basic stats granted to the Pokemon's will range in a variety of numbers.\n")

print("Each pokemon will also have 4 abilities, 2 damaging, 1 buffing, 1 debuffing.")
print("All abilities are shuffled in a card pool. Don't worry, each of them is very basic and easy to understand.")
print("Say no further more! Experience a game and you'll understand how it works!")


while player_input_count < 2:
    print("\n\nGenerating Pokemon stats and abilities...\n")
    while ability_amount < 4:
        if ability_amount == 0:
            ability_1 = ability_list_offense[randint(0, 3)]
            ability_amount += 1
        elif ability_amount == 1:
            ability_2 = ability_list_offense[randint(0, 3)]
            while ability_2 == ability_1:
                ability_2 = ability_list_offense[randint(0, 3)]
            ability_amount += 1
        elif ability_amount == 2:
            ability_3 = ability_list_buff[randint(0, 4)]
            ability_amount += 1
        elif ability_amount == 3:
            ability_4 = ability_list_debuff[randint(0, 3)]
            ability_amount += 1
    if player_round_count == 1:
        atk_threshold = 10 * randint(10, 20)
        hp_threshold = 100 * randint(10, 15)
        def_threshold = 10 * randint(2, 4)
        crit_threshold = 5 * randint(2, 6)
        dodge_threshold = 5* randint(1, 4)
        pokemon1_stats = Pokemon(atk_threshold,
                                 hp_threshold,
                                 def_threshold,
                                 crit_threshold,
                                 dodge_threshold
                                 )
        pokemon1_abilities = [ability_1, ability_2, ability_3, ability_4]
        print("Player 1's pokemon abilities are " + str(pokemon1_abilities))
        print("Player 1's pokemon stats are:\n"
              + "atk: " + str(pokemon1_stats.attack) + "\n"
              + "hp: " + str(pokemon1_stats.health_point) + "\n"
              + "def: " + str(pokemon1_stats.defense) + "\n"
              + "crit%: " + str(pokemon1_stats.crit_chance) + "\n"
              + "dodge%: " + str(pokemon1_stats.dodge_chance) + "\n"
              )
        pokemon1_name = input("Please input a name for your pokemon: ")
        print("Your pokemon's name is now " + str(pokemon1_name) + ".")
        player_input_count += 1
        player_round_count += 1
        ability_amount = ability_amount - 4
    elif player_round_count == 2:
        atk_threshold = 10 * randint(10, 20)
        hp_threshold = 100 * randint(10, 15)
        def_threshold = 10 * randint(2, 4)
        crit_threshold = 5 * randint(2, 6)
        dodge_threshold = 5* randint(1, 4)
        pokemon2_stats = Pokemon(atk_threshold,
                                 hp_threshold,
                                 def_threshold,
                                 crit_threshold,
                                 dodge_threshold
                                 )
        pokemon2_abilities = [ability_1, ability_2, ability_3, ability_4]
        print("Player 2's pokemon abilities are " + str(pokemon2_abilities))
        print("Player 2's pokemon stats are:\n"
              + "atk: " + str(pokemon2_stats.attack) + "\n"
              + "hp: " + str(pokemon2_stats.health_point) + "\n"
              + "def: " + str(pokemon2_stats.defense) + "\n"
              + "crit%: " + str(pokemon2_stats.crit_chance) + "\n"
              + "dodge%: " + str(pokemon2_stats.dodge_chance) + "\n"
              )
        pokemon2_name = input("Please input a name for your pokemon: ")
        print("Your pokemon's name is now " + str(pokemon2_name) + ".")
        player_input_count += 1
        player_round_count -= 1

while pokemon1_stats.health_point > 0 and pokemon2_stats.health_point > 0:
    if player_round_count == 1:
        print("\n\nIt's player 1's turn!")
        print("Go, " + str(pokemon1_name) + "!\n")

        if p1_bleeding is True and p1_bleed_count > 0:
            pokemon1_stats.health_point = pokemon1_stats.health_point - 50
            print("Your pokemon is bleeding! 50 damage will be dealt at the start of the round!")
            p1_bleed_count = p1_bleed_count - 1
            print(str(p1_bleed_count) + " rounds of bleeding left!\n")
        else:
            p1_bleeding = False

        if p1_healing is True and p1_heal_count > 0:
            pokemon1_stats.health_point = pokemon1_stats.health_point + 100
            print("Your pokemon is healing! 100 hp will be restored at the start of the round!")
            p1_heal_count = p1_heal_count - 1
            print(str(p1_heal_count) + " rounds of healing left!\n")
        else:
            p1_healing = False

        if pokemon1_stats.health_point <= 0:
            continue

        print("Player 1's pokemon abilities are " + str(pokemon1_abilities))
        print("Pokemon 1's current stats are:\n"
              + "atk: " + str(pokemon1_stats.attack) + "\n"
              + "hp: " + str(pokemon1_stats.health_point) + "\n"
              + "def:" + str(pokemon1_stats.defense) + "\n"
              + "crit%: " + str(pokemon1_stats.crit_chance) + "\n"
              + "dodge%: " + str(pokemon1_stats.dodge_chance) + "\n"
              )
        if p1_stunned is True:
            player_round_count += 1
            print("Your pokemon is stunned! Your turn will be skipped!")
            p1_stunned = False
            continue

# there's so many logic errors here that I don't know what to say
# I can't reset the statements back to false
# and I cant make it activate once only when its the player's turn

        while p1_valid_ability is False:
            p1_choice = input("Your choice of action is: ")
            if p1_choice in pokemon1_abilities:
                p1_valid_ability = True
            else:
                print("That is not a valid operation!")

        if p1_choice == "punch":
            print("You used \"punch\"!")
            pokemon2_stats, actual_damage, p2_stunned \
                = punch(pokemon1_stats, pokemon2_stats, p2_stunned)
            print("The damage dealt was: " + str(actual_damage))

        elif p1_choice == "slash":
            print("You used \"slash\"!")
            pokemon2_stats, actual_damage, p2_bleeding, p2_bleed_count \
                = slash(pokemon1_stats, pokemon2_stats, p2_bleeding, p2_bleed_count)
            print("The damage dealt was: " + str(actual_damage))

        elif p1_choice == "crush":
            print("You used \"crush\"!")
            pokemon2_stats, actual_damage \
                = crush(pokemon1_stats, pokemon2_stats)
            print("The damage dealt was: " + str(actual_damage))

        elif p1_choice == "whirlwind":
            print("You used \"whirlwind\"!")
            pokemon2_stats, actual_damage, p1_whirlwind_stack_count \
                = whirlwind(pokemon1_stats, pokemon2_stats, p1_whirlwind_stack_count)
            print("The damage dealt was: " + str(actual_damage))
            print("Your stack of whirlwind is now " + str(p1_whirlwind_stack_count) + ".")

        elif p1_choice == "battle_cry":
            print("You used \"battle_cry\"!")
            pokemon1_stats = battle_cry(pokemon1_stats)

        elif p1_choice == "healing potion":
            print("You used \"healing potion\"!")
            p1_healing, p1_heal_count = healing_potion()

        elif p1_choice == "iron_skin":
            print("You used \"iron_skin\"!")
            pokemon1_stats = iron_skin(pokemon1_stats)

        elif p1_choice == "decipher":
            print("You used \"decipher\"!")
            pokemon1_stats = decipher(pokemon1_stats)

        elif p1_choice == "ninjutsu":
            print("You used \"ninjutsu\"!")
            pokemon1_stats = ninjutsu(pokemon1_stats)

        elif p1_choice == "wither":
            print("You used \"wither\"!")
            pokemon2_stats = wither(pokemon2_stats)

        elif p1_choice == "corrosion":
            print("You used \"corrosion\"!")
            pokemon2_stats = corrosion(pokemon2_stats)

        elif p1_choice == "confusion":
            print("You used \"confusion\"!")
            pokemon2_stats = confusion(pokemon2_stats)

        elif p1_choice == "slime":
            print("You used \"slime\"!")
            pokemon2_stats = slime(pokemon2_stats)

# now how do check the validity of the name of the ability that they type in
# how do I make it when they type in the name of the ability they activate it?
# how do I make sure all the required values of the ability can be received from the pokemon stats?

        player_round_count += 1
        p1_valid_ability = False

    elif player_round_count == 2:
        print("\n\nIt's player 2's turn!")
        print("Go, " + str(pokemon2_name) + "!\n")

        if p2_bleeding is True and p2_bleed_count > 0:
            pokemon2_stats.health_point = pokemon2_stats.health_point - 50
            print("Your pokemon is bleeding! 50 damage will be dealt at the start of the round!")
            p2_bleed_count = p2_bleed_count - 1
            print(str(p2_bleed_count) + " rounds of bleeding left!\n")
        else:
            p2_bleeding = False

        if p2_healing is True and p2_heal_count > 0:
            pokemon2_stats.health_point = pokemon2_stats.health_point + 100
            print("Your pokemon is healing! 100 hp will be restored at the start of the round!")
            p2_heal_count = p2_heal_count - 1
            print(str(p2_heal_count) + " round of healing left!\n")
        else:
            p2_healing = False

        if pokemon2_stats.health_point <= 0:
            continue

        print("Player 2's pokemon abilities are " + str(pokemon2_abilities))
        print("Player 2's pokemon stats are:\n"
              + "atk: " + str(pokemon2_stats.attack) + "\n"
              + "hp: " + str(pokemon2_stats.health_point) + "\n"
              + "def:" + str(pokemon2_stats.defense) + "\n"
              + "crit%: " + str(pokemon2_stats.crit_chance) + "\n"
              + "dodge%: " + str(pokemon2_stats.dodge_chance) + "\n"
              )
        if p2_stunned is True:
            player_round_count -= 1
            print("Your pokemon is stunned! Your turn will be skipped!")
            p2_stunned = False
            continue

        while p2_valid_ability is False:
            p2_choice = input("Your choice of action is: ")
            if p2_choice in pokemon2_abilities:
                p2_valid_ability = True
            else:
                print("That is not a valid operation!")

        if p2_choice == "punch":
            print("You used \"punch\"!")
            pokemon1_stats, actual_damage, p1_stunned \
                = punch(pokemon2_stats, pokemon1_stats, p1_stunned)
            print("The damage dealt was: " + str(actual_damage))

        elif p2_choice == "slash":
            print("You used \"slash\"!")
            pokemon1_stats, actual_damage, p1_bleeding, p1_bleed_count \
                = slash(pokemon2_stats, pokemon1_stats, p1_bleeding, p1_bleed_count)
            print("The damage dealt was: " + str(actual_damage))

        elif p2_choice == "crush":
            print("You used \"crush\"!")
            pokemon1_stats, actual_damage \
                = crush(pokemon2_stats, pokemon1_stats)
            print("The damage dealt was: " + str(actual_damage))

        elif p2_choice == "whirlwind":
            print("You used \"whirlwind\"!")
            pokemon1_stats, actual_damage, p2_whirlwind_stack_count \
                = whirlwind(pokemon2_stats, pokemon1_stats, p2_whirlwind_stack_count)
            print("The damage dealt was: " + str(actual_damage) + "\n")
            print("Your stack of whirlwind is now " + str(p2_whirlwind_stack_count) + ".")

        elif p2_choice == "battle_cry":
            print("You used \"battle_cry\"!")
            pokemon2_stats = battle_cry(pokemon2_stats)

        elif p2_choice == "healing potion":
            print("You used \"healing potion\"!")
            p2_healing, p2_heal_count = healing_potion()

        elif p2_choice == "iron_skin":
            print("You used \"iron_skin\"!")
            pokemon2_stats = iron_skin(pokemon2_stats)

        elif p2_choice == "decipher":
            print("You used \"decipher\"!")
            pokemon2_stats = decipher(pokemon2_stats)

        elif p2_choice == "ninjutsu":
            print("You used \"ninjutsu\"!")
            pokemon2_stats = ninjutsu(pokemon2_stats)

        elif p2_choice == "wither":
            print("You used \"wither\"!")
            pokemon1_stats = wither(pokemon1_stats)

        elif p2_choice == "corrosion":
            print("You used \"corrosion\"!")
            pokemon1_stats = corrosion(pokemon1_stats)

        elif p2_choice == "confusion":
            print("You used \"confusion\"!")
            pokemon1_stats = confusion(pokemon1_stats)

        elif p2_choice == "slime":
            print("You used \"slime\"!")
            pokemon1_stats = slime(pokemon1_stats)

        player_round_count -= 1
        p2_valid_ability = False


if pokemon1_stats.health_point <= 0:
    print("Player 2 wins!")
elif pokemon2_stats.health_point <= 0:
    print("Player 1 wins!")
