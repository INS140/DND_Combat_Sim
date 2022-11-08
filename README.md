# Hello and welcome to my DND Combat Simulator!!!

This is a work in progress, but I hope to develop this into a fully functional app. As for now, the features are still very limited. I have added options for multiple combatants, actions during combat, and even all of the weapons in the Player's Handbook! (the net doesn't work though ...)

I still have A LOT of work left to do

## How to play

To play the game, you will need to run main.py.

### Before combat:

At the start you will be asked to state how many combatants will be joining the fight, and then you will assign monster types. The availble monster types as of now are:
- Acolyte (Spellcaster)
- Gnoll
- Skeleton
- Zombie

If you look in the code you will notice a Player monster type, however this is outdated and needs to be fixed.

After you select the monster type, the combatant will need a name. It is ***VERY IMPORTANT*** to name them with unique names, this is how targetting is determined during combat.

### Start of combat:

At the start of combat you will see two lists and a Round number. In DND, one Round is equivalent to 6 seconds. The lists are for names and initiative references, they are ordered so that each name lines up with its respective initiative. These lists will be updated, as well as the Round number, after each combatant has taken their turn.

Whoever rolls the highest Initiative will go first.

### Combatant turns:

At the start of a combatant's turn, a reference for that combatant will appear. This will have all of the important stats associated with the current combatant. This includes equipped weapons as well.

During a combantant's turn, you will be prompted to give them commands. Combatants have a few actions they can take during their turn (actions followed by their in-game commands):

- Actions
    - Attack - atk - attack another combatant with a melee attack
    - Cast - cast - cast a spell (damage only for now)
    - Defend - def - temporarily increase AC until next turn
    - Run - run - forfeit
    - Move - Coming soon!
- Other
    - Options - options - opens a list of options, ex. setting new stats or equipping new weapons
    - Help - help - gives a list of combatant commands
    - End - end - ends the current combatants turn

Each combatant can only take one action per turn. The other commands, can be used multiple times, however you may only equip or remove one weapon per turn using options. This is true for all other commands except end, which will immediately end the current turn.

After the combatant can no longer take any actions, they will need to be commanded to end their turn. This is to ensure that a turn is not ended prematurely.

### Actions Explained:

#### Attack

If you command the combatant to take the attack action, you will be prompted to give a target. You will need to supply the name of another combatant, and then you will be asked to provide a dice roll. If you don't have any dice, think of a random number from 1 to 20 and input that. 1 is a critical failure, and 20 is a critical hit. The combatants modifiers will be added to the dice roll, and if the total is equal to or higher than the target's AC, the attack will hit. Critical failures always miss and critical hits always hit AND do double dice damage (modifiers are unaffected).

#### Cast

Commanding a combatant to take the cast action requires that they are a spellcaster, otherwise it will fail and another command will need to be input. During the cast action you will first choose which spell to cast. Each spellcaster combatant has a specific list of spells they are allowed to cast, for now you will have to look at Monsetr_SB.py to see these spells. The only spells that are available at the moment do damage, and so a target will need to be provided. Just like with the attack action, a dice roll will need to be provided, however it is not always the attacker who must roll. In the case that the target has to make a saving throw, the target will instead make the dice roll with their modifiers added to the total. If the attacker rolls and the total is equal to or above the targets AC, the spell hits. If the target makes a saving throw and it is equal to or higher than the attackers Spell Save DC, the spell misses.

#### Defend

If a combatant takes the defend action, their AC will be increased until the start of their next turn. This makes them harder to hit, but a critical hit will still always hit.

### Beginning of the next Round:

At the beginning of each Round, the reference lists for Initiative and names will be updated based off of which combatants are left. If no combatants were slain or ran away, the lists remain unchanged. A Round ends when all combatants have taken their turn.

### After combat:

When there is only one combatant left standing, whether that be by annihilation or the others running away, the game will end. At the end of the game the winner is displayed at the bottom.

## If you are unfamiliar with DND

This section is just for you. Here I'll go over the vocabulary that I have implemented in this simulator so far. Some of these terms have not been applied yet, however they will be relevant eventually.

### Vocabulary

- Game terms:
    - D_value - number of sides on a die
    - Advantage - roll two d20's and take the higher number
    - Disadvantage - roll two d20's and take the lower number
    - Saving throw - roll a d20 to determine whether you avoid harmful effects
- Stats:
    - HP - Hit Points, health
    - AC - Armor Class, defense
    - SP - Spell Points, magic usage, the books use Spell Slots instead
    - Init - Initiative, determines combat order, higher numbers go first
    - Prof - Proficiency, adds bonus when called
    - STRmod - Strength modifier, determines bonuses to attack
    - DEXmod - Dexterity modifier, determines bonuses to initiative and attack
    - CONmod * - Constitution modifier, determines bonuses to HP
    - INTmod - Intelligence modifier, used for spellcasting/ability checks
    - WISmod * - Wisdom modifier, used for spellcasting/ability checks
    - CHAmod * - Charisma modifier, used for spellcasting/ability checks
    - Speed * - Distance(ft) a combatant can travel in one turn
- Combat:
    - Action - The number of actions that can be resolved during a turn, ex. attack a target
    - Subtle Action - An action that is done in tandum with the main Action, ex. equip a weapon before an attack
    - Bonus Action * - An action that can happen along side a normal Action
    - Reaction * - An action that can be taken at any time once per round
    - Attack Number * - Number of attacks per turn
- Weapons:
    - Finesse - allows the attacker to use either STR or DEX as attack/damage modifier
    - Heavy * - small and tiny creatures have disadvantage using this weapon
    - Light * - if equipped in both hands, can make a bonus attack with second weapon
    - Loading * - can only be fired once per turn, even with multiattack
    - Reach * - melee range is increased by 5ft
    - Special * - weapon with specific rules
    - Thrown - can be used to make a ranged attack without disadvantage
    - Two-handed - requires two hands to weild
    - Versatile - can be weilded with one or two hands, if two d_value increases

\* Not applied yet

## Continued Development

I will be updating this page as I apply more content to the simulator. It has been a fun and exciting process so far, and I can not wait to see what the finished product looks like!