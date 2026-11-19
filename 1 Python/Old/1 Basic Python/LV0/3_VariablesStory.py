character_name = "X"
character_lifetime = "12"

A = "[Narrator]"
B = "[???]"
C = "[Zahara]"

print(A + "The end of humanity is near")
print(A + "Our hero，" + character_name + " stands against the destroyer of worlds")
print(A + "At the end of time, the beginning of the repeat")
print(C + "What makes you stand in front of me, " + character_name + "? You Should cower in fear!")
print(B + "I've lived for " + character_lifetime + " millennium and protected the destruction of countless species from your hands")
print(B + "I, " + character_name + ", don't mind doing it again!")
print(C + "Oh, you, " + character_name + " lived for " + character_lifetime + " millennium I see")


character_name = character_name + character_lifetime
B = "[" + character_name + "]"

print(B + "You fool! My true name is " + character_name + "!")


