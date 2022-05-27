import random

Chartype    = str(input("\nPokemon Character Type:"))
CharLvl     = int(input("Charizard's Level: "))
SpcAtt      = int(input("Special Attack: "))
Stype       = str(input("Skill Type: "))
power       = int(input("Power: "))
FerLvl      = int(input("\nFeraligatr's Level: "))
SpcDef      = int(input("Special Defense: "))
Etype       = str(input("Enemy Type: "))
badge       = int(input("\nGeneration: "))
weather     = int(input("[1] Beneficial [2] Against [3] Normal \nWeather: "))
target      = int(input("Target/s: "))


def modifier (target, weather, badge, Chartype, Stype, Etype):
    
    # Target
    if target == 1:
        target = 1
    else:
        target = .5

    # Weather
    if weather == 1:
        weather = 1.5
    if weather == 2:
        weather = 0.5
    if weather == 3:
        weather = 1

    # Badge
    if badge == 2:
        badge = 1.25
    else:
        badge = 1

    # Stab  
    if Chartype == "fire" and Stype == "fire":
        effect2 = 1.5
    else:
        effect2 = 1
    stab = effect2

    # Random
    rand = [.85 , 1]
    rando = random.choice(rand)

    # Critical
    crit= [1 , 2]
    critic = random.choice(crit)
    if critic == 2:
        print("\nA Critical Hit\n")
    
    # Burn
    burnn = [0.5 , 1]
    burn = random.choice(burnn)
    if burn == .5:
        print("\nThe attacker was burned")

    # Other
    other = 1

    # TYPE
    if Stype == "fire" and Etype == "water":
        effect = .5
    if Stype == "fire" and Etype == "fire":
        effect = .5
    if Stype == "fire" and Etype == "rock":
        effect = .5  
    if Stype == "fire" and Etype == "dragon":
        effect = .5 
    if Stype == "fire" and Etype == "normal":
        effect = 1
    if Stype == "fire" and Etype == "fighting":
        effect = 1
    if Stype == "fire" and Etype == "flying":
        effect = 1
    if Stype == "fire" and Etype == "poison":
        effect = 1
    if Stype == "fire" and Etype == "ground":
        effect = 1
    if Stype == "fire" and Etype == "ghost":
        effect = 1
    if Stype == "fire" and Etype == "electric":
        effect = 1
    if Stype == "fire" and Etype == "psychic":
        effect = 1
    if Stype == "fire" and Etype == "dark":
        effect = 1
    if Stype == "fire" and Etype == "fairy":
        effect = 1
    if Stype == "fire" and Etype == "bug":
        effect = 2
    if Stype == "fire" and Etype == "steel":
        effect = 2
    if Stype == "fire" and Etype == "grass":
        effect = 2
    if Stype == "fire" and Etype == "ice":
        effect = 2

    type = effect
    
    # Attack Condition
    if type <= .5:
        print("Attack is not very effective")
    if type >= 2:
        print("SUPER EFFECTIVE!")
    else:
        type == 1

    # Calculation for Mod
    mod = target * weather * badge * burn * other * critic * rando * type * stab
    return mod

# Calculation for DMG
damage = ((((((2*CharLvl)/5)+2)* power * SpcAtt / SpcDef)/50)+2) * modifier(target, weather, badge, Chartype, Stype, Etype)
print("Charizards Damage to Feraligatr is:", damage)